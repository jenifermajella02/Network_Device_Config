# Network_Device_Config
This project sets up network device to interact with using python  

#Pre-requsie:
1. Python
2. Flask
3. ncclient
4. netmiko

#LIST OF APIS USED:
1) To create a interface
    POST:  /configloopback 
    curl command: curl -X POST http://localhost:5000/configloopback -H "Content-Type: application/json" -d '{"ip": 123456, "name": "sample"}'
2) To delete a interface
    POST:  /deleteloopback
    curl command: curl -X POST http://localhost:5000/deleteloopback -H "Content-Type: application/json" -d '{"loopback": "delete"}'
3) To get interface details
    GET:   /getinterfaces
    curl command: curl -X GET http://localhost:5000/getinterfaces
