from flask import Flask, json, request, abort, jsonify
from configInterface import *
from getDetails import *

app = Flask(__name__)

Params = [
]


################################################################################
# Name: config_loopback()
# Description: This function is used for configuring the loopback IP on the
#              network device
# Input Parameter: loopback ip
# Output Parameter: Returns params in json format
################################################################################
@app.route('/configloopback', methods=['POST'])
def config_loopback():
    if not request.json:
        print('Error while creating config')
        abort(400)
    param = {
        'ip': request.json['ip'],
    }
    Params.append(param)
    b = jsonify({'ip': param['ip']})
    content = request.get_json()
    ip = (content['ip'])
    name = (content['name'])
    if request.json['loopback'] == "create":
        print('Input received to create loopback')
        try:
            print('Posting interface details to create_interface function')
            create_interface(name, ip)
        except:
            abort(404)
        else:
            print('Loopback IP Created successfully')
            return "Loopback IP created"
    else:
        print('Failed to update params')
        abort(404)


################################################################################
# Name: delete_loopback()
# Description: This function is used for delete the loopback IP on the
#              network device
# Input Parameter: none
# Output Parameter: Returns status of the PNP configuration reset process
################################################################################
@app.route('/deleteloopback', methods=['POST'])
def delete_loopback():
    if not request.json:
        print('Error while deleting IP')
        abort(400)
    param = {
        'loopbacknum': request.json['loopbacknum'],
    }
    Params.append(param)
    b = jsonify({'loopbacknum': param['loopbacknum']})
    content = request.get_json()
    loopbacknum = (content['loopbacknum'])
    if request.json['loopback'] == "delete":
        print('Input received to delete loopback')
        try:
            print('Posting delete input to del_interface function')
            del_interface(loopbacknum)
        except:
            abort(404)
        else:
            print('Loopback IP deletion Successful')
            return "Loopback IP deleted"
    else:
        print('Failed to delete IP')
        abort(404)


################################################################################
# Name: get_details()
# Description: This function is used to retrieve the information about interface
# Input Parameter: NULL
# Output Parameter: Returns the received parameters in json format
################################################################################
@app.route('/getinterfaces', methods=['GET'])
def get_params():
    output = interface_details()
    print(output)
    return output


if __name__ == '__main__':
    app.run()
