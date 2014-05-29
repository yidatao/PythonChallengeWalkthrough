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
