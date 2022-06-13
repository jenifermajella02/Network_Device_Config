from ncclient import manager
import xmltodict
import xml.dom.minidom

#####################################################################################
def interface_details():
   int_filter = '''
    <filter>
     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <interface>
       <GigabitEthernet>
        <name>2</name>
       </GigabitEthernet>
      </interface>
     </native>
    </filter>
   '''
m = manager.connect(host="10.0.0.1", port=830, username="cisco", password="cisco")
result = m.get_config('running', int_filter)
print(xml.dom.minidom.parseString(str(result)).toprettyxml())

#####################################################################################

