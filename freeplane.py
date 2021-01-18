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

    # number of available map objects this session
    _num_of_maps = 0

    # global node id per session and incremented
    # each time a node is created will be used to
    # increment a session date. this gives 10000
    # possible new nodes before the id string is
    # added another digit (initially 10 digits).
    _global_node_id_incr = 0
    _global_node_id_seed = datetime.datetime.now().strftime('%y%m%d')


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

        # when a file name was given as CLI argument, it will be checked if an
        # appropriate file is present. if so, the mindmap will be loaded into
        # memory.

        # check for validity of file
        if os.path.isfile(self._path):




            #
            # determine file's map version
            #

            # before load of the actual mindmap into memory, the file version
            # is to be determined. this is due to the fact that the character
            # encoding of older freeplane files was not stable. so, detecting
            # the encoding before load prevents some errors.

            # open mindmap file and read it
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

            # now use the freeplane file version to determine the encoding.

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

        # if there was no path given or the path does not correspond to a valid
        # file, a mindmap structure is created within memory. the basis is a
        # XML structure containing a lot of standard settings identified within
        # the normal freeplane files.

        # set version
        self._version = version

        # init parentmap dictionary in order to facilitate quick identification
        # of parent nodes of valid node objects (using ElementTree nodes as
        # keys and values)
        self._parentmap = {}

        # create map element as XML node containing the version information
        self._mindmap = ET.Element('map') 
        self._mindmap.attrib['version'] = 'freeplane ' + self._version

        # get root of mindmap (necessary for save operation)
        self._root = self._mindmap

        # set some attributes for visibility within freeplane editor
        _node = ET.Element('attribute_registry') 
        _node.attrib['SHOW_ATTRIBUTES'] = 'hide'
        self._mindmap.append(_node)

        # create 1st visible node element containing standard TEXT
        self._rootnode = ET.Element('node') 
        self._rootnode.attrib["TEXT"] = "new_mindmap"
        self._rootnode.attrib["FOLDED"] = "false"
        self._rootnode.attrib["ID"] = Mindmap.get_new_node_id()
        self._mindmap.append(self._rootnode)

        # create some standard edge styles
        _node = ET.Element('edge') 
        _node.attrib['STYLE'] = 'horizontal'
        _node.attrib['COLOR'] = '#cccccc'
        self._rootnode.append(_node)

        #
        # hook element and properties
        #

        _hook = ET.Element('hook') 
        _hook.attrib["NAME"] = "MapStyle"
        _hook.attrib["zoom"] = "1.00"
        self._rootnode.append(_hook)
        # sub element properties
        _node = ET.Element('properties')
        _node.attrib["show_icon_for_attributes"] = "false"
        _node.attrib["show_note_icons"] = "false"
        _hook.append(_node)

        #
        # map styles
        #

        # sub element map styles
        _mapstyles = ET.Element('map_styles')
        _hook.append(_mapstyles)
        # sub sub element stylenode
        _stylenode = ET.Element('stylenode')
        _stylenode.attrib["LOCALIZED_TEXT"] = "styles.root_node"
        _mapstyles.append(_stylenode)

        #
        # predefined styles
        #

        # sub sub sub element stylenode
        _node = ET.Element('stylenode')
        _node.attrib["LOCALIZED_TEXT"] = "styles.predefined"
        _node.attrib["POSITION"] = "right"
        _stylenode.append(_node)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "default"
        _node2.attrib["MAX_WIDTH"] = "600"
        _node2.attrib["COLOR"] = "#000000"
        _node2.attrib["STYLE"] = "as_parent"
        _node.append(_node2)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('font')
        _node3.attrib["NAME"] = "Segoe UI"
        _node3.attrib["SIZE"] = "12"
        _node3.attrib["BOLD"] = "false"
        _node3.attrib["ITALIC"] = "false"
        _node2.append(_node3)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "defaultstyle.details"
        _node.append(_node2)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "defaultstyle.note"
        _node.append(_node2)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "defaultstyle.floating"
        _node.append(_node2)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('edge')
        _node3.attrib["STYLE"] = "hide edge"
        _node2.append(_node3)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('cloud')
        _node3.attrib["COLOR"] = "#0f0f0f"
        _node3.attrib["SHAPE"] = "ROUND_RECT"
        _node2.append(_node3)

        #
        # user styles
        #

        # sub sub sub element stylenode
        _node = ET.Element('stylenode')
        _node.attrib["LOCALIZED_TEXT"] = "styles.user-defined"
        _node.attrib["POSITION"] = "right"
        _stylenode.append(_node)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "styles.topic"
        _node2.attrib["COLOR"] = "#18898b"
        _node2.attrib["STYLE"] = "fork"
        _node.append(_node2)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('font')
        _node3.attrib["NAME"] = "Liberation Sans"
        _node3.attrib["SIZE"] = "12"
        _node3.attrib["BOLD"] = "true"
        _node2.append(_node3)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "styles.subtopic"
        _node2.attrib["COLOR"] = "#cc3300"
        _node2.attrib["STYLE"] = "fork"
        _node.append(_node2)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('font')
        _node3.attrib["NAME"] = "Liberation Sans"
        _node3.attrib["SIZE"] = "12"
        _node3.attrib["BOLD"] = "true"
        _node2.append(_node3)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "styles.subsubtopic"
        _node2.attrib["COLOR"] = "#669900"
        _node.append(_node2)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('font')
        _node3.attrib["NAME"] = "Liberation Sans"
        _node3.attrib["SIZE"] = "12"
        _node3.attrib["BOLD"] = "true"
        _node2.append(_node3)
        # sub sub sub element stylenode
        _node2 = ET.Element('stylenode')
        _node2.attrib["LOCALIZED_TEXT"] = "styles.important"
        _node.append(_node2)
        # sub sub sub sub element stylenode
        _node3 = ET.Element('icon')
        _node3.attrib["BUILTIN"] = "yes"
        _node2.append(_node3)

# MAP

    @classmethod
    def getNumOfMaps(cls):
        return cls._num_of_maps

    @classmethod
    def get_new_node_id(cls):

        # create a valid node id. this node id is incremented automatically,
        # whenever a new XML node is created. even if it is discarded later.
        # the node id, here consists of three parts: the id tiken "ID_" which
        # is used for all nodes directly created within freeplane editor, a
        # kind of session seed which is the current date, and a standard
        # 4-digit integer value incremented as already said.

        # increment future part of node id
        cls._global_node_id_incr += 1

        # return current node id
        return 'ID_' + \
                cls._global_node_id_seed + \
                '{:04}'.format(cls._global_node_id_incr)

    @classmethod
    def createNode(cls,
            core='',
            link='',
            id='',
            style=''
            ):

        #
        # create and init element
        #

        # core
        _node = ET.Element('node')
        node = Node(_node, None)
        node.PlainText = core

        # create temporary branch with local (empty) parent_map reference
        # node._parentmap = {}
        node._branch = Branch()

        # check own id choice
        if id:
            node.Id = id
            if not node.Id == id:
                # print("[ WARNING: node id must follow Freplane's format rules. nothing done. ]")
                return None

        # link
        if link:
            node.Link = link

        # style
        if style:
            print("[ WARNING: style attribute not implemented, yet ]")

        return node


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
            core='',
            link='',
            id='',
            attrib='',
            details='',
            notes='',
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
            lstNodes=lstNodes,
            id=id,
            core=core,
            attrib=attrib,
            details=details,
            notes=notes,
            link=link,
            icon=icon,
            exact=exact,
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

        # strExamplePath = "example__code2mm__v1_8_11.mm"
        # strExamplePath = "example__code2mm__v1_3_15.mm"
        # mm = Mindmap(strExamplePath)
        # dicStyles = mm.Styles
        # print(dicStyles)
        # mm.save(strExamplePath[:strExamplePath.rfind('.')] + '__saved.mm')




        # create new mindmap
        mm=Mindmap()

        # get and print root node
        rn=mm.RootNode
        print(rn)

        # change root node plain text
        rn.PlainText = "ROOT NODE"
        print(rn)




        #
        # create some nodes and branches
        #

        # create detached node
        detach=mm.createNode("DETACHED")
        print(detach)

        # create detached node
        detach2=mm.createNode("DETACHED2")
        print(detach2)

        # add node into 2nd detached branch
        nd2=detach2.addChild("ADDED_TO_DETACHED2_AS_CHILD")
        print(nd2)

        # create detached node
        detach3=mm.createNode("DETACHED3")
        print(detach3)

        # add node into 2nd detached branch
        nd3=detach3.addChild("ADDED_TO_DETACHED3_AS_CHILD")
        print(nd3)

        # check parent node within branch
        print(nd2.Parent)

        #
        # create and attach some styles
        #

        # add style to mindmap
        mm.addStyle(
                "klein und grau",
                {
                    'color': '#999999',
                })

        # WARNING: apply non-existing style to detached branch node
        nd2.Style = "groß und grau"

        #
        # attach some nodes and styles
        #

        # attach detached3 branch head to detached node nd2
        nd2.attach(detach3)

        # WARNING: attach detached branch node to root node
        rn.attach(nd2)

        # attach single detached head to root node
        rn.attach(detach)

        # WARNING: apply existing style to detached branch node
        detach2.Style = "klein und grau"

        # attach detached branch head to root node
        rn.attach(detach2)

        # apply existing style to map node
        nd2.Style = "klein und grau"

        # WARNING: attach already attached branch head
        rn.attach(detach)

        # WARNING: attach already attached branch head to already attached former branch node
        nd2.attach(detach)

        #
        # save mindmap into file
        #

        mm.save("example101.mm")




# BRANCH

class Branch(object):

    def __init__(self):

        #
        # initialize instance
        #

        self._parentmap = {}
        self._map = None




# NODE

class Node(object):

    def __init__(self, node, map):

        #
        # initialize instance
        #

        self._map = map
        self._node = node

        #
        # create unique session node id
        #

        self._node.set('ID',
                Mindmap.get_new_node_id()
                )

    def __str__(self):
        return self.PlainText


    @property
    def is_detached_head(self):
        """
        check if node is the head node of a detached branch.
        """
        # is not associated with a map
        # and has no parent within the branch
        if self._map is None \
                and not self._node in self._branch._parentmap.keys():
            return True
        return False

    @property
    def is_detached_node(self):
        """
        check if node is belonging to a detached branch.
        """
        # is not associated with a map
        # and has a parent within the branch
        if self._map is None \
                and self._node in self._branch._parentmap.keys():
            return True
        return False

    @property
    def is_map_node(self):
        """
        check if node is belonging to a map, but not being the root node.
        """
        # is associated with a map
        if self._map is not None \
                and not self._node == self._map._rootnode:
            return True
        return False

    @property
    def is_root_node(self):
        """
        check if node is the map's root node.
        """
        # is associated with a map
        if self._map is not None \
                and self._node == self._map._rootnode:
            return True
        return False


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

    @Id.setter
    def Id(self, strId):

        # check required format
        if strId.lower().startswith('id_') \
                and strId[len('id_'):].isnumeric():
            # set new ID
            self._node.attrib["ID"] = strId
        else:
            print('[ WARNING: in Freeplane, an ID must start with "ID_" and contain a number string. ignoring ID change request.')
            return False

        return True

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

    @Style.setter
    def Style(self, strStyle):

        #
        # find reference to mindmap
        #

        # when calling this method from a detached node, the _map reference is
        # missing. so, for detached nodes, the check of validity for a
        # particularly requested style name is not possible as it is the
        # mindmap itself that holds them. when a former detached node has been
        # attached to a proper mindmap tree, there might still be an invalid
        # _map reference for its branch trees as they are not updated
        # automatically. in these cases, the _map member can be updated, here,
        # for the user to have a corrected object reference. 

        # check if node seems detached
        if self._map is None:
 
            # check if node is still detached
            if self._branch._map is None:

                print("[ WARNING: trying to set a style for a detached node. make sure, style exists. ]")

            else:

                # 
                # update reference to mindmap
                #

                # update node's map reference
                self._map = self._branch._map




        #
        # set style reference
        #

        # check when map exists
        if self._map is not None:

            # check with existing styles
            for _stylename in self._map.Styles.keys():
                if _stylename.lower() == strStyle.lower():
                    break
            else:
                print('[ WARNING: style "' + strStyle + '" not found in mindmap. make sure, style exists. ]')

        # set style reference in XML node
        self._node.attrib["STYLE_REF"] = strStyle

        return True


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

        # if non-detached node
        if self.is_map_node:
            # ensure existing parent
            if self._node in self._map._parentmap.keys():
                return Node(self._map._parentmap[self._node], self._map)
            else:
                return None

        # if detached node
        elif self.is_detached_node:
            # read from branch object
            return Node(self._branch._parentmap[self._node], self._map)

        # if detached branch head
        elif self.is_detached_head:
            print("[ WARNING: a detached branch head has no other parent. ]")
            return None

        else:
            print("[ ERROR  : local parentmap has not been created for detached node. ]")
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
                 core='',
                 link='',
                 id='',
                 attrib='',
                 details='',
                 notes='',
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
            lstNodes=lstNodes,
            id=id,
            core=core,
            attrib=attrib,
            details=details,
            notes=notes,
            link=link,
            icon=icon,
            exact=exact,
        )




        #
        # create Node instances
        #

        lstNodesRet = []
        for _node in lstNodes:
            lstNodesRet.append(Node(_node, self._map))

        return lstNodesRet


    def findChildren(self,
                 core='',
                 link='',
                 id='',
                 attrib='',
                 details='',
                 notes='',
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
            lstNodes=lstNodes,
            id=id,
            core=core,
            attrib=attrib,
            details=details,
            notes=notes,
            link=link,
            icon=icon,
            exact=exact,
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


    def attachAsChild(self,
            attached_node=None,
            pos=-1,
            ):
        """
        This functions appends an existing but previously detached
        Freeplane-Node as a child to this node object.
        """




        #
        # check if attached node is valid
        #

        if attached_node is None:
            print("[ WARNING: no attached_node given to be attached. ]")
            return False




        #
        # check if to-be-attached-node is already attached
        #

        # in case, the node-to-be-attached is already part of the target
        # branch, this activity is to be aborted as it would lead to confusion
        # of the XML structure and the user's references.

        # check if object is child within map
        if self.is_map_node or self.is_root_node:
            if attached_node._node in self._map._parentmap.keys():
                print("[ WARNING: node already attached to a map. ]")
                return False
        elif attached_node.is_detached_node:
            print("[ WARNING: node attached to a branch. please only attach branch head. ]")
            return False




        #
        # DIFFERENT CASES
        #

        # in order to leave the nodes in a consistent status, there are
        # different cases to be evaluated. as there are different kind of nodes
        # and the necessary operations differ depending on the node types
        # involved during attachment, there must be a kind of
        # "Fallunterscheidung".




        #
        # handle attach of detached head to map node
        #

        if (self.is_map_node or self.is_root_node) and attached_node.is_detached_head:

            #
            # update old branch head's _map member
            #

            # the pointer to the map object of the attached node
            # is to be the same as the map object attached to
            attached_node._map = self._map

            #
            # set parent node within map's parentmap
            #

            self._map._parentmap[attached_node._node] = self._node

            #
            # append map's parent dict from branch's dict
            #

            self._map._parentmap.update(attached_node._branch._parentmap)

            #
            # save new map reference in old branch object
            #

            # store the new map reference within the old branch object
            # for later reference when one of the former branch nodes is
            # to be checked. thus, the _map member can be corrected.
            attached_node._branch._map = self._map

            #
            # insert appropriate XML nodes
            #

            if pos == -1:
                self._node.append(attached_node._node)
            else:
                self._node.insert(pos, attached_node._node)

            # leave function
            # return attached_node
            return True




        #
        # handle attach of detached head to detached branch
        #

        if (self.is_detached_node or self.is_detached_head) and attached_node.is_detached_head:

            #
            # update old branch head's _branch member
            #

            # the pointer to the map object of the attached node
            # is to be the same as the map object attached to
            attached_node._branch = self._branch

            #
            # set parent node within new branch's parentmap
            #

            self._branch._parentmap[attached_node._node] = self._node

            #
            # append new branch's parent dict from branch's dict
            #

            self._branch._parentmap.update(attached_node._branch._parentmap)

            #
            # insert appropriate XML nodes
            #

            if pos == -1:
                self._node.append(attached_node._node)
            else:
                self._node.insert(pos, attached_node._node)

            # leave function
            return True




        #
        # handle attach of detached head to detached branch
        #

        if attached_node.is_detached_node:
            print('[ WARNING: attach of "' \
                    + str(attached_node) \
                    + '" not possible. generally, only the heads of detached branches attachable.]')
            return False




        print('[ ERROR  : host / child configuration for attach is not defined. ]')
        return False


    def addChild(self,
                 core='',
                 link='',
                 id='',
                 pos=-1,
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




        # overwrite standard id
        if id:
            node.Id = id
            if not node.Id == id:
                return None




        #
        # set link portion
        #

        if link:
            node.Link = link




        #
        # set style
        #

        #tmp.Style = style




        #
        # set node's position within children
        #

        if pos == -1:
            self._node.append(_node)
        else:
            self._node.insert(pos, _node)




        #
        # update parentmap dict
        #

        # check if this node is attached to a map
        if self._map is not None:

            # add this object as parent to new object
            self._map._parentmap[_node] = self._node

        else:

            # create _branch and _parentmap nodes in new child
            node._branch = self._branch

            # add this object as parent to new object within detached branch
            self._branch._parentmap[_node] = self._node




        return node


    def addSibling(self,
                   core="",
                   link="",
                   id='',
                   pos=-1,
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




        # overwrite standard id
        if id:
            node.Id = id
            if not node.Id == id:
                # print("[ WARNING: node id must follow Freplane's format rules. nothing done. ]")
                return None




        #
        # set link portion
        #

        if link:
            node.Link = link




        #
        # set style
        #

        #tmp.Style = style




        #
        # set node's position within siblings
        #

        if pos == -1:
            self._node.getparent().append(_node)
        else:
            self._node.getparent().insert(pos, _node)




        #
        # update parentmap dict
        #

        # check if this node is attached to a map
        if self._map is not None:

            # add this object as parent to new object
            self._map._parentmap[_node] = self._node.getparent()

        # check if this node is attached to a branch
        elif self._node in self._branch._parentmap.keys():
            self._branch._parentmap[_node] = self._node.getparent()

        else:

            # output warning
            print("[ WARNING: it is not possible to add a sibling to a detached node. please use the createNode function. ]")
            return None




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
        exact=False,
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

