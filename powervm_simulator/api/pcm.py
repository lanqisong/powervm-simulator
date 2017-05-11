import flask

from powervm_simulator.api import app
from powervm_simulator.api import utils

@app.route('/rest/api/pcm/ManagedSystem/', methods=['GET'])
def list_pcm_managedSystem():
    resp = flask.Response(utils.read('event.xml')) 
    resp.headers['Content-Type'] = 'application/vnd.ibm.powervm.web+xml'
    return resp 

@app.route('/rest/api/pcm/ManagedSystem/<string:id>/preferences', methods=['GET', 'POST'])
def get_preferences(id):
    resp = flask.Response(utils.read('pcm_pref.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 

@app.route('/rest/api/pcm/ManagedSystem/<string:id>/RawMetrics', methods=['GET'])
def list_raw_metrics(id):
    resp = flask.Response(utils.read('pcm_pref.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 


@app.route('/rest/api/pcm/ManagedSystem/<string:id>/RawMetrics/LongTermMonitor', methods=['GET'])
def list_long_term_monitors(id):
    resp = flask.Response(utils.read('ltm_feed2.xml')) 
    resp.headers['Content-Type'] = 'application/atom+xml'
    return resp 


@app.route('/rest/api/pcm/ManagedSystem/<string:id>/RawMetrics/LongTermMonitor/<string:ltm_id>', methods=['GET'])
def get_long_term_monitor(id, ltm_id):
    resp = flask.Response(utils.read('phyp_pcm_data.json')) 
    resp.headers['Content-Type'] = 'application/json'
    return resp 
