# AlexCTF : 150

**Solver:** niden
**Category:** forensics
**Points:** 150
**Description:**

One of our agents managed to sniff important piece of data transferred transmitted via USB, he told us that this pcap file contains all what we need to recover the data can you find it ?

## Writeup

As the description states this is a USB pcap.

When analyzing USB pcaps I quickly filter out the useless packets with `usb.data_flag == "present (0)"` and start looking at the `Leftover Capture Data` field.

Knowing that this is a USB storage device I also sort by `packet length`. This gives me some interesting information.

Reviewing the packets from largest to smallest brings me to packet number `101`

The `Leftover Capture Data` for this packet looks like a `PNG` header. Extract the hex, open in an image viewer and we are rewarded with the flag.

![flag](https://github.com/nidens/ctf-writeups/blob/master/2017/alexctf/forensics/usb-probing/output.png)

Flag = `ALEXCTF{SN1FF_TH3_FL4G_OV3R_US8}`
