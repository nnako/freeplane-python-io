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
import os
import re
import sys
import io

# xml format
#import xml.etree.ElementTree as ET
import lxml.etree as ET


# MINDMAP

class Mindmap(object):

    """
    Freeplane interfacing class

    Access Freeplane mindmap file and do various search, read and write
    operations to retrieve or modify text passages within the mindmap.

    """

    _num_of_maps = 0

    def __init__(self, path='', type='freeplane', version='1.3', id=''):




        #
        # define main command line arguments
        #

        # do this only if called from the command line
        if id == 'cli':

            # define information
            parser = argparse.ArgumentParser(
                    description='Operation on Freeplane mindmap',
                    usage='''%s <command> [<args>]

                    Possible commands are:
                        getText    return text portion of a node
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
        # access class variables
        #

        Mindmap._num_of_maps += 1




        #
        # access instance variables
        #

        # path of instance's mindmap file
        self._path = path

        # type, version
        self._type = type
        self._version = version




        #
        # read mindmap
        #

        # set encoding to be read
        xmlparser = ET.XMLParser(encoding='latin1')

        # read entire etree plan
        self._mindmap = ET.parse(self._path, parser=xmlparser)

        # get root of mindmap
        self._root = self._mindmap.getroot()

        # find and get first node element of etree
        self._rootnode = self._root.find('node')

        # build parent map (using ElementTree nodes)
        self._parentmap = {c:p for p in self._rootnode.iter() for c in p}


# MAP

    @classmethod
    def getNumOfMaps(cls):
        return cls._num_of_maps


    @property
    def RootNode(self):
        return Node(self._rootnode)


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


    def save(self, strPath, encoding='latin1'):

        # open output file
        _file = io.open(strPath, "w", encoding=encoding)

        # create output string
        # and remove first output row
        # as Freeplane doesn't use strict XML
        _outputstring = ET.tostring(
            self._root,
            pretty_print=True,
            encoding=encoding).decode(encoding).split('\n', 1)[1]

        # write output string
        _file.write( _outputstring )

        # close file
        _file.close()


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


    @property
    def Style(self):
        if 'STYLE_REF' in self._node.attrib.keys():
            return self._node.attrib['STYLE_REF']
        return ""


    @property
    def CoreLink(self):

        # check for TEXT attribute
        if not self._node.get('TEXT') is None:

            # read out text content
            text = self._node.attrib['TEXT']

            if len(text) > 0 \
                    and text[0] == "=":




                #
                # check for reference to external node
                #

                # identify link based on type (file, http, ...)




                #
                # check for reference to internal node
                #

                _match=re.match(r'^.*ID_([\d]+)\.text.*', text)
                # valid match found?
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
            _text = ''.join(_lstDetailsNodes[0].itertext())
            _text = _text.replace('\n\n', '[xox]')
            _text = _text.replace('\n', '')
            _text = _text.replace('[xox]', '\n')

        return _text


    @Details.setter
    def Details(self, strDetails):

        # check for existing details
        _lstDetailsNodes = self._node.findall("./richcontent[@TYPE='DETAILS']")
        if _lstDetailsNodes:
            _lstDetailsNodes[0].text = strDetails
        else:
            _node = self._node.append('richcontent')
            _node.attrib["TYPE"] = 'DETAILS'
            _node.text = strDetails


    @property
    def Parent(self):
        return Node(self._map._parentmap[self._node], self._map)


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


    @property
    def Children(self):
        lstNodes = []
        for item in  self._node.findall("./node"):
            lstNodes.append(Node(item, self._map))
        return lstNodes


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


# FUNCTIONS

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

    # execute class init with command line environment
    Mindmap(id='cli')
