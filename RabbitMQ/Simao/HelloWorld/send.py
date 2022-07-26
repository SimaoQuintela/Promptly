import pika

# Getting a connection 
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
#


# Creating a queue
channel.queue_declare(queue='hello')

# publish into the queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

print(" [x] Sent 'Hello World!'")

# Flush the network buffers
connection.close()