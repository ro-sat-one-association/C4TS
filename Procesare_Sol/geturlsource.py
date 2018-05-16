import sys
import pycurl
import certifi

def getSource(URLString):
    class ContentCallback:
            def __init__(self):
                    self.contents = ''
    
            def content_callback(self, buf):
                    self.contents = self.contents + buf
    
    t = ContentCallback()
    curlObj = pycurl.Curl()
    curlObj.setopt(pycurl.CAINFO, certifi.where())
    curlObj.setopt(curlObj.URL, URLString)
    curlObj.setopt(curlObj.WRITEFUNCTION, t.content_callback)
    curlObj.perform()
    curlObj.close()
    return t.contents