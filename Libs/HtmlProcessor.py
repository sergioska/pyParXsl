from pyCrawler.Libs import AbstractProcessor

__author__ = 'sergioska'

import lxml.etree as XTree
from BeautifulSoup import BeautifulSoup
import cStringIO
import StringIO

class HtmlProcessor(AbstractProcessor.AbstractProcessor):

    @property
    def process(self):
        parser = XTree.HTMLParser()
        tmpdom = XTree.parse(cStringIO.StringIO(self.content), parser)
        self.content = XTree.tostring(tmpdom.getroot())
        self.content = self.content[self.content.index("<body "):]
        soup = BeautifulSoup(self.content)
        self.content = soup.prettify()
        try:
            f = StringIO.StringIO(self.content)
            doc = XTree.parse(f)
            xslt = XTree.parse(self.stylesheet)
            transform = XTree.XSLT(xslt)
            newdom = transform(doc)
        except IOError:
            print "Xml or Xsl file not found!"
            return False
        return XTree.tostring(newdom, pretty_print=True)

