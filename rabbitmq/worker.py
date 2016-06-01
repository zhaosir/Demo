import pika
import time
from pika.credentials import PlainCredentials

credentials = PlainCredentials(username='test', password='test')
parameters = pika.ConnectionParameters(host = '192.168.199.232', port=5672, credentials=credentials )
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = 'task_queue_test' , durable = True )
print ' [*] Waiting for messages. To exit press CTRL+C'

msg_list = []

def do(ch, method, properties, body):
    global msg_list
    msg_list.append((ch, method, properties, body))
    if len(msg_list) >= 10:
        for _ch, _method, _properties, _body in msg_list:
            _ch.basic_ack(delivery_tag = _method.delivery_tag)
        msg_list = []

def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)
        time.sleep( body.count( '.' ) )
        print " [x] Done"
#        do(ch, method, properties, body)
        ch.basic_ack(delivery_tag = method.delivery_tag)
          
channel.basic_qos(prefetch_count = 10 )
channel.basic_consume(callback, queue = 'task_queue_test')
channel.start_consuming()
