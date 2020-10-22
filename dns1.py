import socket

ip=input("enter host name:")
addr1=socket.gethostbyname(ip)
print(addr1)
add=input("enter ip address:")
addr2=socket.gethostbyaddr(add)
print(addr2)




