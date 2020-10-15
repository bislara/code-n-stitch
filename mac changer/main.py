from macchanger import MacChanger

if __name__ == '__main__':
    mc = MacChanger()
    mac = mc.get_mac('eth0')
    cur_mac = mc.change_mac('eth0', input('enter the new mac address\n>>> '))
