run_example example model="deepseek/deepseek-v4.1-flash":
    model={{ quote(model) }}; PYDANTIC_AI_MODEL="openrouter:${model#model=}" uv run --env-file .env {{ quote("examples/pydantic_ai_examples/" + example + ".py") }}
