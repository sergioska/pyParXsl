#pyParXsl 

is a tool for python parser application xslt transformation language based.

It can process html or xml source code from url or local file; about url request, throw your mini http client, now it can request only page in get mode.

You can write a base parser xslt based that process a page from a web request, with follow sample code.


```python
from Libs import Processor, Httpclient
'setting your stylesheet'
stylesheet = "yourstylesheet.xsl"
'request a web page'
client = Httpclient.Httpclient()
sWebOutput = client.getPage(url)
'apply the stylesheet to transform the source'
xProc = Processor.Processor()
processor = xProc.factory(sWebOutput, stylesheet)
print processor.process
``` 
