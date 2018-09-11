from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
import os
import threading
end = False
app = Flask(__name__)
api = Api(app)

"""
Test Code
url = 'curl -i -H \"Content-Type: application/json\" -X POST -d ' + '\'' + total_request + '\'' + ' http://127.0.0.1:5050/Test'
 curl -i -H "Content-Type: application/json" -X GET http://127.0.0.1:7070/MECrcaserver
os.system(url)
"""
@app.route('/MECrcaagent',methods=['GET','POST'])
def rca_server():

    # if not request.json:
    #     abort(400)
    # data = request.json
    # print(data)
    # api_handler.start_action(data['action'],data)
    get_rca(5.0)

    return ''
def get_rca(second =  5.0):
    global end
    if end:
        return
    url = 'curl -i -H \"Content-Type: application/json\" -X POST -d ' + '\''+'{"Hello":"hi"}' + '\'' + \
          ' http://192.168.11.11:7071/MECrcaserver'
    os.system(url)
    threading.Timer(second,get_rca,[second]).start()

if __name__ == '__main__':
    app.run(host='127.0.0.1',port = 7071,debug = True)