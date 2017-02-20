# Nullcon HackIM 2017 : programming4/400 points

**Solver:** jopehagen
**Category:** programming
**Points:** 400
**Description:**

Destroy the enemy bot and take control of our precious next generation robo. 
52.90.9.177:9999

## Writeup

Upon connecting to the server you are prompted with a game.

To figure out the solution i played the game until i hit a point in which i could not advance; i recorded my solutions up to this point.

i repeated this process to make sure i didn't miss anything, but repeated attempts resulted in the same error

"Battery Died"

Since this was a programming problem i assumed this was time based and wrote this script:

```python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('52.90.9.177', 9999))
count = 0
cmd = ["2","1","service port","4","1","abacus77""service port","6","1","service port","5","1"," "," "," "," "]
opt = 0
while 1:
        data = sock.recv(1024)
        print(data)
        if "control:" in data:
                sock.sendall(cmd[opt])
                opt += 1
        elif "[KEYPAD]" in data:
                sock.sendall(cmd[opt])
                opt+=1
```

this resulted in the solution.

## Other resources (optional)
