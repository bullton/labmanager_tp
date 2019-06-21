
import socket, time

def OpenPort(ip, port):
    """
        \xb4\xf2\xbf\xaa\xc4\xb3\xb8\xf6\xcd\xa8\xb5\xc0
        OpenPort(ip, port)
        \xba\xaf\xca\xfd\xb2\xce\xca\xfd\xa3\xbaip   \xc9\xe8\xb1\xb8\xb5\xc4IP\xb5\xd8\xd6\xb7
                  port    \xb6\xcb\xbf\xda\xba\xc5
        \xb7\xb5\xbb\xd8\xd6\xb5\xa3\xba  \xd6\xb4\xd0\xd0\xbd\xe1\xb9\xfb   0 \xd6\xb4\xd0\xd0\xb3\xc9\xb9\xa6\xa3\xbb
                           -1 \xd6\xb4\xd0\xd0\xca\xa7\xb0\xdc\xa3\xbb
                           -2 \xb2\xce\xca\xfd\xb4\xed\xce\xf3\xa3\xbb
        """
    clientsocket = None
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.settimeout(500)
        clientsocket.connect((ip, 4001))
        portnum = int(port)
        if portnum < 1 or portnum > 8:
            return -2
        portnum -= 1
        operatorcmd = '\x01\x05\x00' + chr(portnum) + '\xff\x00'
        crc = __crc16(operatorcmd, len(operatorcmd))
        operatorcmd = operatorcmd + chr(crc[0]) + chr(crc[1])
        clientsocket.sendall(operatorcmd)
        returncmd = clientsocket.recv(512)
        if returncmd != operatorcmd:
            clientsocket.close()
            return -1
        time.sleep(0.1)
        operatorcmd = '\x01\x02\x00' + chr(portnum) + '\x00\x01'
        crc = __crc16(operatorcmd, len(operatorcmd))
        operatorcmd = operatorcmd + chr(crc[0]) + chr(crc[1])
        clientsocket.sendall(operatorcmd)
        returncmd = clientsocket.recv(512)
        crc = __crc16(returncmd[:-2], len(returncmd) - 2)
        if crc[0] != ord(returncmd[4]) or crc[1] != ord(returncmd[5]):
            clientsocket.close()
            return -1
        clientsocket.close()
        if int(ord(returncmd[3])) == 1:
            return 0
        return -1
    except Exception as e:
        if clientsocket != None:
            clientsocket.close()
            return -1

    return


def ClosePort(ip, port):
    """
        \xb9\xd8\xb1\xd5\xc4\xb3\xb8\xf6\xcd\xa8\xb5\xc0
        ClosePort(ip, port)
        \xba\xaf\xca\xfd\xb2\xce\xca\xfd\xa3\xbaip   \xc9\xe8\xb1\xb8\xb5\xc4IP\xb5\xd8\xd6\xb7
                  port    \xb6\xcb\xbf\xda\xba\xc5
        \xb7\xb5\xbb\xd8\xd6\xb5\xa3\xba  \xd6\xb4\xd0\xd0\xbd\xe1\xb9\xfb   0 \xd6\xb4\xd0\xd0\xb3\xc9\xb9\xa6\xa3\xbb
                           -1 \xd6\xb4\xd0\xd0\xca\xa7\xb0\xdc\xa3\xbb
                           -2 \xb2\xce\xca\xfd\xb4\xed\xce\xf3\xa3\xbb
        """
    clientsocket = None
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.settimeout(500)
        clientsocket.connect((ip, 4001))
        portnum = int(port)
        if portnum < 1 or portnum > 8:
            return -2
        portnum -= 1
        operatorcmd = '\x01\x05\x00' + chr(portnum) + '\x00\x00'
        crc = __crc16(operatorcmd, len(operatorcmd))
        operatorcmd = operatorcmd + chr(crc[0]) + chr(crc[1])
        clientsocket.sendall(operatorcmd)
        returncmd = clientsocket.recv(512)
        if returncmd != operatorcmd:
            clientsocket.close()
            return -1
        time.sleep(0.1)
        operatorcmd = '\x01\x02\x00' + chr(portnum) + '\x00\x01'
        crc = __crc16(operatorcmd, len(operatorcmd))
        operatorcmd = operatorcmd + chr(crc[0]) + chr(crc[1])
        clientsocket.sendall(operatorcmd)
        returncmd = clientsocket.recv(512)
        crc = __crc16(returncmd[:-2], len(returncmd) - 2)
        if crc[0] != ord(returncmd[4]) or crc[1] != ord(returncmd[5]):
            clientsocket.close()
            return -1
        clientsocket.close()
        if int(ord(returncmd[3])) == 0:
            return 0
        return -1
    except Exception as e:
        if clientsocket != None:
            clientsocket.close()
            return -1

    return


def QueryPort(ip, port):
    """
        \xb2\xe9\xd1\xaf\xc4\xb3\xb8\xf6\xcd\xa8\xb5\xc0\xb5\xc4\xd7\xb4\xcc\xac
        QueryPort(ip, port)
        \xba\xaf\xca\xfd\xb2\xce\xca\xfd\xa3\xbaip   \xc9\xe8\xb1\xb8\xb5\xc4IP\xb5\xd8\xd6\xb7
                  port    \xb6\xcb\xbf\xda\xba\xc5
        \xb7\xb5\xbb\xd8\xd6\xb5\xa3\xba  0 - \xb9\xd8\xb1\xd5(OFF) 
                  1 - \xb4\xf2\xbf\xaa(ON)
                  -1  \xcd\xa8\xd0\xc5\xb4\xed\xce\xf3\xa3\xbb
                  -2  \xb2\xce\xca\xfd\xb4\xed\xce\xf3\xa3\xbb
        """
    clientsocket = None
    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.settimeout(500)
        clientsocket.connect((ip, 4001))
        portnum = int(port)
        if portnum < 0 or portnum > 8:
            return -2
        portnum -= 1
        operatorcmd = '\x01\x02\x00' + chr(portnum) + '\x00\x01'
        crc = __crc16(operatorcmd, len(operatorcmd))
        operatorcmd = operatorcmd + chr(crc[0]) + chr(crc[1])
        clientsocket.sendall(operatorcmd)
        returncmd = clientsocket.recv(512)
        crc = __crc16(returncmd[:-2], len(returncmd) - 2)
        clientsocket.close()
        if crc[0] != ord(returncmd[4]) or crc[1] != ord(returncmd[5]):
            return -1
        if int(ord(returncmd[3])) == 0:
            return 0
        if int(ord(returncmd[3])) == 1:
            return 1
        return -1
    except Exception as e:
        if clientsocket != None:
            clientsocket.close()
        return -1

    return


def __crc16(buffer, len):
    dwCRC16 = 65535
    crc = []
    for i in range(len):
        dwTemp = ord(buffer[i]) & 255
        dwCRC16 ^= dwTemp
        for j in range(8):
            if dwCRC16 & 1 != 0:
                dwCRC16 = dwCRC16 >> 1
                dwCRC16 = dwCRC16 ^ 40961
            else:
                dwCRC16 = dwCRC16 >> 1

    crc.append(dwCRC16 & 255)
    crc.append(dwCRC16 >> 8)
    return crc
# okay decompiling PB_V2.pyc
