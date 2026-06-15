import json
import logging

import paho.mqtt.client as mqtt
from server_rest.mqtt.handlers import handler_weather_update

logger = logging.getLogger(__name__)

HANDLER_REGISTRY = {
    # topic(namespace/domain): handler_function
    "home/weather": handler_weather_update
}
TOPIC_NAMESPACE = "home/#"


class MQTTSubscriber:
    """MQTT Subscriber that connects to a broker, subscribes to topics, and routes messages to handlers.

    Topics are expected to follow the format: <namespace>/<domain>/<device_id>
     - namespace: e.g. "home"
     - domain: e.g. "weather"
     - device_id: e.g. "device123"
    """

    def __init__(self, host: str, port: int, client_id: str, username: str = None, password: str = None):
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=client_id)
        self.host = host
        self.port = port
        self.username = username
        self.password = password

        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message

        self.client.username_pw_set(username, password)

    def start(self):
        logger.info("Connecting to MQTT broker")

        self.client.connect(self.host, self.port, keepalive=60)

        self.client.loop_start()

    def stop(self):
        logger.info("Stopping MQTT subscriber")

        self.client.loop_stop()
        self.client.disconnect()

    def on_connect(self, client, userdata, flags, reason_code, properties):
        logger.info(f"Connected to MQTT broker. Reason code={reason_code}")
        client.subscribe(TOPIC_NAMESPACE)

    def on_disconnect(self, client, userdata, disconnect_flags, reason_code, properties):
        logger.warning(f"Disconnected from MQTT broker. Reason={reason_code}")

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())

            logger.debug(f"Topic={msg.topic} Payload={payload}")

            self.route_message(topic=msg.topic, payload=payload)

        except Exception:
            logger.exception("Failed processing MQTT message")

    def _topic_parser(self, topic: str) -> tuple[str, str, str]:
        topic_parts = topic.split("/")
        if len(topic_parts) < 3:
            return None, None, None
        namespace, domain, device_id = topic_parts[0], topic_parts[1], topic_parts[2]
        return namespace, domain, device_id

    def route_message(self, topic: str, payload: dict):
        namespace, domain, device_id = self._topic_parser(topic)

        if not namespace or not domain or not device_id:
            logger.warning(f"Received message with invalid topic format: {topic}")
            return

        handler = HANDLER_REGISTRY.get(f"{namespace}/{domain}")
        if handler:
            handler(device_id, payload)
        else:
            logger.warning(f"No handler registered for topic: {topic}")
