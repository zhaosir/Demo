import pika
import time
from pika.credentials import PlainCredentials

credentials = PlainCredentials(username='test', password='test')
parameters = pika.ConnectionParameters(host = '192.168.199.232', port=5672, credentials=credentials )
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue = 'task_queue_test' , durable = True )
print ' [*] Waiting for messages. To exit press CTRL+C'
 
def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)
        time.sleep( body.count( '.' ) )
        print " [x] Done"
        ch.basic_ack(delivery_tag = method.delivery_tag)
          
channel.basic_qos(prefetch_count = 1 )
channel.basic_consume(callback, queue = 'task_queue')
channel.start_consuming()
