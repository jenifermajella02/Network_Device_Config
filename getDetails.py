from netmiko import ConnectHandler

global dry_run
dry_run = False


################################################################################
# Name: interface_details()
# Description: This function is used for retrieving interface information from
#              network device
# Input Parameter: none
# Output Parameter: interface details from device
################################################################################
def interface_details():
    cisco1 = {
        "device_type": "cisco_ios",
        "host": "ios-xe-mgmt.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
    }
    # Show command that we execute.
    command = "show interfaces summary"
    if not dry_run:
        try:
            with ConnectHandler(**cisco1) as net_connect:
                output = net_connect.send_command(command)
            # Automatically cleans-up the output so that only the show output is returned
            print(output)
        except:
            print("Something went wrong")
        else:
            print("Displayed successfully")
            return output
    else:
        print('DRY_RUN enabled')
