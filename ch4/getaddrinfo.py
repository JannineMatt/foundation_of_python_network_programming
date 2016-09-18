from socket import getaddrinfo
import socket


def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )


def get_addr_info_print(obj):
    # object(family, sockettype, proto, '', ('::', 53, 0, 0))
    # family(1 AF_UNIX, 2 AF_INET, 10 AF_INET)
    # sockettype(SOCK_STREAM=1，SOCK_DGRAM=2，SOCK_RAW=3)
    # proto(IPPROTO_TCP=6, IPPTOTO_UDP=17)
    families = get_constants('AF_')
    types = get_constants('SOCK_')
    protocols = get_constants('IPPROTO_')

    family, socktype, proto, canonname, sockaddr = obj
    print('Family        :', families[family])
    print('Type          :', types[socktype])
    print('Protocol      :', protocols[proto])
    print('Canonical name:', canonname)
    print('Socket address:', sockaddr)
    print()

'''
common web prot service
  http : 80
 https : 443
   ftp : 21
gopher : 70
  smtp : 25
  imap : 143
 imaps : 993
  pop3 : 110
 pop3s : 995
'''

print('==========get http service==========')
for resp in getaddrinfo(None, 'http', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    get_addr_info_print(resp)


print('==========get dns service==========')
for resp in getaddrinfo(None, 53, 0, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE):
    get_addr_info_print(resp)

print('==========get local stmp service==========')
for resp in getaddrinfo('localhost', 'smtp', 0, socket.SOCK_STREAM, 0):
    get_addr_info_print(resp)
