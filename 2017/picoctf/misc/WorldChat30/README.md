# PicoCTF 2017 : misc/World Chat 30 points

**Solver:** attackd0gz
**Category:** misc
**Points:** 30
**Description:**

We think someone is trying to transmit a flag over WorldChat. Unfortunately, there are so many other people talking that we can't really keep track of what is going on! Go see if you can find the messenger at shell2017.picoctf.com:31955. Remember to use Ctrl-C to cut the connection if it overwhelms you!

## Writeup
Upon connecting to the World Chat server, I was greeted by a massive amount of traffic.  

...image

The first thing to do is output the traffic to a file to parse it further. 

...image

After grepping for "flag", there was still a ton of traffic, but I noticed this....

...image

So using grep, I just searched for the user, and found what I needed for the flag. 

...image

* flag = 42f66deb5f3c2ce50e2ae34323988f04

## Other resources (optional)
