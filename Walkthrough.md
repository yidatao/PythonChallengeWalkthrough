##Level 0

* Simple simple warm up
* Use double star (\*\*) for exponentiation: 2\*\*38 = 274877906944
* Use this number to replace the url

##Level 1

* A [Caesar cipher](http://en.wikipedia.org/wiki/Caesar_cipher), each letter in the plain text needs a right shift of 2
* `string.maketrans()` is recommended to translate the ciphertext to plaintext
* "Now apply on the url". Shame it took me a while to crack its meaning. Literally, decipher the url "map" to get "ocr"

##Level 2

* The clue in the HTML source is pretty straightforward: simply find the rare characters in the long meaningless string
* I used `Counter` to get the occurrence of each character. It's easy to see that a few characters appear only once
* `Counter` is convenient, but it messes up the order of characters. So after getting "aeilquty", think twice to get "equality"

##Level 3

* The page title, the hint and the image pretty much scream out loud: "regular expressions!"
* I used `[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]`
* The messy text is still in the html source, of course

##Level 4
* Go to "linkedlist.php" instead of "linkedlist.html", and click the image
* The URL changes to "nothing=12345", and the page says "the next nothing is 44827". Go to "nothing=44827", and you get another number. Combining the puzzle's title "follow the chain", it's pretty obvious what to do next
* In fact, the html source of the "linkedlist.php" gives another clue - automate this process instead of manually following the chain. Basically a loop and a regular expression match should suffice. Yet, something "odd" happens during the process, be prepared :-)

##Level 5
* So the "peak hell" = "pickle" joke is not that easy to get
* But when I checked the page source and looked at the "meaningless" banner.p content, it's safe to guess that we need to use python pickle to deserialize banner.p
* The name "banner.p" itself is also a clue, which indicates the output format is like that of the Unix banner program. So the core python programming here is to efficiently print "#" and spaces, whose counts are suggested by the deserialized object.

##Level 6
* So the clue is "zip". Change the URL to "channel.zip" and download it.
* Start with the readme, you'll find that this is another "the next nothing" game just like Level 4. This time, use python zipfile package to read the file content.
* And another surprise, the answer is hidden in the comment of every file. So collect the comment using zipfile's function and assemble them to get the final answer...not yet. 
* "Hockey" turned out to be another clue: look at the letters that made up "Hockey".

##Level 7
* Okay this one is tricky. I consulted a lot of resources to get this done [sigh]
* The key to this puzzle is actually quite straightforward: something is encoded in the grey area of the picture
* First we need to get the grey pixel by the coordinate (x,y). Horizontally, the grey color changes every 7 pixel (well, someone suggested it's because this is level "7"); Vertically, the grey area is roughly at the middle. So this leads to the code `row = [img.getpixel((x, img.size[1]/2)) for x in range(0, img.size[0], 7)]`
* A PNG file has four color values: (R,G,B,Transparency). One key to find the grey color is that it has [R=G=B](http://en.wikipedia.org/wiki/Grey). So this explains the code `hint1 = [chr(r) for r, g, b, t in row if r == g == b]`
* Now the last piece of the puzzle is to decode this ACSII value to a meaningful character using `chr()`

##Level 8
* Clicking the bee in the picture leads to another page, which is guarded by username (un) and password (pw). View the page source and you will find that they simply appear in the comment.
* Both strings start with `BZh91AY&SY`. Google it and you'll find the `bz2` module
* Also some minor clues: "bee", "working hard"->"busy"->sounds familiar?

##Level 9
* In the page source, the hint is "first+second?". Initially I assumed that the "first" array should be x coordinates while "second" should be y coordinates, but their lengths are different. So a safe guess is that the value is like [x1,y1,x2,y2...]
* So, we can use `first[::2]` and `first[1::2]` to get the x values and y values, respectively. Then using the `zip` function to create (x,y) tuples.
* Finally, we can draw a picture using these coordinates

##Level 10
* Clicking the bull gives an array `a = [1, 11, 21, 1211, 111221`, which is an [look-and-say](http://en.wikipedia.org/wiki/Look-and-say_sequence) sequence
* My own solution is not really elegant. Yet I found one good solution which requires only 2 lines of code:
  * `sets = re.findall("(1+|2+|3+)", s)`
  * `return "".join([str(len(x))+x[0] for x in sets])`

##Level 11
* The only hint is "odd even". So it must have something to do with the image's coordinates.
* For coordinates (x, y), there are four possibilities if we check whether their values are odd or even: (odd, even), (odd, odd), (even, odd), and (even, even)
* So for pixels that have the same odd/even properties, we put them into a new image, whose size is now half of that of the original image.
* Finally we end up with four new images. Two of the images that are created with (even, even) and (odd, odd) pixels of the original image reveal the answer 'evil', which appears on the top-right corner.

##Level 12
* I considered `eval()`, `shuffle`, but the hint is actually the image's name: why it's `evil1.jpg` instead of `evil.jpg`? This might leads you to check `evil2.jpg`, which gives a hint of using `evil2.gfx`
* Another hint is the image itself, in which a person is dealing cards into 5 piles. We should use the same strategy to distribute the bytes in `evil2.gfx` into 5 images. That is, each image gets the `i`, `i+5`, `i+10`, `i+15`, `i+20` bytes
* It's easy to explain this solution afterwards, but it's really hard to figure it out at first.

##Level 13
* When I checked the page source, I found this `<remote />` tag before evil. So, "remote" and "phone" made me think about "remote procedure call (RPC)".
* Clicking "5" leads to an XML page, with the root element as "methodResponse". If only I knew about the python library `xmlrpclib`, I would get this hint more quickly.
* The code is quite simple, except that the true "evil" is revealed in the previous level, http://www.pythonchallenge.com/pc/return/evil4.jpg (why I can only view this in IE?)

##Level 14
* The wire.png is actually 10000*1 = 100*100. The hint in the page source let us know that 100*100 = (100+99+99+98)..., which seems like a way to consume these 10000 pixels.
* The sequence gives 4 numbers as a "group", which is the number of pixels we consume at each of the four sides of a square. The cinnamon roll suggest we should do it clockwise.
* That's it. We consume the 10000 pixels as follows: 100 to the right, 99 down, 99 to the left, and 98 up, and so on...As such we'll get a new 100*100 image which renders the answer.

##Level 15
* First it's obvious we need to guess the year, which is 1??6. Two clues are given: Jan 1st is Thursday and it's a leap year (note in the bottom-right corner, Feb has 29 days). Using python's `calendar` module quickly renders a few candidates: 1176, 1356, 1576, 1756, 1976
* Then it's purely detective time. The page title says "whom?" and the page source says "he ain't the youngest, he is the second", so the answer should be a person
* The page source says "buy flowers for tomorrow", so a good guess is that this person's birthday is on Jan 27. The final answer is "mozart", whose birthday is on 1756-1-27

##Level 16
* Again, this puzzle is about image processing, and it's still difficult with little hint. So I googled the answer.
* Basically, the solution is to align the pink bar to the beginning of each line.
