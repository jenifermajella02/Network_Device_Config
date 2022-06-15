from ncclient import manager

global dry_run
dry_run = False


################################################################################
# Name: create_interface()
# Description: This function is used for configuring the loopback IP on the
#              network device
# Input Parameter: loopback ip,name
# Output Parameter: ok reply from device
################################################################################
def create_interface(name, ipvalue):
    creation_rpc = '''
   <config>
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
         <interface>
                   <Loopback>
             <name>%s</name>
             <ip>
               <address>
                 <primary>
                   <address>%s</address>
                   <mask>255.255.255.255</mask>
                 </primary>
               </address>
             </ip>
           </Loopback>
         </interface>
       </native>
   </config>
   '''
    rpc_msg = creation_rpc % (name, ipvalue)
    print(rpc_msg)
    if not dry_run:
        try:
            with manager.connect(host="ios-xe-mgmt.cisco.com", port=830, username='developer', password='C1sco12345',
                                 hostkey_verify=False) as m:
                reply = m.edit_config(rpc_msg, target='running')
                print(reply)
        except:
            print("Something went wrong")
        else:
            print("Created successfully")
    else:
        print('DRY_RUN enabled')
        print(rpc_msg)


################################################################################
# Name: del_interface()
# Description: This function is used for deleting the loopback IP on the
#              network device
# Input Parameter: name
# Output Parameter: ok reply from device
################################################################################
def del_interface(name):
    print(name)
    name = name
    deletion_rpc = '''
   <config>
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
         <interface>
             <Loopback xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="delete">
             <name>%s</name>
             </Loopback>
         </interface>
       </native>
   </config>
   '''

    rpc_msg = deletion_rpc % name
    print(rpc_msg)
    if not dry_run:
        try:
            with manager.connect(host="ios-xe-mgmt.cisco.com", port=830, username='developer', password='C1sco12345',
                                 hostkey_verify=False) as m:
                reply = m.edit_config(rpc_msg, target='running')
                print(reply)
        except:
            print("Something went wrong")
        else:
            print("Created successfully")
    else:
        print('DRY_RUN enabled')
        print(rpc_msg)
