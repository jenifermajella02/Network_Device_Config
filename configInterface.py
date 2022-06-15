from ncclient import manager

creation_rpc = '''
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
                <Loopback>
          <name>300</name>
          <ip>
            <address>
              <primary>
                <address>192.168.100.100</address>
                <mask>255.255.255.255</mask>
              </primary>
            </address>
          </ip>
        </Loopback>
      </interface>
    </native>
</config>
      '''
deletion_rpc = '''
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
          <Loopback xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" nc:operation="delete">
          <name>300</name>
          </Loopback>
      </interface>
    </native>
</config>
'''

with manager.connect(host="ios-xe-mgmt.cisco.com", port=830, username='developer', password='C1sco12345',hostkey_verify=False) as m:
  reply = m.edit_config(creation_rpc, target='running')
  print(reply)
  reply = m.edit_config(deletion_rpc, target='running')
  print(reply)

