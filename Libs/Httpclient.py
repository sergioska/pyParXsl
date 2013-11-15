__author__ = 'sergioska'

import pycurl
import cStringIO


class Httpclient:

    def __init__(self):
        Httpclient.buffer = cStringIO.StringIO()

    @classmethod
    def getPage(self, sUrl):
        """
        get html source page from cUrl request
        @param sUrl:
        @return:
        """
        c = pycurl.Curl()
        c.setopt(c.URL, sUrl)
        c.setopt(c.WRITEFUNCTION, Httpclient.buffer.write)
        c.perform()
        sRet = Httpclient.buffer.getvalue()
        Httpclient.buffer.close()
        return sRet







