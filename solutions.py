import webbrowser
import string
import urllib2
from bs4 import BeautifulSoup, Comment
from collections import Counter
import re
import pickle
import zipfile
from PIL import Image
import bz2
import xmlrpclib

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
    
def level7():
    img = Image.open("puzzleFiles/oxygen.png")
    # get the pixel of the grey area
    row = [img.getpixel((x, img.size[1]/2)) for x in range(0, img.size[0], 7)]
    # the color is grey if R==G==B, so get the value which is the ASCII code of a character
    hint1 = [chr(r) for r, g, b, t in row if r == g == b]
    print "".join(hint1)

    hint2 = [chr(x) for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]]
    print "".join(hint2)

def level8():
    username = bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
    password = bz2.decompress("BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")

    print username + "," + password

def level9():

    first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
    310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
    190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
    389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
    215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
    290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
    279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
    327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
    328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
    259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
    352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
    120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
    214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
    102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
    113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
    133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
    111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
    332,155,348,156,353,153,366,149,379,147,394,146,399]

    second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
    157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
    125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
    77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
    158,121,157,128,156,134,157,136,156,136]

    # the format is (x1,y1),(x2,y2) ...
    # use "zip" to create tuples
    cords1 = zip(first[::2],first[1::2])
    cords2 = zip(second[::2],second[1::2])


    img = Image.open("puzzleFiles/good.jpg")
    img2 = Image.new(img.mode, img.size)

    for x,y in cords1+cords2:
        img2.putpixel((x, y),(255,255,255))

    img2.save("puzzleFiles/good2.jpg")

def level10():
    current = [1]
    for i in range(0,30):
        current = look_n_say(current)
    print len(current)
    
def level11():
    img = Image.open('puzzleFiles/cave.jpg')
    imglist = [Image.new('RGB', (img.size[0]/2, img.size[1]/2)) for i in range(4)]

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            if x % 2 == 0 and y % 2 == 0:
                imglist[0].putpixel((x/2, y/2), img.getpixel((x,y)))
            elif x % 2 == 0 and y % 2 == 1:
                imglist[1].putpixel((x/2, (y-1)/2), img.getpixel((x,y)))
            elif x % 2 == 1 and y % 2 == 0:
                imglist[2].putpixel(((x-1)/2, y/2),img.getpixel((x,y)))
            else:
                imglist[3].putpixel(((x-1)/2, (y-1)/2),img.getpixel((x,y)))

    # save four images
    [imglist[i].save('puzzleFiles/%d.jpg' % i) for i in range(4)]

def level12():
    evil = open('puzzleFiles/evil2.gfx', 'rb')
    data = evil.read()
    evil.close()

    # write to 5 images
    for i in range(5):
        f = open('puzzleFiles/img'+str(i)+'.jpg', "wb")
        # like dealing the cards to 5 stacks
        f.write(data[i::5])
        f.close()

def level13():
    s = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print s.system.listMethods()
    print s.phone("Bert")

# acknowledge the blog post http://blog.csdn.net/kosl90/article/details/7341181 for helping me solving this level :D
def level14():
    #the sequence in the hint
    seq = [[i, i - 1 , i - 1, i - 2] for i in range(100, 1, -2)]
    #collapse to a single list
    seq = [i for l in seq for i in l]

    img = Image.open("puzzleFiles/wire.png")
    img_data = list(img.getdata())
    # the original image has 10000 pixels
    index = 0

    res = Image.new(img.mode,(100,100))
    res_data = res.load()

    # right, down, left, up (clockwise for a square)
    step = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # the current direction
    d = 0

    #cursor for writing to the result image
    cursor = (-1,0)

    for times in seq:
        for i in range(times):
            # move the cursor one step along the correct direction
            cursor = tuple(map(sum, zip(cursor, step[d])))
            # write to the result image
            res_data[cursor] = img_data[index]
            index += 1
        #change the direction (4 sides for a square)
        d = (d+1) % 4

    res.save("puzzleFiles/res14.png")

def openURL(url):
    webbrowser.open_new_tab(pythonChallengeURL+url+".html")

def look_n_say(num):
    next = []
    count = 0
    current = num[0]
    for i in num:
        if i == current:
            count = count+1
        else:
            next.append(count)
            next.append(current)
            count = 1
            current = i
    next.append(count)
    next.append(current)
    return next
        
if __name__ == "__main__":
    level14()
