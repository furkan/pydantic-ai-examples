"""Simple example of using Pydantic AI to construct a Pydantic model from a text input.

Run with:

    uv run -m pydantic_ai_examples.pydantic_model
"""

import os
from pathlib import Path
from uuid import uuid4

import mlflow
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.capabilities import Caching

mlflow.set_tracking_uri("http://127.0.0.1:5050")
mlflow.set_experiment(Path(__file__).stem)
mlflow.pydantic_ai.autolog()


class MyModel(BaseModel):
    city: str
    country: str


model = os.getenv("PYDANTIC_AI_MODEL", "openai:gpt-5.2")
print(f"Using model: {model}")
agent = Agent(model, output_type=MyModel, capabilities=[Caching()])

if __name__ == "__main__":
    session_id = str(uuid4())

    with mlflow.tracing.context(session_id=session_id):
        result = agent.run_sync("The windy city in the US of A.")
        print(result.output)
        print(result.usage)
