# pydantic-ai-examples

pydantic ai examples, further opiniated with openrouter and mlflow integrations

---

`.env`:

```
OPENROUTER_API_KEY=sk***
```

---

Install `uv` and `just`, then sync dependencies:

```sh
uv sync
```

---

Run mlflow server
```
uvx mlflow server --host 127.0.0.1 --port 5050
```

---

Run an example by its filename without `.py`:

```sh
just run_example bank_support model=deepseek/deepseek-v4.1-flash
```

---

The runner loads `.env` and runs scripts from `examples/pydantic_ai_examples/`.
It sets `PYDANTIC_AI_MODEL` to `openrouter:<model>`, which `bank_support.py` uses.
Other examples must read `PYDANTIC_AI_MODEL` to use the selected model.
Omit `model=...` to use the default `deepseek/deepseek-v4.1-flash`:

```sh
just run_example bank_support
```
