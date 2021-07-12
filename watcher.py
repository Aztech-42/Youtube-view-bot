
import ipaddress
import time 
import webbrowser as wb
# initialize an IPv4 Address
ip = ipaddress.IPv4Address("192.168.1.1")
# print True if the IP address is global
print("Is global:", ip.is_global)

# print Ture if the IP address is Link-local
print("Is link-local:", ip.is_link_local)

# next ip address
ip = ipaddress.IPv4Address("192.168.1.1") + 1
print(ip)
# initialize an IPv4 Network
network = ipaddress.IPv4Network("192.168.1.0/24")
# get the network mask
print("Network mask:", network.netmask)
# get the broadcast address
print("Broadcast address:", network.broadcast_address)
# get the broadcast address
print("Broadcast address:", network.broadcast_address)
# iterate over all the hosts under this network
print("Hosts under", str(network), ":")
for host in network.hosts():
    print(host)

# get the supernet of this network
print("Supernet:", network.supernet(prefixlen_diff=1))
# tell if this network is under (or overlaps) 192.168.0.0/16
print("Overlaps 192.168.0.0/16:", network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))

while True:
    wb.open("https://youtu.be/Sxae-rfrmHc")
    time.sleep(3.5)

