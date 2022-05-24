import logging
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter
 
# Create the logger and set it's logging level
logger = logging.getLogger("logstash")
logger.setLevel(logging.DEBUG)
# Create the handler
handler = AsynchronousLogstashHandler(
    host='727a3edb-ab46-4ffb-915a-50e2c5ef1e15-ls.logit.io', 
    port=27231, 
    ssl_enable=False, 
    ssl_verify=False,
    database_path='')
# Here you can specify additional formatting on your log record/message
formatter = LogstashFormatter()
handler.setFormatter(formatter)

# Assign handler to the logger
logger.addHandler(handler)