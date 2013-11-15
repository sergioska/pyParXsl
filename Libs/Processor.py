from pyCrawler.Libs import HtmlProcessor, XmlProcessor

__author__ = 'sergioska'

import re


class Processor(object):
    @staticmethod
    def factory(content, stylesheet):
        if re.search(r'^[^<]*<\?xml[ ]', content) is not None:
            return XmlProcessor.XmlProcessor(content, stylesheet)
        return HtmlProcessor.HtmlProcessor(content, stylesheet)
