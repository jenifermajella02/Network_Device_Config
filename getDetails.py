from netmiko import ConnectHandler

import constants


################################################################################
# Name: interface_details()
# Description: This function is used for retrieving interface information from
#              network device
# Input Parameter: none
# Output Parameter: interface details from device
################################################################################
def interface_details():
    cisco1 = {
        "device_type": constants.device_type,
        "host": constants.host,
        "username": constants.username,
        "password": constants.password,
    }
    # Show command that we execute.
    command = "show interfaces summary"
    if not constants.dry_run:
        try:
            with ConnectHandler(**cisco1) as net_connect:
                output = net_connect.send_command(command)
        except:
            print("Something went wrong")
        else:
            print("Displayed successfully")
            return output
    else:
        print('DRY_RUN enabled')
