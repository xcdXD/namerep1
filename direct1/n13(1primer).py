#region на нахождение наибольшего ip

from ipaddress import *

net = ip_network(f"146.180.173.153/255.192.0.0",strict=False)
print(net[-2])