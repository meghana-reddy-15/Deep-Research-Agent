from openai import OpenAI
import yaml
import os

config_path = os.path.expandvars(
    r"%USERPROFILE%\.deep-research\config.yaml"
)

with open(config_path, encoding="utf-8") as f:
    config = yaml.safe_load(f)

client = OpenAI(
    api_key=config["llm"]["api_key"],
    base_url=config["llm"]["base_url"],
)

response = client.chat.completions.create(
    model=config["llm"]["model"],
    messages=[
        {
            "role": "user",
            "content": (
                'Reply ONLY with this JSON: '
                '{"thought":"test","action":"searxng_search",'
                '"action_input":{"query":"AI","limit":3}}'
            ),
        }
    ],
    temperature=0,
    max_tokens=200,
)

print("RESPONSE:", repr(response.choices[0].message.content))
print("FINISH:", response.choices[0].finish_reason)