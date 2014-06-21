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
