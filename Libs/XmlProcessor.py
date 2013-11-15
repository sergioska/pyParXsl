from pyCrawler.Libs import AbstractProcessor

__author__ = 'sergioska'

import lxml.etree as XTree


class XmlProcessor(AbstractProcessor.AbstractProcessor):

    @property
    def process(self):
        try:
            dom = XTree.parse(self.content)
            xslt = XTree.parse(self.stylesheet)
            transform = XTree.XSLT(xslt)
            newdom = transform(dom)
            print(XTree.tostring(newdom, pretty_print=True))
        except IOError:
            print "Xml or Xsl file not found!"
            return False
        return True