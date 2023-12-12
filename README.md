# wifistrawberry
 This project draws inspiration from Airgeddon and Wifi Pineapple. It is designed as an evil twin attack tool, providing more information below.


------------------|TOS|------------------
If you are apprehended or encounter a failure, I disclaim any responsibility for your actions. This tool is created solely for educational purposes.
-------------|how to install|------------

||| git clone https://github.com/adgwfg/wifistrawberry |||-|
||| cd wifistrawberry |||----------------------------------|
||| python3 wifistrawberry |||-----------------------------|
-----------|options|----------------

        Options:

                -h : Display this help message

                -s : Start Evil Twin attack

                -p : Specify the password for the attack (optional)

                -e : Specify the ESSID for the attack (optional)

                -l : Specify the HTML login page for the attack (optional)

        Examples:

                python evil_twin.py -s -e mynetwork -p mypassword -l login.html

                python evil_twin.py -s -e mynetwork -l login.html

        Note: You may need to run this script with sudo depending on your permissions.

        Note: Before using this script, ensure your wireless interface is in monitor mode using 'airmon-ng start wlan0' (wlan0 is the interface name).
