import subprocess
import re


class MacChanger:
    def __init__(self):
        self.mac = ""

    def get_mac(self, interface):
        # linux command - sudo ifconfig <iface e.g:eth0>
        command = subprocess.run(["sudo", "ifconfig", interface],
                                 shell=False,
                                 capture_output=True)
        # capture shell output
        command_result = command.stdout.decode('utf-8')

        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        regex_obj = re.compile(pattern)
        # find a mac-address match obj from the shell output
        regex = regex_obj.search(command_result)

        # extract the mac-address from the match object
        current_mac = regex.group().split(" ")[1]
        self.mac = current_mac
        return self.mac

    def change_mac(self, interface, new_mac):
        print(f"[+] current mac address is {self.mac}")

        # shutdown the current intended interface
        command = subprocess.run(["sudo", "ifconfig", interface, "down"],
                                 shell=False,
                                 capture_output=True)
        # if error occurs, print it out to standard output
        print(command.stderr.decode('utf-8'))

        # change the mac-address
        command = subprocess.run(
            ["sudo", "ifconfig", interface, "hw", "ether", new_mac],
            shell=False,
            capture_output=True)
        # if error occurs, print it out to standard output
        print(command.stderr.decode('utf-8'))

        # fireup the interface
        command = subprocess.run(["sudo", "ifconfig", interface, "up"],
                                 shell=False,
                                 capture_output=True)
        # if error occurs, print it out to standard output
        print(command.stderr.decode('utf-8'))

        print(f"[+] updated MAC address is", self.get_mac(interface))

        return self.get_mac(interface)
