from agents import Agent, Runner, function_tool, RunContextWrapper
import asyncio
from connection import config
from dataclasses import dataclass

@dataclass
class UserInfo:
    name: str
    uid: int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"User {wrapper.context.name} is 20 years old."

async def main():
    user_info = UserInfo(name="TEHREEM", uid=103)

    agent = Agent[UserInfo](
        name="Assistant",
        instructions="use 'fetch_user_age' tool and always only say exactly what the tool returns.",
        tools=[fetch_user_age]
    )

    result = await Runner.run(
        starting_agent=agent,
        input="What is the age of the user?",
        context=user_info,
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
