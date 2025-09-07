import os
import json
from kafka import KafkaConsumer
from config.config import KAFKA_HOST
import datetime


class Consumer:

    def __init__(self, topic):
        self.topic = topic
        self.consumer= self.get_consumer_events()
        self.event = None

    def get_consumer_events(self):
        """ create consumer object """
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=KAFKA_HOST,
            group_id='my-group',
            enable_auto_commit=True,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        return consumer


