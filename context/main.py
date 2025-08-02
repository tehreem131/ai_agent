from agents import Agent, Runner
from connection import config
import asyncio

#sirf LLm context: instructions de raha hai agent ko
agent = Agent(
    name="PoliteAssistant",
    instructions="User ka naam tehreem hai. Hamesha polite raho our har jawab mai 'TEHREEM' keh kar bulao."
)

async def main():
    result = await Runner.run(
        starting_agent=agent,
        input="Who is the founder of Pakistan?",
        run_config=config # yai bhi LLM context hai
    )

    print(result.final_output)

if __name__ =="__main__":
    asyncio.run(main())