from pprint import pprint
from kafka import KafkaProducer
from config.config import KAFKA_HOST
import json



class Producer:

    def __init__(self):
        self.producer = self.get_producer_config()

    def get_producer_config(self):
        """
        Creates and returns a KafkaProducer instance with recommended settings,
        including JSON serialization for messages and key conversion to bytes.
        """
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_HOST,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            key_serializer=lambda k: k.encode('utf-8') if isinstance(k, str) else k,
            acks='all',
            retries=5,
            enable_idempotence=True
        )
        return producer

    def publish_message(self, topic, message):
        """ publish_message to a specific topic """
        self.producer.send(topic, value=message)
        self.producer.flush()
        # self.producer.close(timeout=999999)


    def publish_message_with_key(self, topic, key, message):
        """ publish_message to a specific topic secure with key """
        self.producer.send(topic, key=key, value=message)

