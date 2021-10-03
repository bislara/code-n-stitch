import sys
import socket
import threading
import configparser as cfg
from queue import Queue


def get_ip(config):
	parser = cfg.ConfigParser()
	parser.read(config)
	return parser.get('creds', 'token')


def check_inp(info):
	check = False

	if info[0] == '1':
		check = ''.join(info[1].strip().split()).isdigit()
	elif info[0] == '2':
		tup = tuple(info[1].strip().split())
		if (len(tup) == 2) and (''.join(tup).isdigit()):
			low, high = tuple(map(int, tup))
			check = True if low <= high else False
	
	if check == False:
		print('Error in input, try again. Exiting program')
		sys.exit()

def get_inp():
	opt = input('1. Custom list\t\t\t2. Range\nEnter(1/2): ')

	if opt == '1':
		inp = input('Enter list of port numbers as space seperated integers: ')
		check_inp((opt, inp))
		port_list = tuple(map(int, inp.strip().split()))
	elif opt == '2':
		inp = input('Enter lower and upper bound as space seperated integers: ')
		check_inp((opt, inp))
		low, up = tuple(map(int, inp.strip().split()))
		port_list = tuple(i for i in range(low, up+1))
	
	return port_list


def create_queue(port_list):
	for port in port_list:
		queue.put(port)


def portscan(port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.1)
		sock.connect((target, port))
		return True
	except:
		return False


def execute():
	while not queue.empty():
		port = queue.get()
		if portscan(port):
			open_ports.append(port)
			print(f'Port {port} is open')


def thread(threads):
	thread_list = []

	for i in range(threads):
		thread = threading.Thread(target=execute)
		thread_list.append(thread)
	
	for thread in thread_list:
		thread.start()
	
	for thread in thread_list:
		thread.join()


if __name__ == '__main__':
	target = get_ip('/home/naman/Documents/python_files/ip_ad.cfg')
	# target = input('Enter IP address of host machine: ')
	queue = Queue()
	open_ports = []

	port_list = get_inp()
	ports = len(port_list)
	create_queue(port_list)
	thread(ports if ports < 500 else 500)

	if len(open_ports) == 0:
		print('There are no open ports on the host machine')
		sys.exit()
	print(f'Open ports are: {open_ports}')
