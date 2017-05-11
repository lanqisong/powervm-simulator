import flask

from powervm_simulator.api import app
from powervm_simulator.api import utils


@app.route('/rest/api/uom/ManagedSystem', methods=['GET'])
def list_managedSystem():
    resp = flask.Response(utils.read('event.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/VirtualIOServer', methods=['GET'])
def list_vios_servers():
    resp = flask.Response(utils.read('vios_feed.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/LogicalPartition', methods=['GET'])
def list_lpars():
    resp = flask.Response(utils.read('lpar.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/jobs/<string:id>', methods=['DELETE'])
def delete_job(id):
    resp = flask.Response(utils.read('job_response_power_on.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/ManagedSystem/<string:id>', methods=['GET'])
def get_ms(id):
    resp = flask.Response(utils.read('managedsystem_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/ManagedSystem/<string:id>/VirtualIOServer', methods=['GET'])
def list_ms_vios(id):
    resp = flask.Response(utils.read('vios_feed.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/ManagedSystem/<string:id>/VirtualSwitch', methods=['GET'])
def list_ms_vswitch(id):
    resp = flask.Response(utils.read('vswitch_feed.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/ManagedSystem/<string:id>/VirtualSwitch/<string:vswitch_id>', methods=['GET'])
def get_ms_vswitch(id, vswitch_id):
    resp = flask.Response(utils.read('vswitch_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 


@app.route('/rest/api/uom/ManagedSystem/<string:id>/VirtualIOServer/<string:vios_id>', methods=['GET'])
def get_ms_vios(id, vios_id):
    resp = flask.Response(utils.read('vios_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/ManagedSystem/<string:id>/VirtualIOServer/<string:vios_id>', methods=['POST', 'PUT'])
def create_ms_vios(id, vios_id):
    resp = flask.Response(utils.read('vios_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp


@app.route('/rest/api/uom/ManagedSystem/<string:id>/LogicalPartition', methods=['GET'])
def list_ms_lpars(id):
    resp = flask.Response(utils.read('lpar.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/ManagedSystem/<string:id>/LogicalPartition', methods=['POST', 'PUT'])
def create_ms_lpar(id):
    resp = flask.Response(utils.read('lpar_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 


@app.route('/rest/api/uom/ManagedSystem/<string:id>/LogicalPartition/<string:lpar_id>', methods=['GET'])
def get_ms_lpar(id, lpar_id):
    resp = flask.Response(utils.read('lpar_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/VirtualIOServer/<string:id>', methods=['GET'])
def get_vios(id):
    resp = flask.Response(utils.read('vios_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/VirtualIOServer/<string:id>/VolumeGroup', methods=['GET'])
def list_ms_vios_vg(id):
    resp = flask.Response(utils.read('volume_group_feed.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/VirtualIOServer/<string:id>/VolumeGroup/<string:vg_id>', methods=['GET'])
def get_ms_vios_vg(id, vg_id):
    resp = flask.Response(utils.read('volume_group.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/VirtualIOServer/<string:id>/VolumeGroup/<string:vg_id>', methods=['POST'])
def create_ms_vios_vg(id, vg_id):
    resp = flask.Response(utils.read('volume_group.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 


@app.route('/rest/api/uom/LogicalPartition/<string:id>', methods=['GET'])
def get_uom_lpar(id):
    resp = flask.Response(utils.read('lpar_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>', methods=['DELETE'])
def delete_uom_lpar(id):
    resp = flask.Response(utils.read('lpar_entry.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>/quick/PartitionState', methods=['GET'])
def get_uom_lpar_state(id):
    resp = flask.Response(utils.read('partition_state.json')) 
    resp.headers['Content-Type'] = 'application/json'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>/quick/PartitionID', methods=['GET'])
def get_uom_lpar_id(id):
    resp = flask.Response('{"PartitionID": 1}') 
    resp.headers['Content-Type'] = 'application/json'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>/ClientNetworkAdapter', methods=['GET', 'PUT'])
def list_uom_lpar_cnas(id):
    resp = flask.Response(utils.read('cna_feed.xml'))
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>/ClientNetworkAdapter/<string:cna_id>', methods=['GET', 'PUT'])
def get_uom_lpar_cna(id, cna_id):
    resp = flask.Response(utils.read('cna_entry.xml'))
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>/do/PowerOn', methods=['GET'])
def get_uom_lpar_power_on(id):
    resp = flask.Response(utils.read('job_request_power_on.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/uom/LogicalPartition/<string:id>/do/PowerOn', methods=['PUT'])
def do_uom_lpar_power_on(id):
    resp = flask.Response(utils.read('job_response_power_on.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

