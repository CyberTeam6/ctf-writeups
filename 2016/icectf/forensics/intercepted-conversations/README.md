# IceCTF-2016 : intercepted-conversations-110

**Category:** forensics
**Points:** 110
**Description:**

This traffic was picked up by one of our agents. We think this might be a conversation between two elite hackers that we are investigating. Can you see if you can analyze the data? intercept.pcapng

## Writeup

So opening the intercept.pcapng in Wireshark showed me that this was a packet capture of some sort of USB device. But what type of device? One of my pitfalls was looking at the “DEVICE DESCRIPTOR” field too early in the pcap. I spent many days trying to find the flag with using this information. Instead of getting a solid overview of the entire pcap I focused (incorrectly) on this.

idVendor: Ericsson Business Mobile Networks BV (0x0bdb)
All this was, was that the laptop that the designer used happened to have when he was creating this. Anyways, after pulling my head out of my ass I decided to look at the host field in Wireshark and see if anything else interesting was being initialized. Specifically any sort of input device. After a bit of searching I was able to find a solid input device.

idProduct: Kinesis Advantage PRO MPC/USB Keyboard (0x0007)
That sounds more like it. Before this, I have never analyzed  a USB pcap, but since it is a keyboard, we are probably hunting for key strokes. I used my best friend google and was given an amazing blog post that outlined how he solved a CSAW 2012 challenge that was similar.

So after taking the time to fully digest that blog post I was ready to get the “LEFTOVER CAPTURE DATA” field in Wireshark and see if we can match everything. I took Hexter’s Wireshark expression and modified to get rid of some of the pcap’s empty values

((usb.transfer_type == 0x01) && (frame.len == 72)) && !(usb.capdata == 00:00:00:00:00:00:00:00) && !(usb.capdata == 20:00:00:00:00:00:00:00)&& !(usb.capdata == 02:00:00:00:00:00:00:00)
Once I used this I had a very clear picture the hex bite codes for the key presses.


I took each value starting with 0x0a and placed it into a file so I could start looking to identify the key strokes. Again taking a look at Hexstr’s post post usb.org maintains updated keyboard layout tables. Here on page 53.

So instead of being fancy and writing a script, I just went ahead and did it by hand and was rewarded with this output

GIDIKY{,J0_P1V3;_X,3O7T_4LT,4T5}

Well, it has the same layout as the flag, but it is definitely not a flag. So after trying to run it though some cipher solving websites I didn’t find anything. Then I though maybe because the keyboard is USB 3.0 that is had a different HID table. All of which I came up with nothing.

So after I slept on it, I thought that someone who has a specialized keyboard like that may possibly use a different keyboard layout.

I visited Will’s Qwerty to Dvorak website and placed the output and was given

ICECTF?wH0{L1K3s{Qw3R7Y{4NYw4Y5+
I just changed the format to the standard flag format and was rewarded with 115 pts!

* Flag = IceCTF{wH0_L1K3s_Qw3R7Y_4NYw4Y5}



