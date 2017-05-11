import flask

from powervm_simulator.api import app
from powervm_simulator.api import utils


@app.route('/rest/api/web/Logon', methods=['PUT'])
def logon():
    resp = flask.Response(utils.read('logon_file.xml'))
    resp.headers['X-MC-Type'] = 'PVM'
    resp.headers['Content-Type'] = 'application/vnd.ibm.powervm.web+xml'
    return resp


@app.route('/rest/api/web/File', methods=['PUT'])
def create_file():
    resp = flask.Response(utils.read('file_entry.xml'))
    resp.headers['Content-Type'] = 'application/vnd.ibm.powervm.web+xml'
    return resp

@app.route('/rest/api/web/File', methods=['GET'])
def list_file():
    resp = flask.Response(utils.read('file.xml'))
    resp.headers['Content-Type'] = 'application/vnd.ibm.powervm.web+xml'
    return resp

#@app.route('/rest/api/web/File/<string:id>', methods=['GET', 'DELETE'])
#def get_file(id):
#    resp = flask.Response(utils.read('file_entry.xml'))
#    resp.headers['Content-Type'] = 'application/vnd.ibm.powervm.web+xml'
#    return resp

#@app.route('/rest/api/web/File/contents/<string:id>', methods=['PUT'])
#def get_file_content(id):
#    resp = flask.Response(utils.read('file_entry.xml'))
#    resp.headers['Content-Type'] = 'application/vnd.ibm.powervm.web+xml'
#    return resp
