import HtmlProcessor, XmlProcessor

__author__ = 'sergioska'

import re


class Processor(object):
    @staticmethod
    def factory(content, stylesheet):
        """
        factory pattern instance correct processor class
        @param content:
        @param stylesheet:
        @return:
        """
        if re.search(r'^[^<]*<\?xml[ ]', content) is not None:
            return XmlProcessor.XmlProcessor(content, stylesheet)
        return HtmlProcessor.HtmlProcessor(content, stylesheet)
