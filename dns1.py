import socket
"""Take input as host name from user"""
ip=input("enter host name:")
addr1=socket.gethostbyname(ip)
print(addr1)
add=input("enter ip address:")
"""Gives IP address of host by its name."""
addr2=socket.gethostbyaddr(add)
print(addr2)




