# BITSCTF : 20

**Solver:** niden
**Category:** misc
**Points:** 20
**Description:**

Follow your heart, for it leads you straight to the answer.

## Writeup

Opened the file and it was an `XML` file with various latitude and longitudes on it.

Digging around google it bright me to a couple websites that convert `XML` to `KMZ` which you can import into google maps.

Using the websites below. I converted the `XML` to `KMZ` and imported it into google maps.

The flag is the first letter of each of the countries listed on google maps.

Flag = `BITSCTF{map_the_hack}`

## Other resources

* http://www.urbanhikr.com/how-to-import-gpx-into-google-maps/
* http://www.gpsvisualizer.com/map_input?form=googleearth
