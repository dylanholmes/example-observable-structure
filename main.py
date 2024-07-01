from griptape.drivers import GriptapeCloudObservabilityDriver
from griptape.rules import Rule
from griptape.structures import Agent
from griptape.observability import Observability

observability_driver = GriptapeCloudObservabilityDriver(service_name="example-observable-structure")

with Observability(observability_driver=observability_driver):
    agent = Agent(rules=[Rule("Output one word")])
    agent.run("Name an animal")

