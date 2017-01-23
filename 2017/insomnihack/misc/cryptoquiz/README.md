# IceCTF-2016 : Misc/Crypto 50

**Solver:** AnarKy
**Category:** Misc/Crypto
**Points:** 50
**Description:**

Hello, young hacker.  Are you ready to fight rogue machines?  Now, you'll have to prove us that you are a genuine cryptographer.

Running on quizz.teaser.insomnihack.ch:1031

## Writeup

Upon using netcat to connect to the service you are greeted with....

```
\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ Hello, young hacker. Are you ready to fight rogue machines ?    ~~
~~ Now, you'll have to prove us that you are a genuine             ~~
~~ cryptographer.                                                  ~~
\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


~~ What is the birth year of Paul van Oorschot 
```

At this point, when you answer the question you are given another name. A quick python script checks the name and spits back the year
if the name is in the database, and if it isn't, exit letting us know which name it was.  After running enough, and googling all the 
years, we end up with something like...


```python
import sys, socket
from time import sleep

target = 'quizz.teaser.insomnihack.ch'
port = 1031

people = { "Douglas Stinson" : "1956",	"Donald Davies" : "1924", "Jim Massey" : "1934", "Joan Daemen" : "1965", "Yvo Desmedt" : "1956", "Jacques Stern" : "1949", "Dan Boneh" : "1969", "Paulo Barreto" : "1965",
	"Tatsuaki Okamoto" : "1952", "Ralph Merkle" : "1952", "Martin Hellman" : "1945", "Markus Jakobsson" :  "1968", "Michael O. Rabin" : "1931", "Jacques Patarin" : "1965",	"Phil Rogaway" : "1962",
	"Mitsuru Matsui" : "1961", "Shai Halevi" : "1966", "Antoine Joux" : "1967", "Horst Feistel" : "1915", "Ronald Cramer" : "1968",	"Whitfield Diffie" : "1944", "Arjen K. Lenstra" : "1956",
	"Lars Knudsen" : "1962", "Paul Kocher" : "1973", "Rafail Ostrovsky" : "1963", "Serge Vaudenay" : "1968", "Daniel Bleichenbacher" : "1964", "Yehuda Lindell" : "1971", "Victor S. Miller" : "1947",
	"Xuejia Lai" : "1954", "Eli Biham" : "1960", "Kaisa Nyberg" : "1948", "Niels Ferguson" : "1965", "Alex Biryukov" : "1969", "Paul van Oorschot" : "1962", "Ross Anderson" : "1956",
	"Daniel J. Bernstein" : "1971",	"Moni Naor" : "1961", "Amos Fiat" : "1965", "Ron Rivest" : "1947", "Adi Shamir" : "1952", "Claus-Peter Schnorr" : "1943", "Nigel P. Smart" : "1967",
	"Markus Jakobsson" : "1968", "Douglas Stinson" : "1956", "David Naccache" : "1967"
	}

att = 1
try:
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    s.connect(( target, port ))
    while True:
	print "### ROUND %s ###" %att
	response = s.recv(4096)
	print "recv started"
	if len(response) == 1:
                response = s.recv(4096)
	if att == 1:
		print "Banner"
	        response = s.recv(4096)
                name = response[31:-4].strip()
	else:
		name = response[30:-3].strip()
        print "RESPONSE: %s " %response
	print "NAME: *%s*" %name
	if name.strip() in people:
		answer = people[name]
		s.send(answer + "\n")
		print "Sent %s" % answer
		att += 1
	else:
		print "%s - MISSING!" % name
		break
    print "DONE!"
    s.close()
except:
	print "FAIL!"
	sys.exit()
```

When ran, your output should look like this....

```
### ROUND 1 ###
recv started
Banner
RESPONSE: 

~~ What is the birth year of Ron Rivest ?

 
NAME: *Ron Rivest*
Sent 1947
### ROUND 2 ###
recv started
RESPONSE: 
~~ What is the birth year of Adi Shamir ?
 
NAME: *Adi Shamir*
Sent 1952
### ROUND 3 ###
recv started
RESPONSE: 
~~ What is the birth year of Joan Daemen ?

 
NAME: *Joan Daemen*
Sent 1965
### ROUND 4 ###
recv started
RESPONSE: 
~~ What is the birth year of Douglas Stinson ?
 
NAME: *Douglas Stinson*
Sent 1956
### ROUND 5 ###
recv started
RESPONSE: 
~~ What is the birth year of Rafail Ostrovsky ?

 
NAME: *Rafail Ostrovsky*
Sent 1963
### ROUND 6 ###
recv started
RESPONSE: 
~~ What is the birth year of Donald Davies ?
 
NAME: *Donald Davies*
Sent 1924
### ROUND 7 ###
recv started
RESPONSE: 
~~ What is the birth year of Nigel P. Smart ?

 
NAME: *Nigel P. Smart*
Sent 1967
### ROUND 8 ###
recv started
RESPONSE: 
~~ What is the birth year of Eli Biham ?
 
NAME: *Eli Biham*
Sent 1960
### ROUND 9 ###
recv started
RESPONSE: 
\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~ OK, young hacker. You are now considered to be a                ~~
~~ INS{GENUINE_CRYPTOGRAPHER_BUT_NOT_YET_A_PROVEN_SKILLED_ONE}     ~~
\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

* flag = INS{GENUINE_CRYPTOGRAPHER_BUT_NOT_YET_A_PROVEN_SKILLED_ONE}

## Other resources (optional)



