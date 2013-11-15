__author__ = 'sergioska'

import AbstractProcessor
import lxml.etree as XTree


class XmlProcessor(AbstractProcessor.AbstractProcessor):

    @property
    def process(self):
        """
        implement process logic for xml
        @return:
        """
        try:
            dom = XTree.parse(self.content)
            xslt = XTree.parse(self.stylesheet)
            transform = XTree.XSLT(xslt)
            newdom = transform(dom)
        except IOError:
            print "Xml or Xsl file not found!"
            return False
        return XTree.tostring(newdom, pretty_print=True)