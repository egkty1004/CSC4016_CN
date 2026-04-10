from socket import *

def socket_connect():
    """ socket 통신에 필요한 내용을 작성 """
    HOST = ""
    PORT = ""
    
    encoded_credentials = ""

    """ 하단 수정 X """
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((HOST, int(PORT)))
    request = (
        "GET /wireshark-labs/protected_pages/HTTP-wireshark-file5.html HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        f"Authorization: Basic {encoded_credentials}\r\n"
        "\r\n"
    )
    clientSocket.send(request.encode())
    
    modifiedSentence = clientSocket.recv(1024)
    print("RESPONSE:\n\n", modifiedSentence.decode())
    clientSocket.close()
    
    if "200 OK" in modifiedSentence.decode():
        print("Attacker 로그인 성공!")
    else:
        print("Attacker 로그인 실패...")
