import pika, json
from app.services.detector import detect
from app.storage import save_result, save_status
from app.config import QUEUE_NAME

def callback(ch, method, properties, body):
    task = json.loads(body)
    task_id = task["task_id"]

    save_status(task_id, "processing")

    count, image = detect(task["source"], task_id)
    save_result(task_id, count, image)

    ch.basic_ack(method.delivery_tag)

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME, durable=True)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
channel.start_consuming()