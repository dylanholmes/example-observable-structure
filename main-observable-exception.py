import os

from griptape.drivers import GriptapeCloudEventListenerDriver, GriptapeCloudObservabilityDriver
from griptape.events import EventListener
from griptape.rules import Rule
from griptape.structures import Agent
from griptape.observability import Observability

observability_driver = GriptapeCloudObservabilityDriver(service_name="example-observable-structure")
event_listener_driver = GriptapeCloudEventListenerDriver(api_key=os.environ["GT_CLOUD_API_KEY"])

with Observability(observability_driver=observability_driver):
    agent = Agent(
        rules=[Rule("Output one word")],
        event_listeners=[EventListener(driver=event_listener_driver)]
    )
    agent.run("Name an animal")

    raise Exception("Observable exception")
