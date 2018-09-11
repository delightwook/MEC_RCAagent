from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from horizon.utils.memoized import memoized
# from openstack_dashboard.api import base
from keystoneauth1.identity.generic.token import Token
from keystoneauth1.session import Session
from keystoneclient import client as ksclient
from vitrageclient import client as vitrage_client


from keystoneauth1.identity import v3

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

@memoized
def vitrageclient(request, password=None):
    # endpoint = base.url_for(request, 'identity')
    # token_id = request.user.token.id
    # tenant_name = request.user.tenant_name
    """
    curl -sd '{"auth":{"passwordCredentials":{"username": "admin", "password": "root"}}}'
    -H "Content-type: application/json" http://192.168.11.101:5000/v2.0/tokens | python -m json.tool
    """
    endpoint = 'http://192.168.11.101/identity'



    token_id = ""
    tenant_name = 'admin'
    project_domain_id = 'default'
    auth = Token(auth_url=endpoint, token=token_id,
                 project_name=tenant_name,
                 project_domain_id=project_domain_id)
    session = Session(auth=auth, timeout=600)
    return vitrage_client.Client('1', session)
#
# def get_Resource(request, all_tenants='false'):
#     resource = vitrageclient(request).resource.list()
#     return resource

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
    """
    Vitage RCA Data Get Function

    """

    auth= v3.Password(user_domain_name = "default",username = "admin",password="root",project_domain_name="default",
                     project_name="admin",auth_url = "http://192.168.11.101/identity")
    session = Session(auth=auth, timeout=600)
    x = vitrage_client.Client('1', session)
    # keystone = ksclient.Client(auth_url="http://192.168.11.101/identity",username="admin",
    #                            password="root", tenant_name="admin")

    print("############## keystone", auth)
    print("############## keystone", session)
    print("############## keystone", x)


    # get_Resource(request)
    #
    #
    # url = 'curl -i -H \"Content-Type: application/json\" -X POST -d ' + '\''+'{"Hello":"hi"}' + '\'' + \
    #       ' http://192.168.11.11:7071/MECrcaserver'
    # os.system(url)
    threading.Timer(second,get_rca,[second]).start()

if __name__ == '__main__':
    app.run(host='127.0.0.1',port = 7071,debug = True)