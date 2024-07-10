import os

from griptape.drivers import GriptapeCloudEventListenerDriver, GriptapeCloudObservabilityDriver
from griptape.events import EventListener
from griptape.structures import Agent
from griptape.observability import Observability

from sleeper.tool import Sleeper

observability_driver = GriptapeCloudObservabilityDriver(service_name="example-observable-structure")
event_listener_driver = GriptapeCloudEventListenerDriver(api_key=os.environ["GT_CLOUD_API_KEY"])

with Observability(observability_driver=observability_driver):
    agent = Agent(
        event_listeners=[EventListener(driver=event_listener_driver)],
        tools=[Sleeper()],
    )
    agent.run("Sleep for 3 seconds, then output an animal sound (in text)")
