import webbrowser
import string
import urllib2
from bs4 import BeautifulSoup, Comment
from collections import Counter
import re
import pickle
import zipfile
import os.path

pythonChallengeURL = 'http://www.pythonchallenge.com/pc/def/'

def level0():
    answer = 2**38
    print answer
    openURL(str(answer))

def level1():
    ciphertext = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
    table = string.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
    print ciphertext.translate(table)
    openURL("map".translate(table))

def level2():
    # first get the mess from html source
    source = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()
    soup = BeautifulSoup(source)
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    mess = comments[1]
    # count the instance
    count = Counter(list(mess))
    for k,v in count.iteritems():
        if v == 1:
            print k,
    # using Counter ruins the order of the characters, though
    openURL("equality")

def level3():
    # first get the mess from html source
    source = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
    soup = BeautifulSoup(source)
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    mess = comments[0]
    # use regular expression to get characters
    answer = "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", mess))
    openURL(answer)

def level4():
    nothing = '12345'
    headURL = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    source = urllib2.urlopen(headURL+nothing).read()
    while True:
        if 'Divide by two' in source:
            nothing = str(int(nothing)/2)
        else:
            nothing = "".join(re.findall(r"nothing is (\d+)",source))
        print nothing
        if nothing == "":
            break
        source = urllib2.urlopen(headURL+nothing).read()
    print source

def level5():
    source = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    answer = pickle.load(source)
    for elements in answer:
        print "".join([e[0] * e[1] for e in elements])

def level6():
    nothing = '90052'  # check the Readme first
    file = zipfile.ZipFile("puzzleFiles/channel.zip", "r")
    rawContent = ''
    comments = []
    while True:
        try:
            content = file.read(nothing+'.txt')
        except:
            print rawContent
            break
        rawContent = content
        comments.append(file.getinfo(nothing+'.txt').comment)
        nothing = "".join(re.findall(r"Next nothing is (\d+)",content))        
    
    print ''.join(comments)
    


def openURL(url):
    webbrowser.open_new_tab(pythonChallengeURL+url+".html")

if __name__ == "__main__":
    level6()
