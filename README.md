#pyParXsl *(~payparxel)*

is a **toolkit** for python parser applications **xslt** transformation language based.

It can process html or xml source code from url or local file; about url request, throw your mini http client, now it can request only page in get mode.

In the project root is present a test file (test.py) that test the toolkit; in this test script there isn't a valid web url (and stylesheet is only an example), but you can use it this as 'from scratch' 
Otherwise uou can write a base parser xslt based that process a page from a web request, with follow sample code.


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

- [X] Html parsing
- [ ] Check Xml parsing
- [ ] Add post request feature to HttpClient
- [ ] Add working sample (with an really url and really stylesheet)
- [ ] Split HttpClient login in 2 layers (divide get/post login from client request feature such as getPage) 

