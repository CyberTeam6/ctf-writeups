# IceCTF-2016 : rip-transmission-65

**Category:** forensics
**Points:** 64
**Description:**

This seems to be receiving some sort of transmission. Our experts have been working around the clock trying and figure out what the hell it means with no hope of getting to the bottom of it. You’re our only hope.

## Writeup

I pulled down the binary and loaded it up with binary ninja to see if there was an easy flag sitting there. This program is absolutely crazy and stepping through the application wasn’t helpful at all.

Since it is a Forensics challenge, I wanted to see if there was anything hidden inside of the binary. So I loaded up Foremost to see if there was anything interesting inside.

foremost rip_2067f9686b4d07eea2cac19b9c6588b2abac16500135901ce8781e4ccc262446 
Processing: rip_2067f9686b4d07eea2cac19b9c6588b2abac16500135901ce8781e4ccc262446
|foundat=rip.jpgUT *|

It looks like there is a jpg hidden in there. Should be nice and easy. Move into the folder and notice that there is a zip archive that has a password. Loaded up AAPR on my windows machine. (You can use the DEMO version for .zip files) and it popped the password (bunny) in a minute or two. Used the password on the zip file and extract the rip.jpg image and the flag is written on the image



