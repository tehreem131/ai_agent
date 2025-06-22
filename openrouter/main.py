from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

#load .env file and get API key
load_dotenv()
openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# Check if the API key is present; if not, raise an error
if not openrouter_api_key:
    raise ValueError("OPENROUTER_API_KEY is not set. Please ensure it is defined in your .env file.")

#setup openrouter clint (like openai but via openRouter)
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

#choose any openrouter-supported motel
model = OpenAIChatCompletionsModel(
    model="google/gemini-2.0-flash-exp:free ", #Example model, replace if needed
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name = "Writer agent",
    instructions = "you are a writer agent. Generate storys, poems, essay etc."

)

response = Runner.run_sync(
agent,
input = "write a sort essay on Quaid-e-azam in simple english",
run_config = config
)

print(response)
 

