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
# internally, the following object model is used, where the symbols follow this
# definition:
#
#   M   Mindmap object        - holding general map information
#   R   root Node object      - the first user-accessible Node within a mindmap
#   N   Node object           - any Node attached to a mindmap
#   B   Branch object         - a separate information structure organizing detached elements
#   DH  Detached Head object  - the head of a detached branch
#   DN  Detached Node object  - any branch node below a detached head
#   XMLNODE object            - an lxml node element representing a real node in Freeplane 
#
#
#  _path
#  _type          .---------------------------- .  _map                .-----------.
#  _version       |                             .  _node ------------->| XMLNODE   |
#  _mindmap       |                             .  _branch ---|        '-----------'
#  _root          |                                                          ^
#  _parentmap     |                                |                         |
#                 v                                |                         |
#  |            .---.  .----.   .----. .----. .--------.                     |
#  '----------- | M |  | R  +-+-+ N  +-+ N  +-+ N      +- ...                |
#               '---'  '----' | '----' '----' '--------'                     |
#                 ^           |                                              |
#                 |           | .----. .----.                                |
#                 |           '-+ N  +-+ N  +- ...                           |
#                 |             '----' '----'               |--- .  _map     |
#                 |                                              .  _node ---'
#                 |  .------------------------------------------ .  _branch
#     _map -------'  |
#     _parentmap     |                                              |
#                    v                                              |
#     |            .---.  .----.   .----. .----. .----. .----. .-------.
#     '----------- | B |  | DH +-+-+ DN +-+ DN +-+ DN +-+ DN +-+ DN    +- ...
#                  '---'  '----' | '----' '----' '----' '----' '-------'
#                                |
#                                | .----. .----.
#                                '-+ DN +-+ DN +- ...
#                                  '----' '----'
#
#
# AUTHOR
#
#   - nnako, started in 2016
#


# generals
from __future__ import print_function
import argparse
import datetime
import os
import re
import sys
import io
import logging

# xml format
try:
    import lxml.etree as ET
except:
    print("at this point, lxml package is not available. shouldn't be a problem, though.")

# html format
try:
    import html2text
except:
    print("at this point, html2text package is not available. shouldn't be a problem, though.")


# version
__version__         = '0.8.0'

# BUILTIN ICONS
ICON_EXCLAMATION    = 'yes'
ICON_LIST           = 'list'
ICON_QUESTION       = 'help'
ICON_CHECKED        = 'button_ok'
ICON_BOOKMARK       = 'bookmark'
ICON_PRIO1          = 'full-1'
ICON_PRIO2          = 'full-2'


# logging
logging.basicConfig(
        format='%(name)s - %(levelname)-8s - %(message)s',
        level=logging.WARNING,
        )


# MINDMAP

class Mindmap(object):

    """
    representation of Freeplane mindmap file as a container for nodes. access
    styles and other general features from here.

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


    def __init__(
            self,
            path='',
            mtype='freeplane',
            version='1.3.0',
            id='',
            log_level="warning",
            logger=None,
            ):




        #
        # adjust logging level to user's wishes
        #

        # if logger has not been provided via API
        if logger is None:

            # create logger and set level according to API
            if log_level.lower() == "debug":
                logging.getLogger().setLevel(logging.DEBUG)
            elif log_level.lower() == "info":
                logging.getLogger().setLevel(logging.INFO)
            elif log_level.lower() == "warning":
                logging.getLogger().setLevel(logging.WARNING)
            elif log_level.lower() == "error":
                logging.getLogger().setLevel(logging.ERROR)
            else:
                logging.getLogger().setLevel(logging.WARNING)
                logging.warning("log level mismatch in user arguments. setting to WARNING.")

            # create a usable logger if it was not provided by the function
            self._logger = logging.getLogger(__name__)

        # else, logger object was given
        else:
            self._logger = logger





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

                self._logger.error('Unrecognized command. EXITING.')
                parser.print_help()
                sys.exit(1)

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
            # the encoding before load prevents some encoding errors.

            # open mindmap file and read first row
            retry = False
            try:
                with io.open(self._path, "r", encoding="utf-8") as fpMap:
                    strFirstLine = fpMap.readline()
            except:
                self._logger.info("format mismatch in mindmap file vs. UTF-8. TRYING WORKAROUND.")
                retry = True

            # in case there are wrong encodings when trying to read as UTF-8,
            # it is tried to use Window's native encoding scheme to read the
            # file. this will be most likely the case and might be a good
            # workaround

            if retry:
                try:
                    with io.open(self._path, "r", encoding="windows-1252") as fpMap:
                        strFirstLine = fpMap.readline()
                    self._logger.info("format mismatch could be worked around, successfully")
                except:
                    self._logger.warning("format mismatch in mindmap file vs. windows-1252. FURTHER PROBLEMS WILL FOLLOW.")

            # now, analyze the characters in the first line of the mindmap file
            # and try to find the "freeplane" token which will contain the
            # version information.

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

            # some Freeplane versions produce invalid XML syntax when writing
            # the mindmap into file. here, these invalid syntaxes are to be
            # removed from the file, before using and parsing the file.

            try:
                self._mindmap = ET.parse(self._path, parser=xmlparser)

            except ET.XMLSyntaxError:
                self._logger.warning("invalid XML syntax. will try to fix it temporarily...")

                # write sanitized file into temporary file
                _basename = "_" + os.path.basename(self._path)
                _dirname  = os.path.dirname(self._path)

                # ensure temp file is not yet present
                while os.path.isfile(os.path.join(_dirname, _basename)):
                    _basename = "_" + _basename
                _temp_file = os.path.join(_dirname, _basename)

                # read original XML file
                with io.open(self._path, "r", encoding="utf-8") as _file:
                    _content = _file.read()

                # sanitize content
                _content = _content.replace("&nbsp;", "&#160;")

                # create and write temp file
                with io.open(_temp_file, "w", encoding="utf-8") as _file:
                    _file.write(_content)

                # repeat open of mindmap
                self._mindmap = ET.parse(_temp_file, parser=xmlparser)

                # remove temporary file
                os.remove(_temp_file)

                self._logger.info("... XML source was successfully sanitized.")

            # now that the XML file has been read in in a valid way, the normal
            # XML parsing is to take place within the module's functionalities.

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
        self._rootnode.attrib["ID"] = Mindmap.create_node_id()
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
    def get_num_of_maps(cls):
        """
        return the number of maps already created within the current session

        :returns: integer
        """

        return cls._num_of_maps

    @classmethod
    def create_node_id(cls, mindmap=None):
        """
        create a valid node id. this node id is incremented automatically,
        whenever a new XML node is created. even if it is discarded later.
        the node id, here consists of three parts:

            1. the id token "ID_" which is used for all nodes directly created
               within freeplane editor
        
            2. and kind of session seed which is the current date
        
            3. and a standard 4-digit integer value constantly incremented
        """

        # increment future part of node id
        cls._global_node_id_incr += 1

        # set the node id
        _id = 'ID_' + \
                cls._global_node_id_seed + \
                '{:04}'.format(cls._global_node_id_incr)




        #
        # resolve overlapping ids
        #

        # check if the originally intended node id is already present within
        # the mindmap. if it is, increment the node id counter, generate the
        # node id again and check again. do this until a node id was found
        # which does not yet exist within the mindmap.

        # only if valid mindmap pointer was given
        if mindmap is not None:

            bLeave = False
            while not bLeave:

                # check for calculated id already used
                lstOfNodesMatchingId = mindmap._root.xpath("//node[@ID='" + _id + "']")
                if len(lstOfNodesMatchingId):

                    # increment global node id counter
                    cls._global_node_id_incr += 1

                    # set the node id string
                    _id = 'ID_' + \
                            cls._global_node_id_seed + \
                            '{:04}'.format(cls._global_node_id_incr)

                else:
                    bLeave = True




        # return new node id
        return _id

    @classmethod
    def create_node(cls,
            core='',
            link='',
            id='',
            style='',
            modified='',  # timestamp format, milliseconds since 1.1.1970
            created='',   # timestamp format, milliseconds since 1.1.1970
            ):

        #
        # create and init element
        #

        # core
        _node = ET.Element('node')
        node = Node(_node, None)
        node.plaintext = core




        #
        # set current creation and modification dates
        #

        update_date_attribute_in_node(
                node=_node,
                key="MODIFIED",
                )

        update_date_attribute_in_node(
                node=_node,
                key="CREATED",
                )




        # create temporary branch with local (empty) parent_map reference
        node._branch = Branch()

        # check own id choice
        if id:
            node.id = id
            if not node.id == id:
                # print("[ WARNING: node id must follow Freplane's format rules. nothing done. ]")
                return None

        # link
        if link:
            node.hyperlink = link

        # style
        if style:
            self._logger.warning("style attribute not implemented, yet")

        return node


    @property
    def rootnode(self):
        return Node(self._rootnode, self)


    @property
    def styles(self):
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


    def add_style(self,
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
                    print('[ WARNING: style "' + name + '" is already existing. ignoring request. ]')
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
                _item = _sty.find('./font')
                if _item is None:
                    # create new font element
                    _item = ET.Element('font', SIZE=settings[_check])
                    _sty.append(_item)
                else:
                    # add size attribute to font element
                    _item.set("SIZE", settings[_check])

            return True

        return False


    def find_nodes(
            self,
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
        lstXmlNodes = self._root.findall(".//node")

        # do the checks on the base of the list
        lstXmlNodes = reduce_node_list(
            lstXmlNodes=lstXmlNodes,
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
        for _node in lstXmlNodes:

            # create reference to parent lxml node
            #...

            # apend to list
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

            # at least substitute encoded german special characters
            # with characters fitting to the UTF-8 HTML encoding

            _outputstring = _outputstring.replace( 'ä','&#xe4;') # &#228
            _outputstring = _outputstring.replace( 'ö','&#xf6;') # &#246
            _outputstring = _outputstring.replace( 'ü','&#xfc;') # &#252
            _outputstring = _outputstring.replace( 'Ä','&#xc4;')
            _outputstring = _outputstring.replace( 'Ö','&#xd6;')
            _outputstring = _outputstring.replace( 'Ü','&#xdc;')
            _outputstring = _outputstring.replace( 'ß','&#xdf;')

            # by copy/paste from other applications into the mindmap, there
            # might be further character sequences not wanted within this file

            # alternative double quotes
            # _outputstring = _outputstring.replace( '&#x201c;','&quot;')
            # _outputstring = _outputstring.replace( '&#x201e;','&quot;')

            # three subsequent dots (e.g. from EXCEL's auto chars)
            # _outputstring = _outputstring.replace( '&#x2026;','...')
            # _outputstring = _outputstring.replace( chr(0x2026);','...')
            # _outputstring = _outputstring.replace( chr(133),'...')




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
        rn=mm.rootnode
        print(rn)

        # change root node plain text
        rn.plaintext = "ROOT NODE"
        print(rn)




        #
        # create some nodes and branches
        #

        # create detached node
        detach=mm.create_node("DETACHED")
        print(detach)

        # create detached node
        detach2=mm.create_node("DETACHED2")
        print(detach2)

        # add node into 2nd detached branch
        nd2=detach2.add_child("ADDED_TO_DETACHED2_AS_CHILD")
        print(nd2)

        # create detached node
        detach3=mm.create_node("DETACHED3")
        print(detach3)

        # add node into 2nd detached branch
        nd3=detach3.add_child("ADDED_TO_DETACHED3_AS_CHILD")
        print(nd3)

        # check parent node within branch
        print(nd2.parent)

        #
        # create and attach some styles
        #

        # add style to mindmap
        mm.add_style(
                "klein und grau",
                {
                    'color': '#999999',
                })

        # WARNING: apply non-existing style to detached branch node
        nd2.style = "groß und grau"

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
        detach2.style = "klein und grau"

        # attach detached branch head to root node
        rn.attach(detach2)

        # apply existing style to map node
        nd2.style = "klein und grau"

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




# ARROW STYLES

# currently, Freeplane stores arrow link foot points as xmlnodes directly below
# a content node. unlike the user-defined node styles which are stored
# centrally at a top position of the map, there is no built-in way to manage
# "named" arrow link definitions e.g. in order to re-use them. thus, here we
# define a structure to externally provide named arrow link styles. these can
# be set an retrieved when creating arrow links.

class ArrowStyles(object):

    def __init__(self):

        self._styles = {}

    @property
    def styles(self):
        return self._styles

    def add_style(self,
            name='',
            settings={},
            ):
        self._styles.update({
            name: settings
            })
        return True


# NODE

class Node(object):
    """
    representation of Freeplane node elements found within a mindmap. all the
    node-related features can be accessed from here.
    """

    def __init__(self, node, mindmap):




        #
        # initialize instance
        #

        self._map = mindmap
        self._node = node
        self._branch = None




        #
        # create unique session node id
        #

        if not node.get('ID', ''):
            self._node.set('ID',
                Mindmap.create_node_id(self._map)
                )




        #
        # create date entries
        #

        if not node.get('CREATED', ''):
            update_date_attribute_in_node(node, key="CREATED")
        if not node.get('MODIFIED', ''):
            update_date_attribute_in_node(node, key="MODIFIED")


    def __repr__(self):
        return self.plaintext


    def __str__(self):
        return self.plaintext


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
    def plaintext(self):
        return getCoreTextFromNode(self._node, bOnlyFirstLine=False)


    @plaintext.setter
    def plaintext(self, strText, modified=''):

        # check if there is textual content to be set (other than None)
        if strText is None:
            return None

        # set plain text content
        self._node.attrib['TEXT'] = strText

        # remove node's richcontent if present
        _richcontentnode = self._node.find('richcontent')
        if _richcontentnode is not None:
            self._node.remove(_richcontentnode)




        #
        # set modification date
        #

        update_date_attribute_in_node(
                node=self._node,
                date=modified,
                key="MODIFIED",
                )



        return True


    @property
    def has_internal_hyperlink(self):
        _link = self._node.attrib.get("LINK","")
        if _link and _link[0] == "#":
            return True
        return False


    @property
    def follow_internal_hyperlink(self):

        # check for internal hyperlink
        if self.has_internal_hyperlink:

            # get target node id by removing leading hash char
            _referenced_node_id = self._node.attrib.get("LINK","")[1:]

            try:
                # find node
                _node = self._map.find_nodes(id=_referenced_node_id)[0]

                # create Node instance
                fpnode = Node(_node._node, self._map)

                # update branch reference in case of detached node
                if not self.is_root_node and not self.is_map_node:
                    fpnode._map     = None
                    fpnode._branch  = self._branch

                # return it to user
                return fpnode

            except:
                print(f'[ WARNING: the referenced node "{_referenced_node_id}" was not found in mindmap. please check. ]')
                return None


    @property
    def hyperlink(self):
        return self._node.attrib.get("LINK","")


    @hyperlink.setter
    def hyperlink(self, strLink, modified=''):
        self._node.attrib["LINK"] = strLink




        #
        # set creation and modification dates
        #

        update_date_attribute_in_node(
                node=self._node,
                date=modified,
                key="MODIFIED",
                )

        return True


    @property
    def imagepath(self):

        # check if node holds no in-line image
        if self._node.find('hook') is None:
            # print(f'[ WARNING: the node "{self.id}" does not contain an in-line image. ]')
            return None

        # get hook node
        hook = self._node.find('hook')

        # get uri attribute
        uri = hook.attrib.get("URI", "")

        # sanitize uri
        uri = uri.replace("file://", "")

        # somehow, freeplane currently stores paths in the image hook with
        # THREE slashes after the protocol token "file". for Linux, this makes
        # sense when dealing with absolute file paths (all starting with
        # another "/"). but for Windows this doesn't make sense as there
        # remains an additional "/" in front of the drive specification "C:" of
        # absolute path definitions. this is to be corrected, here, as long it
        # is not corrected within Freeplane.

        # check for leading slash in front of drive token
        _match = re.search(r'^(/[A-z]:/)', uri)
        if _match:
            # remove leading slash
            uri = uri[1:]

        return uri

    @property
    def imagesize(self):

        # check if node holds no in-line image
        if self._node.find('hook') is None:
            print(f'[ WARNING: the node "{self._node.id}" does not contain an in-line image. ]')
            return None

        # get hook node
        hook = self._node.find('hook')

        # get uri attribute
        size = hook.attrib.get("SIZE", "")

        return size

    def set_image(self,
            link="",
            size="1",
            modified='',
            ):




        #
        # prepare path string
        #

        # convert backslashes to slashes
        link = link.replace("\\", "/")

        # check for Windows-style absolute path
        _match = re.search(r'^([A-z]:/)', link)

        # check for absolute linux path
        if link[0] == "/":
            link = "file://" + link
        # check for absolute windows path
        elif _match:
            link = "file:///" + link
        # should be relative path
        elif link[0] == ".":
            pass
        else:
            link = "./" + link

        # localize XML hook element below node
        hook = self._node.find('hook')
        if hook is None:

            # create hook element
            hook = ET.Element(
                    "hook",
                    URI=link,
                    SIZE=str(size),
                    NAME='ExternalObject',
                    )

            # add hook to node's children
            self._node.append(hook)

        else:

            # just override attributes
            hook.set("URI", link)
            hook.set("SIZE", size)




        #
        # set creation and modification dates
        #

        update_date_attribute_in_node(
                node=self._node,
                date=modified,
                key="MODIFIED",
                )

        return True

    @property
    def id(self):
        return self._node.attrib['ID']

    @id.setter
    def id(self, strId):

        # ensure type
        if not type(strId) == str:
            strId = str(strId)

        # check required format
        if not strId.lower().startswith('id_'):
            print('[ INFO   : in Freeplane, an ID must start with "ID_" and contain a number string.')
            # correct ID format
            strId = "ID_"+strId

        if not strId[len('id_'):].isnumeric():
            print('[ WARNING: in Freeplane, an ID must have a certain format. ignoring ID change request.')
            return False

        # set new ID
        self._node.attrib["ID"] = strId
        return True

    @property
    def attributes(self):
        _attribute = {}
        _lst = self._node.findall('attribute')
        for _attr in _lst:
            _name = _attr.get('NAME', '')
            _value = _attr.get('VALUE', '')
            if _name:
                _attribute[_name] = _value
        return _attribute


    def set_attribute(self,
                key='',
                value='',
                ):
        """
        This functions sets an attribute for a node
        """




        #
        # IF attribute key already exists
        #

        if key.lower() in [ _.lower() for _ in self.attributes.keys() ]:

            #
            # overwrite existing value
            #

            _lst = self._node.findall('attribute')
            for _attr in _lst:
                _name = _attr.get('NAME', '')
                if key.lower() == _name.lower():
                    _attr.set('VALUE', value)

        #
        # ELSE
        #

        else:

            #
            # create new attribute
            #

            _attrib = ET.Element("attribute", NAME=key, VALUE=value)

            # append element
            _node = self._node.append(_attrib)


    def add_attribute(self,
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

        # return self.attributes


    @property
    def style(self):
        if 'STYLE_REF' in self._node.attrib.keys():
            return self._node.attrib['STYLE_REF']
        return ""

    @style.setter
    def style(self, strStyle):

        #
        # try to re-connect to a valid mindmap
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
            for _stylename in self._map.styles.keys():
                if _stylename.lower() == strStyle.lower():
                    break
            else:
                print('[ WARNING: style "' + strStyle + '" not found in mindmap. make sure, style exists. ]')

        # set style reference in XML node
        self._node.attrib["STYLE_REF"] = strStyle

        return True


    @property
    def creationdate(self):

        # check for TEXT attribute
        if self._node.get('CREATED'):

            # read out text content
            text = self._node.attrib['CREATED']

            # convert to float time value
            _time = float(text)/1000

            # return datetime value
            return datetime.datetime.fromtimestamp(_time).timetuple()

        return tuple()


    @property
    def modificationdate(self):

        # check for TEXT attribute
        if self._node.get('MODIFIED'):

            # read out text content
            text = self._node.attrib['MODIFIED']

            # convert to float time value
            _time = float(text)/1000

            # return datetime value
            return datetime.datetime.fromtimestamp(_time).timetuple()

        return tuple()


    @property
    def corelink(self):

        # as the link can be present within the node's core or the node's
        # richtext section, here both should be checked. this is done using the
        # plaintext function.

        # check for TEXT attribute
        _text = self.plaintext
        if _text:

            # check for formula identifier
            if _text[0] == "=":




                #
                # check for reference to external node
                #

                # identify link based on type (file, http, ...)




                #
                # check for reference to internal node content
                #

                _match=re.match(r'^.*ID_([\d]+)\.text.*', _text)
                if _match:
                    return 'ID_' + _match.group(1)




        return ""


    @property
    def comment(self):

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
    def details(self):

        _text = ''

        # check for details node
        _lstDetailsNodes = self._node.findall("./richcontent[@TYPE='DETAILS']")
        if _lstDetailsNodes:
            _text = ''.join(_lstDetailsNodes[0].itertext()).strip()

        return _text


    @details.setter
    def details(self, strDetails):

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
            for strLine in strDetails.split('\n'):
                _p    = ET.SubElement(_body, "p")
                _p.text = strLine
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

        # return self.details


    @property
    def parent(self):

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
            #print("[ ERROR  : local parentmap has not been created for detached node. ]")
            return None


    @property
    def previous(self):

        # ensure existing parent
        _previous = self._node.getprevious()
        if _previous is not None:

            # create Node instance
            fpnode = Node(_previous, self._map)

            # update branch reference in case of detached node
            if not self.is_root_node and not self.is_map_node:
                fpnode._map     = None
                fpnode._branch  = self._branch

            # append node object
            return fpnode
        else:
            return None


    @property
    def next(self):

        # ensure existing parent
        _next = self._node.getnext()
        if _next is not None:

            # create Node instance
            fpnode = Node(_next, self._map)

            # update branch reference in case of detached node
            if not self.is_root_node and not self.is_map_node:
                fpnode._map     = None
                fpnode._branch  = self._branch

            # append node object
            return fpnode
        else:
            return None


    @property
    def icons(self):
        _icons = []
        _lst = self._node.findall('icon')
        for _icon in _lst:
            _name = _icon.get('BUILTIN', '')
            if _name:
                _icons.append(_name)
        return _icons


    def add_icon(self,
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

        # return self.icons


    def remove(self,
                ):
        """
        This functions removes the current Freeplane node from a branch
        """

        # get parent element
        parent = self.parent

        # remove the current node
        parent._node.remove(self._node)

        return True


    def del_icon(self,
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

        # return self.icons


    @property
    def children(self):
        lstNodesRet = []
        for _node in  self._node.findall("./node"):

            # create Node instance
            fpnode = Node(_node, self._map)

            # update branch reference in case of detached node
            if not self.is_root_node and not self.is_map_node:
                fpnode._map     = None
                fpnode._branch  = self._branch

            # append node object
            lstNodesRet.append(fpnode)

        return lstNodesRet


    @property
    def index(self):
        # valid child index values can be determined in case the node is not a
        # root node and has a parent
        if not self.is_root_node and self.parent:
            return self.parent._node.index(self._node)
        return 0


    def get_child_by_index(self, idx=0):
        # check if node has children
        _children = self._node.findall("./node")
        if len(_children):
            # run through all child nodes
            for _i, _child in enumerate(_children):
                # check for matching index
                if _i == idx:

                    # create Node instance
                    fpnode = Node(_child, self._map)

                    # update branch reference in case of detached node
                    if not self.is_root_node and not self.is_map_node:
                        fpnode._map     = None
                        fpnode._branch  = self._branch

                    # append node object
                    return fpnode

            # index not found
            else:
                return None
        # no children present
        else:
            return None

    def get_indexchain_until(self, node):
        """
        determine the list of index values which have to be used in order to
        find the given node. the process is started from the self object and
        continued until the given node was found. the actual implementation
        works from backwards. starting at the given node and determining its
        parents until the base node (self) was found. then reversing the list
        order.
        """

        # default and error return
        lstIdxValues = []

        # init
        _run = node

        # check if given node (or it's parents) is not rootnode
        while not _run.is_rootnode:

            # break loop if start of chain reached
            if self.id == _run.id:
                break

            # get parent of current node (go back one level)
            parent = _run.parent

            # determine node's child idx below it's parent
            for _i, child in enumerate(parent.children):
                if child.id == _run.id:
                    lstIdxValues.append(_i)
                    break

            # next loop
            _run = parent

        # reverse results
        return list(reversed(lstIdxValues))


    def is_descendant_of(self, node):
        """
        determine if the current node object has a direct relational connection
        to a given node element. so, if the current node object is a child,
        grand-child, ... of that given node element.
        """

        # walk up the parent elements until the given element is found or the
        # search ends with the root node

        # get 1st parent element
        parent = self.parent

        # loop
        while parent:

            # check for match
            if parent.id == node.id:
                return True

            # leave function if we reached the root node
            if parent.id == self._map.rootnode:
                return False

            # get next parent further up
            parent = parent.parent

        # this statement shouldn't be reached
        return False


    @property
    def is_rootnode(self):
        if self._map._rootnode == self._node \
                and not self._branch:
            return True
        return False


    @property
    def is_comment(self):
        if not self._node.get('STYLE_REF') is None \
                and self._node.attrib['STYLE_REF'] == 'klein und grau':
            return True
        return False


    @property
    def has_children(self):
        if not self._node.findall('./node'):
            return False
        return True


    def find_nodes(
            self,
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
        lstXmlNodes = self._node.findall(".//node")

        # do the checks on the base of the list
        lstXmlNodes = reduce_node_list(
            lstXmlNodes=lstXmlNodes,
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
        for _node in lstXmlNodes:

            # create Node instance
            fpnode = Node(_node, self._map)

            # update branch reference in case of detached node
            if not self.is_root_node and not self.is_map_node:
                fpnode._map     = None
                fpnode._branch  = self._branch

            # append node object
            lstNodesRet.append(fpnode)

        return lstNodesRet


    def find_children(self,
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
        lstXmlNodes = self._node.findall("./node")

        # do the checks on the base of the list
        lstXmlNodes = reduce_node_list(
            lstXmlNodes=lstXmlNodes,
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
        for _node in lstXmlNodes:

            # create Node instance
            fpnode = Node(_node, self._map)

            # update branch reference in case of detached node
            if not self.is_root_node and not self.is_map_node:
                fpnode._map     = None
                fpnode._branch  = self._branch

            # append node object
            lstNodesRet.append(fpnode)

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


    def attach(self,
            attached_node=None,
            pos=-1,
            ):
        """
        This functions appends an existing but previously detached
        Freeplane-Node as a child to this node object.
        """

        # CAUTION
        #
        # after using this function, node references targetting the attached
        # branch will not be valid anymore. this is due to changes which
        # currently cannot be updated within the reference objects on the user
        # side. so, please, ensure that after using the attach function, all
        # needed node references are re-created e.g. by using find() on the
        # map.




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
                print('[ WARNING: node "' + str(attached_node) + \
                        '" already attached to a map. NOTHING DONE. ]')
                return False
        elif attached_node.is_detached_node:
            print('[ WARNING: node "' + str(attached_node) + \
                    '" is part of a detached branch. NOTHING DONE. please only attach branch head. ]')
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


    def add_arrowlink(self,
            node=None,
            style='',
            shape='',
            color='',
            width='',
            transparency='',
            dash='',
            fontsize='',
            font='',
            startinclination='',
            endinclination='',
            startarrow='NONE',
            endarrow='DEFAULT',
            ):
        """
        add an arrow link to a node. the arrow starts at the host object and extends to an arbitrary node.
        """

        if node:




            #
            # create arrow link node
            #

            _node = ET.Element('arrowlink')




            #
            # append arrow link node to node object
            #

            self._node.append(_node)




            #
            # IF named style definition was given
            #

            if style:




                #
                # set style according to style definition
                #

                pass




            #
            # ELSE
            #

            else:




                #
                # set individual style members
                #

                if not shape:
                    _node.set('SHAPE', 'CUBIC_CURVE')
                else:
                    _node.set('SHAPE', shape)
                if not color:
                    _node.set('COLOR', '#000000')
                else:
                    _node.set('COLOR', color)
                if not width:
                    _node.set('WIDTH', '2')
                else:
                    _node.set('WIDTH', width)
                if not transparency:
                    _node.set('TRANSPARENCY', '80')
                else:
                    _node.set('TRANSPARENCY', transparency)
                if dash:
                    _node.set('DASH', dash)
                if not fontsize:
                    _node.set('FONT_SIZE', '9')
                else:
                    _node.set('FONT_SIZE', fontsize)
                if not font:
                    _node.set('FONT_FAMILY', 'SansSerif')
                else:
                    _node.set('FONT_FAMILY', font)
                if not startinclination:
                    _node.set('STARTINCLINATION', '131;0;')
                else:
                    _node.set('STARTINCLINATION', startinclination)
                if not endinclination:
                    _node.set('ENDINCLINATION', '131;0;')
                else:
                    _node.set('ENDINCLINATION', endinclination)
                if not startarrow:
                    _node.set('STARTARROW', 'NONE')
                else:
                    _node.set('STARTARROW', startarrow)
                if not endarrow:
                    _node.set('ENDARROW', 'DEFAULT')
                else:
                    _node.set('ENDARROW', endarrow)

            # destination
            _node.set('DESTINATION', node.id)




        return False


    def add_child(self,
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
        node.plaintext = core




        #
        # overwrite standard id
        #

        if id:
            node.id = id
            if not node.id == id:
                return None




        #
        # set link portion
        #

        if link:
            node.hyperlink = link




        #
        # set style
        #

        if style:
            node.style = style




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
        if self.is_root_node or self.is_map_node:

            # add this object as parent to new object
            self._map._parentmap[_node] = self._node

        else:

            # create _branch and _parentmap nodes in new child
            node._branch = self._branch

            # add this object as parent to new object within detached branch
            self._branch._parentmap[_node] = self._node




        return node


    def add_sibling(self,
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
        node.plaintext = core




        # overwrite standard id
        if id:
            node.id = id
            if not node.id == id:
                # print("[ WARNING: node id must follow Freplane's format rules. nothing done. ]")
                return None




        #
        # set link portion
        #

        if link:
            node.hyperlink = link




        #
        # set style
        #

        if style:
            node.style = style




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
        if self.is_root_node or self.is_map_node:

            # add this object as parent to new object
            self._map._parentmap[_node] = self._node.getparent()

        # check if this node is attached to a branch
        elif self._node in self._branch._parentmap.keys():
            self._branch._parentmap[_node] = self._node.getparent()

        else:

            # output warning
            print("[ WARNING: it is not possible to add a sibling to a detached node. please use the create_node function. ]")
            return None




        return node


#
# HELPERS
#

def update_date_attribute_in_node(
            node=None,
            date="",
            key="MODIFIED",
            ):

    # leave if inappropriate arguments
    if node is None:
        return False

    # calculate current date in milliseconds
    _current_time = datetime.datetime.now()
    _current_timestamp = str(int(_current_time.timestamp()*1000))

    # set modification date
    if date:
        node.set(key, date)
    else:
        # set current date
        node.set(key, _current_timestamp)

    return True


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
        lstXmlNodes=[],
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
        for _node in lstXmlNodes:
            if id.lower() == _node.attrib.get("ID", "").lower():
                _lstNodes.append(_node)
        lstXmlNodes = _lstNodes

    # check for TEXT within a node's CORE
    if core:
        _lstNodes = []
        for _node in lstXmlNodes:
            if exact:
                if core == _node.attrib.get("TEXT", ""):
                    _lstNodes.append(_node)
            else:
                if core.lower() in _node.attrib.get("TEXT", "").lower():
                    _lstNodes.append(_node)
        lstXmlNodes = _lstNodes

    # check for all ATTRIBUTES within a node
    if attrib:
        _lstNodes = []
        # check for current list of nodes
        for _node in lstXmlNodes:
            # get attributes of node
            for _attribnode in _node.findall("./attribute"):
                _key = _attribnode.attrib.get("NAME", "")
                _value = ""
                if _key:
                    _value = _attribnode.attrib.get("VALUE", "")
                # check all given attributes
                iFound = 0
                for _check_key, _check_value in attrib.items():
                    # key and value found in node
                    if _key == _check_key and _value == _check_value:
                        iFound += 1
                # check for ALL matches
                if iFound == len(attrib.items()):
                    _lstNodes.append(_node)
        lstXmlNodes = _lstNodes

    # check for LINK within a node's LINK TEXT
    if link:
        _lstNodes = []
        for _node in lstXmlNodes:
            if exact:
                if link.replace("\\","/") == _node.attrib.get("LINK", "").replace("\\", "/"):
                    _lstNodes.append(_node)
            else:
                if link.replace("\\", "/").lower() in _node.attrib.get("LINK", "").replace("\\", "/").lower():
                    _lstNodes.append(_node)
        lstXmlNodes = _lstNodes

    # check for BUILTIN ICON at node
    if icon:
        _lstNodes = []
        for _node in lstXmlNodes:
            # check for icon node
            _lstIconNodes = _node.findall("./icon[@BUILTIN='" + icon + "']")
            if _lstIconNodes:
                _lstNodes.append(_node)
        lstXmlNodes = _lstNodes

    # check for node's DETAILS
    if details:
        _lstNodes = []
        for _node in lstXmlNodes:
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
        lstXmlNodes = _lstNodes

    # and back
    return lstXmlNodes


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

