# Nullcon HackIM 2017 : Misc3/300 points

**Solver:** jopenhagen/niden
**Category:** Misc
**Points:** 300
**Description:**

Got an artefact file to be analysed. Can you please help me find the hidden data ?


## Writeup

the file was compressed as a .xz
decompressing the file revieled that it was an ext3 image:
```bash
#file artefact
artefact: Linux rev 1.0 ext3 filesystem data, UUID=c6666f0c-f641-4958-be07-bcc6540fdafd (large files)
```
Niden (of Cyberteam6) pointed me in the direction of extundelete **NEED NIDEN INPUT**
```bash
# extundelete artefact --restore-all
```
after running extundelete a recovery folder was created.
the folder contained a lot of "data" file types.

there was a hint that the flag was somewhere inside..
Niden pointed me to the file ts8Uc0pmcYvxe
running strings on the file "RECOVERED_FILES/file_system/ts8Uc0pmcYvxe" revealed "JFIF" which is a header for a jpg image.
the header was however corrupt. 
to repair it I simply ran hexedit and added "FF D8 FF E0" at the start of the file.
this successfully repaired the image file and it contained a flag. 


* flag = flag{i_h@te_stupid_color$}

## Other resources (optional)



