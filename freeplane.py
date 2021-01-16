#!/usr/bin/env python
#-*- coding: utf-8 -*-




#
# DESCRIPTION
#
# a library holding useful and object-oriented functionalities to interface with
# a (freeplane) mindmap. using this library, information can easily be extracted
# and used in a programmatical way without having to browse through the mindmap
# itself.
#
#
# AUTHOR
#
#   - nnako, 2016
#


# generals
from __future__ import print_function
import argparse
import datetime
import os
import re
import sys
import io

# xml format
import lxml.etree as ET

# html format
import html2text

# BUILTIN ICONS
ICON_EXCLAMATION = 'yes'
ICON_LIST = 'list'
ICON_QUESTION = 'help'
ICON_CHECKED = 'button_ok'
ICON_BOOKMARK = 'bookmark'
ICON_PRIO1 = 'full-1'
ICON_PRIO2 = 'full-2'


# MINDMAP

class Mindmap(object):

    """
    Freeplane interfacing class

    Access Freeplane mindmap file and do various search, read and write
    operations to retrieve or modify text passages within the mindmap.

    """

    _num_of_maps = 0


    def __init__(self, path='', mtype='freeplane', version='1.3.0', id=''):




        #
        # check for command line arguments
        #

        # do this only if called from the command line
        if id == 'cli':

            # define information
            parser = argparse.ArgumentParser(
                    description='Operation on Freeplane mindmap',
                    usage='''%s <command> [<args>]

                    Possible commands are:
                        getText    return text portion of a node
                        test       test this library
                        ...               ...''' % os.path.basename(sys.argv[0]))

            # define command argument
            parser.add_argument(
                    'command',
                    help='Subcommand to run'
                    )




            #
            # read out CLI and execute main command
            #

            # get main arguments from user
            args = parser.parse_args(sys.argv[1:2])

            # check if command is provided in script
            if not hasattr(self, args.command):

                print( 'Unrecognized command' )
                parser.print_help()
                exit(1)

            # use dispatch pattern to invoke method with same name
            getattr(self, args.command)()




        #
        # update class variables
        #

        Mindmap._num_of_maps += 1




        #
        # access instance variables
        #

        # path of instance's mindmap file
        self._path = path

        # type, version
        self._type = mtype




        #
        # read mindmap in case path is given
        #

        # check for validity of file
        if os.path.isfile(self._path):




            #
            # determine file's map version
            #

            with io.open(self._path, "r", encoding="utf-8") as fpMap:
                strFirstLine = fpMap.readline()

            # detect from '<map version="freeplane 1.3.0">'
            idxFpToken    = strFirstLine.find("freeplane")
            idxSpace      = strFirstLine[idxFpToken:].find(" ") + idxFpToken
            idxVer        = idxSpace+1
            idxClQuote    = strFirstLine[idxVer:].find('"') + idxVer
            self._version = strFirstLine[idxVer:idxClQuote]




            #
            # set parser encoding due to map version
            #

            # check for fitting encoding
            encoding = get_version_specific_file_encoding(self._version)

            # set encoding to be read
            xmlparser = ET.XMLParser(encoding=encoding)
            # xmlparser = ET.XMLParser(encoding="latin1")
            # xmlparser = ET.XMLParser(encoding="utf-8")




            #
            # read entire mindmap and evaluate structure
            #

            self._mindmap = ET.parse(self._path, parser=xmlparser)

            # get root of mindmap
            self._root = self._mindmap.getroot()

            # find and get first node element of etree
            self._rootnode = self._root.find('node')

            # build parent map (using ElementTree nodes)
            self._parentmap = {c:p for p in self._rootnode.iter() for c in p}




            return




        #
        # create mindmap if path is invalid or empty
        #

        # set version
        self._version = version

        # build parent map (using ElementTree nodes)
        self._parentmap = {}

        # create map element
        self._mindmap = ET.Element('map') 
        self._mindmap.attrib['version'] = 'freeplane ' + self._version

        # get root of mindmap
        self._root = self._mindmap

        # some attributes
        _node = ET.Element('attribute_registry') 
        _node.attrib['SHOW_ATTRIBUTES'] = 'hide'
        self._mindmap.append(_node)

        # 1st node element
        self._rootnode = ET.Element('node') 
        self._rootnode.attrib["LOCALIZED_TEXT"] = "new_mindmap"
        self._rootnode.attrib["FOLDED"] = "false"
        self._mindmap.append(self._rootnode)

        # some styles
        _node = ET.Element('edge') 
        _node.attrib['STYLE'] = 'horizontal'
        _node.attrib['COLOR'] = '#cccccc'
        self._mindmap.append(_node)

        #
        # create hook element
        #

        _hook = ET.Element('hook') 
        _hook.attrib["NAME"] = "MapStyle"
        _hook.attrib["zoom"] = "0.62"
        self._mindmap.append(_hook)
        # sub element properties
        _node = ET.Element('properties')
        _node.attrib["show_icon_for_attributes"] = "false"
        _node.attrib["show_note_icons"] = "false"
        _hook.append(_node)
        # sub element map styles
        _mapstyles = ET.Element('map_styles')
        _hook.append(_mapstyles)
        # sub sub element stylenode
        _stylenode = ET.Element('stylenode')
        _stylenode.attrib["LOCALIZED_TEXT"] = "styles.root_node"
        _mapstyles.append(_stylenode)
        # sub sub sub element stylenode
        _node = ET.Element('stylenode')
        _node.attrib["LOCALIZED_TEXT"] = "styles.predefined"
        _node.attrib["POSITION"] = "right"
        _stylenode.append(_node)
        # sub sub sub element stylenode
        _node = ET.Element('stylenode')
        _node.attrib["LOCALIZED_TEXT"] = "default"
        _node.attrib["MAX_WIDTH"] = "600"
        _node.attrib["COLOR"] = "#000000"
        _node.attrib["STYLE"] = "as_parent"
        _stylenode.append(_node)
        # sub sub sub element stylenode
        _node = ET.Element('font')
        _node.attrib["NAME"] = "Segoe UI"
        _node.attrib["SIZE"] = "12"
        _node.attrib["BOLD"] = "false"
        _node.attrib["ITALIC"] = "false"
        _stylenode.append(_node)


# MAP

    @classmethod
    def getNumOfMaps(cls):
        return cls._num_of_maps


    @property
    def RootNode(self):
        return Node(self._rootnode, self)


    @property
    def Styles(self):
        _style = {}

        _stylenode_user = self._mindmap.find('.//stylenode[@LOCALIZED_TEXT="styles.user-defined"]')
        _lst = _stylenode_user.findall('./stylenode[@TEXT]')
        for _sty in _lst:
            _item = {}

            # style name
            _name = _sty.get('TEXT', '')

            # foreground color
            _color = _sty.get('COLOR', '')
            if _color:
                _item['color'] = _color

            # background color
            _bgcolor = _sty.get('BACKGROUND_COLOR', '')
            if _bgcolor:
                _item['bgcolor'] = _bgcolor

            # font
            _sty_sub = _sty.find('./font')
            if _sty_sub is not None:
                # font name
                _fontname = _sty_sub.get('NAME', '')
                _item['fontname'] = _fontname
                # font size
                _fontsize = _sty_sub.get('SIZE', '')
                _item['fontsize'] = _fontsize

            # ...

            # add to dict
            _style[_name] = _item

        return _style


    def addStyle(self,
                name='',
                settings={},
                ):
        """
        This functions adds a style to a mindmap
        """




        #
        # create new style within mindmap
        #

        if name:



            #
            # check validity of requests
            #

            # look for parent element
            _stylenode_user = self._mindmap.find('.//stylenode[@LOCALIZED_TEXT="styles.user-defined"]')

            # get list of existing style elements
            _lst = _stylenode_user.findall('./stylenode[@TEXT]')

            # leave function if style is already existing
            for _sty in _lst:
                if name.lower() == _sty.get('TEXT').lower():
                    return False

            # create element
            _sty = ET.Element("stylenode", TEXT=name)

            # append element to list of styles
            _stylenode_user.append(_sty)




            #
            # set attributes
            #

            # foreground color
            _check = 'color'
            if _check in settings.keys():
                _sty.set('COLOR', settings[_check])

            # background color
            _check = 'bgcolor' 
            if _check in settings.keys():
                _sty.set('BACKGROUND_COLOR', settings[_check])

            # font name
            _check = 'fontname'
            if _check in settings.keys():
                _item = ET.Element('font', NAME=settings[_check])
                # add item to style
                _sty.append(_item)
            # font size
            _check = 'fontsize'
            if _check in settings.keys():
                _item.set("SIZE", settings[_check])

            return True

        return False


    def findNodes(self,
            id='',
            core='',
            attrib='',
            details='',
            notes='',
            link='',
            icon='',
            exact=False
            ):




        #
        # find list of nodes in map
        #

        # start with ALL nodes within the mindmap and strip down to the number
        # of nodes matching all given arguments

        # list all nodes regardless of further properties
        lstNodes = self._root.findall(".//node")

        # do the checks on the base of the list
        lstNodes = reduce_node_list(
            lstNodes,
            id,
            core,
            attrib,
            details,
            notes,
            link,
            icon,
            exact
        )





        #
        # create Node instances
        #

        lstNodesRet = []
        for _node in lstNodes:
            lstNodesRet.append(Node(_node, self))

        return lstNodesRet


    def save(self, strPath, encoding=''):




        #
        # auto-determine and set encoding
        #

        # check for fitting encoding
        if not encoding:
            encoding = get_version_specific_file_encoding(self._version)




        #
        # create XML formatted output string
        #

        # create output string
        _outputstring = ET.tostring(
            self._root,
            pretty_print=True,
            method='xml',
            encoding=encoding,
            ).decode(encoding)




        #
        # sanitize string content
        #

        # prior to v1.8.0 the mindmap file was not a real XML and also not
        # consequently encoded in a specific code format. rather the encoding
        # is a mixture between "latin1" and "windows-1252". thus, in Germany,
        # at least the german special characters must be corrected to be
        # properly displayed within freeplane.

        _version = self._version.split('.')
        if int(_version[0]) == 1 and int(_version[1]) < 8:

            # #160 characters representing <SPACE>
            _outputstring = _outputstring.replace( chr(160),' ')

            # german special characters
            _outputstring = _outputstring.replace( 'ä','&#xe4;') # &#228
            _outputstring = _outputstring.replace( 'ö','&#xf6;') # &#246
            _outputstring = _outputstring.replace( 'ü','&#xfc;') # &#252
            _outputstring = _outputstring.replace( 'Ä','&#xc4;')
            _outputstring = _outputstring.replace( 'Ö','&#xd6;')
            _outputstring = _outputstring.replace( 'Ü','&#xdc;')
            _outputstring = _outputstring.replace( 'ß','&#xdf;')




        #
        # write content into file
        #

        # remove first line if not starting with "<map"
        # as Freeplane doesn't use strict XML
        if not _outputstring.startswith("<map"):
            _outputstring = _outputstring.split('\n', 1)[1]

        # open output file
        _file = io.open(strPath, "w", encoding=encoding)

        # write output string
        _file.write( _outputstring )

        # close file
        _file.close()


    def test(self):

        strExamplePath = "example__code2mm__v1_8_11.mm"
        # strExamplePath = "example__code2mm.mm"
        mm = Mindmap(strExamplePath)
        dicStyles = mm.Styles
        print(dicStyles)
        mm.save(strExamplePath[:strExamplePath.rfind('.')] + '__save.mm')




# NODE

class Node(object):

    def __init__(self, node, map):

        #
        # initialize instance
        #

        self._map = map
        self._node = node


    @property
    def PlainText(self):
        return getCoreTextFromNode(self._node, bOnlyFirstLine=False)


    @PlainText.setter
    def PlainText(self, strText):
        self._node.attrib['TEXT'] = strText


    @property
    def Link(self):
        return self._node.attrib.get("LINK","")


    @Link.setter
    def Link(self, strLink):
        self._node.attrib["LINK"] = strLink


    @property
    def Id(self):
        return self._node.attrib['ID']


    @property
    def Attributes(self):
        _attribute = {}
        _lst = self._node.findall('attribute')
        for _attr in _lst:
            _name = _attr.get('NAME', '')
            _value = _attr.get('VALUE', '')
            if _name:
                _attribute[_name] = _value
        return _attribute


    def addAttribute(self,
                key='',
                value='',
                ):
        """
        This functions adds an attribute to a node
        """




        #
        # create new attribute within node
        #

        if key:

            # create element
            _attrib = ET.Element("attribute", NAME=key, VALUE=value)

            # append element
            _node = self._node.append(_attrib)

        # return self.Attributes


    @property
    def Style(self):
        if 'STYLE_REF' in self._node.attrib.keys():
            return self._node.attrib['STYLE_REF']
        return ""


    @property
    def CreationDate(self):

        # check for TEXT attribute
        if self._node.get('CREATED'):

            # read out text content
            text = self._node.attrib['CREATED']

            # convert to float time value
            time = float(text)/1000

            # return datetime value
            return datetime.datetime.fromtimestamp(time).timetuple()

        return tuple()


    @property
    def ModificationDate(self):

        # check for TEXT attribute
        if self._node.get('MODIFIED'):

            # read out text content
            text = self._node.attrib['MODIFIED']

            # convert to float time value
            time = float(text)/1000

            # return datetime value
            return datetime.datetime.fromtimestamp(time).timetuple()

        return tuple()


    @property
    def CoreLink(self):

        # check for TEXT attribute
        if self._node.get('TEXT'):

            # read out text content
            text = self._node.attrib['TEXT']

            # check for formula identifier
            if text[0] == "=":




                #
                # check for reference to external node
                #

                # identify link based on type (file, http, ...)




                #
                # check for reference to internal node content
                #

                _match=re.match(r'^.*ID_([\d]+)\.text.*', text)
                if _match:
                    return 'ID_' + _match.group(1)




        return ""


    @property
    def Comment(self):

        # check for existence of child
        if not self._node.find('node') is None:

            # get first child
            node = self._node.find('node')

            # check for TEXT attribute
            if not node.get('TEXT') is None:

                # read out text content
                return node.attrib['TEXT']

        return ""


    @property
    def Details(self):

        _text = ''

        # check for details node
        _lstDetailsNodes = self._node.findall("./richcontent[@TYPE='DETAILS']")
        if _lstDetailsNodes:
            _text = ''.join(_lstDetailsNodes[0].itertext()).strip()

        return _text


    @Details.setter
    def Details(self, strDetails):

        # remove existing details element
        _lstDetailsNodes = self._node.findall("./richcontent[@TYPE='DETAILS']")
        if _lstDetailsNodes:
            self._node.remove(_lstDetailsNodes[0])

        # create new details element
        if strDetails:

            # build html structure
            _element = ET.Element("richcontent", TYPE='DETAILS')
            _html = ET.SubElement(_element, "html")
            _head = ET.SubElement(_html, "head")
            _body = ET.SubElement(_html, "body")
            _p    = ET.SubElement(_body, "p")
            _p.text = strDetails
            # _element.text = \
                # '\n' + \
                # '<html>\n' + \
                # '  <head>\n' + \
                # '\n' + \
                # '  </head>\n' + \
                # '  <body>\n' + \
                # '    <p>\n' + \
                # '      ' + strDetails + '\n' + \
                # '    </p>\n' + \
                # '  </body>\n' + \
                # '</html>\n'

            # append element
            _node = self._node.append(_element)

        # return self.Details


    @property
    def Parent(self):

        # ensure existing parent
        if self._node in self._map._parentmap.keys():
            return Node(self._map._parentmap[self._node], self._map)
        else:
            return None


    @property
    def Next(self):

        # ensure existing parent
        _next = self._node.getnext()
        if _next is not None:
            return Node(_next, self._map)
        else:
            return None


    @property
    def Icons(self):
        _icons = []
        _lst = self._node.findall('icon')
        for _icon in _lst:
            _name = _icon.get('BUILTIN', '')
            if _name:
                _icons.append(_name)
        return _icons


    def addIcon(self,
                icon='',
                ):
        """
        This functions adds a Freeplane-Icon to a node
        """




        #
        # add icon to node
        #

        if icon:

            _icon = ET.Element('icon')
            _icon.attrib['BUILTIN'] = icon

            self._node.append(_icon)

        # return self.Icons


    def delIcon(self,
                icon='',
                ):
        """
        This functions removes a Freeplane-Icon from a node
        """




        #
        # search for icon
        #

        if icon:

            _icons = []
            _lst = self._node.findall('icon')
            for _icon in _lst:

                if _icon.get('BUILTIN', '').lower() == icon.lower():




                    #
                    # remove icon from node's icon list
                    #

                    self._node.remove(_icon)
                    break

        # return self.Icons


    @property
    def Children(self):
        lstNodes = []
        for item in  self._node.findall("./node"):
            lstNodes.append(Node(item, self._map))
        return lstNodes


    def getChildByIndex(self, idx=0):
        # check if node has children
        _children = self._node.findall("./node")
        if len(_children):
            # run through all child nodes
            for _i, _child in  enumerate(_children):
                # check for matching index
                if _i == idx:
                    return Node(_child, self._map)
                    break
            # index not found
            else:
                return None
        # no children present
        else:
            return None


    @property
    def isComment(self):
        if not self._node.get('STYLE_REF') is None \
                and self._node.attrib['STYLE_REF'] == 'klein und grau':
            return True
        return False


    @property
    def hasChildren(self):
        if not self._node.findall('./node'):
            return False
        return True


    def findNodes(self,
                 id='',
                 core='',
                 attrib='',
                 details='',
                 notes='',
                 link='',
                 icon='',
                 exact=False
                 ):




        #
        # find list of nodes below node
        #

        # list all nodes regardless of further properties
        lstNodes = self._node.findall(".//node")

        # do the checks on the base of the list
        lstNodes = reduce_node_list(
            lstNodes,
            id,
            core,
            attrib,
            details,
            notes,
            link,
            icon,
            exact
        )




        #
        # create Node instances
        #

        lstNodesRet = []
        for _node in lstNodes:
            lstNodesRet.append(Node(_node, self._map))

        return lstNodesRet


    def findChildren(self,
                 id='',
                 core='',
                 attrib='',
                 details='',
                 notes='',
                 link='',
                 icon='',
                 exact=False
                 ):




        #
        # find list of nodes directly below node
        #

        # list all nodes regardless of further properties
        lstNodes = self._node.findall("./node")

        # do the checks on the base of the list
        lstNodes = reduce_node_list(
            lstNodes,
            id,
            core,
            attrib,
            details,
            notes,
            link,
            icon,
            exact
        )




        #
        # create Node instances
        #

        lstNodesRet = []
        for _node in lstNodes:
            lstNodesRet.append(Node(_node, self._map))

        return lstNodesRet


    def getSubText(self, token=''):

        # initialize contents
        text = ""
        commentnode = None




        #
        # find node's INTERMEDIATE child node
        #

        # skip tokennode if token present
        if not token == "":

            # check for token node
            tokennode = self._node.findall("./node[@TEXT='" + token + "']")
            if not tokennode == []:

                # go further to find the comment text
                commentnode = tokennode[0].find('./node')

        else:

            # get first node node as comment node
            commentnode = self._node.find('./node')




        #
        # access text portion of target node
        #

        # if comment node exists
        if commentnode is not None:

            # get comment text
            text = getCoreTextFromNode(commentnode, bOnlyFirstLine=False)

        else:

            # text is invalid
            text = ""

        return text


    def addChild(self,
                 pos=-1,
                 core='',
                 style='',
                 ):
        """
        This functions adds a Freeplane-Node as a child to this Node. Further
        more a XML-node ist added to the XML-Tree
        """




        #
        # create and init element
        #

        _node = ET.Element('node')
        node = Node(_node, self._map)
        node.PlainText = core




        #
        # set node's position within children
        #

        if pos == -1:
            self._node.append(_node)
        else:
            self._node.insert(pos, _node)




        #
        # set style
        #

        #tmp.Style = style




        #
        # update parent dict
        #

        self._map._parentmap[_node] = self._node




        return node


    def addSibling(self,
                   pos=-1,
                   core="",
                   style=None,
                   ):
        """
        This functions adds a Freeplane-Node as a Sibling. Further more a
        XML-node ist added to the XML-Tree at the corresponding position
        """



        #
        # create and init element
        #

        _node = ET.Element('node')
        node = Node(_node, self._map)
        node.PlainText = core




        #
        # set node's position within siblings
        #

        if pos == -1:
            self._node.getparent().append(_node)
        else:
            self._node.getparent().insert(pos, _node)




        #
        # set style
        #

        #tmp.Style = style




        #
        # update parent dict
        #

        self._map._parentmap[_node] = self._node.getparent()




        return node


# VERSION-SPECIFICS

def get_version_specific_file_encoding(version):

    # file encoding was changed from "latin1" or "windows-1252"
    # to "utf-8" with Freeplane version 1.8.0

    lstVersionItems = version.split('.')
    if len(lstVersionItems)>=2:
        if int(lstVersionItems[0]) == 1 and int(lstVersionItems[1]) <= 6:
            # return "latin1"
            return "windows-1252"
        elif int(lstVersionItems[0]) == 1 and int(lstVersionItems[1]) > 6:
            return "utf-8"


# CONVENIENCE FUNCTIONS

def getCoreTextFromNode(node, bOnlyFirstLine=False):

    # initialize text content
    text = ""




    #
    # get TEXT attribute of node if present
    #

    if not node.get('TEXT') is None:

        # read out text content
        text = node.attrib['TEXT']




    #
    # strip text from RICHTEXT content if present
    #

    elif not node.find('richcontent') is None:

        # get richtext node
        richnode = node.find('richcontent')

        # get html node
        htmlnode = richnode.find('html')

        # get html body node
        htmltext = htmlnode.find('body')

        # filter out plain text content
        raw = "".join([x for x in htmltext.itertext()])




        #
        # filter first line if desired
        #

        if bOnlyFirstLine:

            # take only first line of text content
            text = raw.strip().split('\n')[0].strip()

        else:

            # replace <CR> and leading / trailing <SPACE>
            raw__no_CR = raw.replace('\n', '')
            text = raw__no_CR.strip()

    return text


def reduce_node_list(
        lstNodes=[],
        id='',
        core='',
        attrib='',
        details='',
        notes='',
        link='',
        icon='',
        exact=False
    ):

    # check for identical ID
    if id:
        _lstNodes = []
        for _node in lstNodes:
            if id.lower() == _node.attrib.get("ID", "").lower():
                _lstNodes.append(_node)
        lstNodes = _lstNodes

    # check for TEXT within a node's CORE
    if core:
        _lstNodes = []
        for _node in lstNodes:
            if exact:
                if core == _node.attrib.get("TEXT", ""):
                    _lstNodes.append(_node)
            else:
                if core.lower() in _node.attrib.get("TEXT", "").lower():
                    _lstNodes.append(_node)
        lstNodes = _lstNodes

    # check for BUILTIN ICON at node
    if icon:
        _lstNodes = []
        for _node in lstNodes:
            # check for icon node
            _lstIconNodes = _node.findall("./icon[@BUILTIN='" + icon + "']")
            if _lstIconNodes:
                _lstNodes.append(_node)
        lstNodes = _lstNodes

    # check for node's DETAILS
    if details:
        _lstNodes = []
        for _node in lstNodes:
            # check for details node
            _lstDetailsNodes = _node.findall("./richcontent[@TYPE='DETAILS']")
            if _lstDetailsNodes:
                _text = ''.join(_lstDetailsNodes[0].itertext())
                if exact:
                    if details in _text:
                        _lstNodes.append(_node)
                else:
                    if details.lower() in _text.lower():
                        _lstNodes.append(_node)
        lstNodes = _lstNodes

    # and back
    return lstNodes


# OLD

# read text paragraph from mindmap
# CLI FUNCTIONS

def getText(self, strRootAttribute, strTitleText, strPortion):

    # get list of all attributes
    lstAttributes = self._mindmap.getElementsByTagName('attribute')

    # search for ROOT ATTRIBUTE NODE
    for item in lstAttributes:
        if item.attributes['NAME'].value == 'type' and \
                item.attributes['VALUE'].value == strRootAttribute:
            rootnode = item.parentNode

    # get list of all nodes below
    lstNodes = rootnode.getElementsByTagName('node')

    # look for node containing TITLE STRING
    for item in lstNodes:
        if item.hasAttribute('TEXT'):
            if item.getAttribute('TEXT') == strTitleText:
                titlenode = item

    # get list of all nodes below
    lstNodes = titlenode.getElementsByTagName('node')

    # look for node containing PORTION STRING
    for item in lstNodes:
        if item.hasAttribute('TEXT'):
            if item.getAttribute('TEXT') == strPortion:
                portionnode = item

    # if there is no richtext content ...
    if not portionnode.getElementsByTagName('richcontent'):

        # get next following single node
        textnode = portionnode.getElementsByTagName('node')[0]

        # get standard TEXT attribute
        strText = textnode.getAttribute('TEXT')

    else:

        # look for HTML content
        richcontents = portionnode.getElementsByTagName('richcontent')

        # convert content to HTML
        strHtml = richcontents[0].toxml()

        # convert HTML to MARKDOWN ASCII
        strText = html2text.html2text(strHtml)

    # replace cryptic text passages
    strText = strText.replace('&lt;', '<')
    strText = strText.replace('&gt;', '>')

    # return value back to caller
    return strText


#
# execute this module code
#

if __name__ == "__main__":

    # create execute class init with command line environment
    Mindmap(id='cli')

