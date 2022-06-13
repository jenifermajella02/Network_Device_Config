from flask import Flask, json, request, abort, jsonify
import logging
#import logframework

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
        logging.info('Error while creating config')
        abort(400)
    param = {
        'ip': request.json['ip'],
        #'certificate': request.json.get('certificate', "")
    }
    Params.append(param)
    b=jsonify({'ip': param['ip']})
    content = request.get_json()
    ip_value = (content['ip'])
    logging.info('IP VALUE: %s', ip_value)
    if (ip_value == Params[0]['ip']):
       print("success")
       logging.info('Updated params')
       logging.info('Params= %s', Params)
       try:
          logging.info('Posting ip Config to ipconfig function')
          print("success")
	  #loopback_config()  function call here
       except:
          abort(404)
       else:
          logging.info('Loopback IP Configuration Successful')
          return jsonify({'param': param}), 201
    else:
       logging.error('Failed to update params')
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
        logging.info('Error while deleting IP')
        abort(400)
    if request.json['loopback'] == "delete" :
       logging.info('Input received to delete loopback')
       print("del success")
       try:
          logging.info('Posting delete input to ipdelete function')
          print("del success")
	  #loopback_del()  function call here
       except:
          abort(404)
       else:
          logging.info('Loopback IP deletion Successful')
          return "Loopback IP deleted"
    else:
       logging.error('Failed to delete IP')
       abort(404)

################################################################################
# Name: get_details()
# Description: This function is used to retrieve the information about interface
# Input Parameter: NULL
# Output Parameter: Returns the received parameters in json format
################################################################################
@app.route('/getinterfaces', methods=['GET'])
def get_params():
    #interface_details() function call here
    return jsonify({'Interfaces': Params})


if __name__ == '__main__':
    app.run()
