import subprocess
import optparse

def get_argunment():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change it MAC address")
    parser.add_option("-m", "--mac", dest="New_mac", help="New_MAC address")
    (options, argunment) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info")
    elif not options.New_mac:
        parser.error("[-] please specify a new mac, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+]changing mac_address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_argunment()
change_mac(options.interface, options.New_mac)

