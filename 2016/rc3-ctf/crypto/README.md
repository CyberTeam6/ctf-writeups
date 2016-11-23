# RC3-CTF : crypto300

**Solver:** attackd0gz	
**Category:** crypto
**Points:** 300
**Description:**

Decipher the image and find the flag. *I will edit this when the RC3 site comes back up.

## Writeup

For this challenge, they provided us with a gif file, which was a bunch of pictures of cats.  We already knew the flag format, so I started with "RC3-2016-" and came to the conclusion that I was looking for a 8 character word to put at the end of the key.  I used a website (found below) which breaks gifs down into individual pictures to take a closer look.  There were 8 pictures altogether.

The first thing I did was run strings and exiftool on a couple images, but failed to come up with anything of value.  I decided I might have been looking a bit too deep, so I just looked at the individual images as they were.  I counted the number of cats on each image and came up with:

Image 1 - 14  
Image 2 - 9  
Image 3 - 1  
Image 4 - 20  
Image 5 - 23  
Image 6 - 15  
Image 7 - 5  
Image 8 - 13  

When I convert those numbers to their corresponding letters of the alphabet, it becomes:

14 - n  
9  - i  
1  - a  
20 - t  
23 - w  
15 - o  
5  - e  
13 - m  

Reverse that... 

niatwoem == meowtain

flag == RC3-2016-meowtain


## Other resources (optional)

http://ezgif.com/split


