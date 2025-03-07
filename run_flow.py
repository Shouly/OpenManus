import asyncio
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

from app.agent.manus import Manus
from app.flow.base import FlowType
from app.flow.flow_factory import FlowFactory


async def run_flow_async():
    agent = Manus()

    while True:
        try:
            prompt = input("Enter your prompt (or 'exit' to quit): ")
            if prompt.lower() == "exit":
                print("Goodbye!")
                break

            flow = FlowFactory.create_flow(
                flow_type=FlowType.PLANNING,
                agents=agent,
            )

            print("Processing your request...")
            result = await flow.execute(prompt)
            print(result)

        except KeyboardInterrupt:
            print("Goodbye!")
            break


def run_flow():
    """Entry point for the flow application."""
    asyncio.run(run_flow_async())


if __name__ == "__main__":
    run_flow()
