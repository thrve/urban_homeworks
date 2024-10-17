#!/usr/bin/env python


import argparse
import os
import re
import signal
import subprocess as sp
import pexpect

username = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
con_ref = 'telnet: Unable to connect to remote host: Connection refused'


re_ip = re.compile(r'(:?(2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)$')
re_radio_ip = re.compile(r'10.240.(2[0-4]\d|25[0-5]|[1]?\d\d?).(2[0-4]\d|25[0-4]|[1]?\d\d?)')
re_hostname = re.compile(r'(:?\d\d-[A-Z]+-[A-Z]+\d+-[A-Z]+-\d$)')


parser = argparse.ArgumentParser(description='pseudo_telnet')
parser.add_argument('ip', type=str, help='IP address')
args = parser.parse_args()


def signal_handler(sig, frame):
    print('\r')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)


if not re.match(re_ip, args.ip) and not re.match(re_hostname, args.ip):
    print(f'{args.ip} is invalid value for ip addres.')
    exit(1)
else:
    status, result = sp.getstatusoutput(f'ping -c1 -w2 {args.ip}')
    if status != 1:
        print(f'The {args.ip} is unavailable.')
        exit(1)


if __name__ == '__main__':
    with pexpect.spawn(f'telnet {args.ip}') as telnet:
        if re.match(re_radio_ip, args.ip):
            telnet.interact()
        else:
            index = telnet.expect(['login', '[Uu]sername', 'User [Nn]ame:', con_ref])
            if index == 3:
                print(con_ref)
                exit(0)
            elif index == 0:
                telnet.sendline(username)
                telnet.expect('assword:')
                telnet.sendline(password)
                index_jun = telnet.expect(['}', '#'])  # for Juniper
                if index_jun == 0:
                    print('')
                    telnet.interact()
                else:
                    telnet.sendcontrol('j')  # for SNR
                    print('')
                    telnet.interact()
            else:
                telnet.sendline(username)
                telnet.expect('assword:')
                telnet.sendline(password)
                index_olt = telnet.expect(['reserved.', '>', '#'])
                if index_olt == 0:  # for OLT Huawei
                    telnet.expect('>')
                    telnet.sendline('enable')
                    telnet.expect('#')
                    telnet.sendline('undo interactive')
                    telnet.expect('#')
                    telnet.sendline('undo smart')
                    telnet.expect('#')
                    telnet.sendcontrol('j')
                    telnet.interact()
                else:
                    print('')
                    telnet.sendcontrol('j')
                    telnet.interact()



