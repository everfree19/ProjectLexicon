import re
from html.parser import HTMLParser
from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup



class LinkFinder():
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.allExtLinks = set()
        self.allIntLinks = set()


    def getAllExternalLinks(self, page_url):
        html = urlopen(page_url)
        bsObj = BeautifulSoup(html, "html.parser")
        internalLinks = getInternalLinks(bsObj, splitAddress(self.base_url)[0])
        externalLinks = getExternalLinks(bsObj, splitAddress(self.base_url)[0])
        self.appendInternalLink(internalLinks)
        self.appendExternalLink(externalLinks)

    def appendExternalLink(self, externalLinks):
        for link in externalLinks:
            if link not in self.allExtLinks:
                self.allExtLinks.add(link)
                print(link)

    def appendInternalLink(self, internalLinks):
        for link in internalLinks:
            if link == "/":
                link = self.base_url
            elif link[0:2] == "//":
                link = "http:" + link
            elif link[0:1] == "/":
                link = self.base_url + link
            if link not in self.allIntLinks:
                print("About to get link: "+link)
                self.allIntLinks.add(link)

    def page_internalLink(self):
        return self.allIntLinks


############### non class member ###############
# 페이지에서 발견된 내부 링크를 모두 목록으로 만듭니다.
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # /로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

# 페이지에서 발견된 외부 링크를 모두 목록으로 만듭니다.
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두 찾습니다.
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

