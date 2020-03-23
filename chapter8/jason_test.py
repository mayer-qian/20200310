import json
interface = '{"name": "eth1/1", "ipaddress": "172.16.100.1", "netmask": "255.255.255.0"}'
interface_dict = json.loads(interface)
print(interface_dict.get("name"))
print(interface_dict.get("ipaddress"))
print(interface_dict)
#print(interface["name"])

routers = {"routers": [{"name": "R1", "ip": "10.1.1.1"}, {"name": "R2", "ip": "10.1.1.2"}]}
routers_str = json.dumps(routers)
print(routers_str)