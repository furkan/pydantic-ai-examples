run_example example model="openai/gpt-6-luna":
    model={{ quote(model) }}; PYDANTIC_AI_MODEL="openrouter:${model#model=}" PYTHONPATH=examples uv run --env-file .env -m pydantic_ai_examples.{{example}}
