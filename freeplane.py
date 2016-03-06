# compatibility python2 and python3
from __future__ import print_function

# application relevant imports
import xml.dom.minidom
import html2text


class Freeplane(object):

    """
    Freeplane interfacing class

    Access Freeplane mindmap file and do various search, read and write
    operations to retrieve or modify text passages within the mindmap.

    """

    def __init__(self, strMindmapFile):

        """
        Create a DOM object from a mindmap and return it to caller

        parameters
            - strMindmapFile  ->  file path to mindmap
        """

        # read mindmap into DOM object
        self.mindmap = xml.dom.minidom.parse(strMindmapFile)

    # read text paragraph from mindmap
    def getText(self, strRootAttribute, strTitleText, strPortion):

        # get list of all attributes
        lstAttributes = self.mindmap.getElementsByTagName('attribute')

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
