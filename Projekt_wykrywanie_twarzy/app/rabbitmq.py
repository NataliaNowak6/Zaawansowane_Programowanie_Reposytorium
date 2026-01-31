import pika, json
from app.config import QUEUE_NAME

def publish_task(task: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=QUEUE_NAME,
        body=json.dumps(task),
        properties=pika.BasicProperties(delivery_mode=2)
    )

    connection.close()