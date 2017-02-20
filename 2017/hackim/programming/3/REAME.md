# Nullcon HackIM 2017 : programming3/300 points

**Solver:** jopehagen
**Category:** programming
**Points:** 300
**Description:**

Dig deeper and try harder


26685

## Writeup
This challenge involved unarchiving... a lot of times

```python
import os

while True:
	ls = commands.getstatusoutput("ls")
	if "26685.out" in ls[1]:
		os.system("mv 26685.out 26685")
	if "a.out" in ls[1]:
		os.system("mv a.out 26685")
	data = commands.getstatusoutput('file 26685')
	print(data)
	print(data[1])
	if "LZMA" in data[1]:
		os.system("mv 26685 26685.lzma")
		os.system("unxz 26685.lzma")
	elif "XZ" in data[1]:
		os.system("mv 26685 26685.xz")
		os.system("unxz 26685.xz")
	elif "gzip" in data[1]:
		os.system("mv 26685 26685.gz")
		os.system("gunzip 26685.gz")
	elif "POSIX" in data[1]:
		print("POSIX")
		os.system("tar -xvf 26685")
	elif "bzip2" in data[1]:
		print("BZIP")
		os.system("bzip2 -d 26685")
		os.system("mv 26685.out 26685")
	elif "NuFile" in data[1]:
		os.system("./nulib/nulib2-master/nulib2/nulib2 -x /root/ctf/26685")
	elif "lzip" in data[1]:
		os.system("lunzip 26685")
	elif "ZPAQ" in data[1]:
		os.system("mv 26685 26685.zpaq")
		os.system("zp ex 26685.zpaq")
	elif "Zoo" in data[1]:
		os.system("mv 26685 26685.zoo")
		os.system("zoo -extract 26685")
	elif "7-zip" in data[1]:
		os.system("7z e 26685")
	elif "ARJ" in data[1]:
		os.system("mv 26685 26685.arj")
		os.system("arj e 26685.arj")
	elif "Zip" in data[1]:
		os.system("unzip 26685")
	else:
		break;

```

I created this script one step at a time.. every time i hit a new compression type i added a new conditional statement to handle that type.
some of the compression algorythms required a rename, and some change the output location (initial ls conditionals handled that)
The only one that took me a bit of time was the NuFile apple compression, i ran into issues when attempting to overwrite the original file.. so i manually output it to a.out. this was slow but it got the job done.
after running the script, there was an ascii file with an "la -la" output.

```
drwx------ 2 root     root     28672 Dec 23 21:01 apt-dpkg-install-kKBLWj
-rw-r--r-- 1 root     root     71259 Dec 23 19:50 apt-fast.list
-rw-r--r-- 1 root     root         0 Dec 23 19:50 apt-fast.lock
-rw-r--r-- 1 root     root         0 Dec 23 21:03 secr
drwx------ 3 root     root      4096 Dec 23 19:30 systemd-private-20af98806288452f91376e836938dc35-colord.service-hbUpEj
drwx------ 3 root     flag      4096 Dec 23 19:30 63336C756448746861486C35634442684C565A686353467566513D3D
```
a file was owned by group flag was a hexadecimal string.
```
63336C756448746861486C35634442684C565A686353467566513D3D
```
decoding the hexacdecimal string gave a base64 string
```
c3ludHthaHl5cDBhLVZhcSFufQ==
```
decoding the base 64 string gave a rot13 string
```
synt{ahyyp0a-Vaq!n}
```
rot13 decode:
```python
import string
rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
print(string.translate("synt{ahyyp0a-Vaq!n}", rot13))
```

* flag = flag{nullc0n-Ind!a}

## Other resources (optional)



