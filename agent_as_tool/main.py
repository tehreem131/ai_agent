from agents import Agent, Runner
from connection import config
#define individual transloter agents

italian_agent = Agent(
    name="Italian Translator",
    instructions="Italian Translator",
)

spanish_agent = Agent(
    name="Spanish Translator",
    instructions="Translate any english text into spanish.",
)

french_agent = Agent(
    name="French Translator",
    instructions="Translate any english text into french.",
)




