# Nullcon HackIM 2017 : programming1/200 points

**Solver:** jopehagen
**Category:** programming
**Points:** 100
**Description:**

We unearthed this text file from one of the older servers and want to know what this is all about. Could you please analyse this and let us know your finding?

## Writeup


Upon viewing the file, i quickly identified a list of tuples with values (255,255,255). This immediatly lead me to believe this list was RGB values.
Some google fu of "list of tuples to image python" led me to the python module Pillow.

```python
from PIL import Image

new_data=open("abc.txt").read()
data = eval(new_data)
print len(data)
for i in range(0,10):
	width = 300+(i*10)
	file = "abc"+str(i)+".jpg"
	im = Image.new('RGB', (width,6192))
	im.putdata(data)
	im.save(file, 'JPEG')

```

The for loop in the solution was because a width was not identified however, a trial width of 300 produced a close result.
The output 'abc1.jpg' was close enough for me to read the flag.

* flag = flag{Pil_PIL_PIL}

## Other resources (optional)



