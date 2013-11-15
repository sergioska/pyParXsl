__author__ = 'sergioska'

''' this script is an example '''

import sys
from Libs import Processor, Httpclient
import os.path as Fs

url = "http://it.notizie.yahoo.com/rss/"
stylesheet = "Stylesheets/yahoorss.xsl"
buffer = "buffer.xml"


def main():
    if Fs.exists(buffer):
        print "READ FROM FILE"
        fhandle = file(buffer, "r")
        sWebOutput = fhandle.read()
    else:
        print "READ FROM WEB"
        fhandle = file(buffer, "w")
        client = Httpclient.Httpclient()
        sWebOutput = client.getPage(url)
        fhandle.write(sWebOutput)
    xProc = Processor.Processor()
    processor = xProc.factory(sWebOutput, stylesheet)
    print processor.process


if __name__ == "__main__":
    sys.exit(main())
