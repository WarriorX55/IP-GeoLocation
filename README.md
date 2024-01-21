# IP-GeoLocation

# usage: 
        ip-geolocation.py [-h] [-u URL] [-t IP] [-f DATFILE]

[*] IP Geolocation Tool

options:
  -h,         --help                 show this help message and exit
  -u URL,     --url URL              Locate an IP based on a URL
  -t IP,      --target IP            Locate the specified IP
  -f DATFILE, --dat DATFILE          Custom database filepath

we can use this script to find the approximate location of manyIP addresses!
Let’s start by viewing the help page so that we can see the formatting of the argparse module:

![help](https://github.com/WarriorX55/IP-GeoLocation/assets/141424663/370a2cdf-57c4-49cf-805b-c16c17f1a885)

We can see that the automatic installation is going through just fine 
(The database installation may take a minute, as it is quite a lot to download and decompress). 
Now we just have to wait for the query to complete:

![ip](https://github.com/WarriorX55/IP-GeoLocation/assets/141424663/b4ef7cc2-5e36-4e35-b1a8-7e3e8af01404)

We can see by the results of our query that it’s possible that Hackers-Arise is being hosted 
somewhere near Ashburn, Virginia. We did it!
