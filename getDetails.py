from netmiko import ConnectHandler

cisco1 = {
    "device_type": "cisco_ios",
    "host": "ios-xe-mgmt.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
}

# Show command that we execute
command = "show interfaces summary"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that only the show output is returned
print()
print(output)
print()


