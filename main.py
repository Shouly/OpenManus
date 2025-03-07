import asyncio

from app.agent.manus import Manus
from app.logger import logger


async def main_async():
    agent = Manus()
    while True:
        try:
            prompt = input("Enter your prompt (or 'exit' to quit): ")
            if prompt.lower() == "exit":
                logger.info("Goodbye!")
                break
            logger.warning("Processing your request...")
            await agent.run(prompt)
        except KeyboardInterrupt:
            logger.warning("Goodbye!")
            break


def main():
    """Entry point for the application."""
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
