from oslo_log import log
from powervm_simulator.api import app
from powervm_simulator.api import web
from powervm_simulator.api import uom
from powervm_simulator.api import pcm

LOG = log.getLogger(__name__)


def main():
    # Fabric use 'print', need to catch here
    #sys.stdout = LoggerWriter(LOG.info)
    #sys.stderr = LoggerWriter(LOG.warning)

    # Build and start the WSGI app
    host = 'localhost'
    port = 12080
    app.run(host=host, port=12080, debug=True)
    LOG.info("Serving on http://%(host)s:%(port)s",
             {'host': host, 'port': port})

if __name__ == '__main__':
    main()
