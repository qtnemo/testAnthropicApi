import anthropic
from dotenv import load_dotenv

load_dotenv() # load env vars from .env (api key, etc)
client = anthropic.Anthropic() # read api key from env by default.

response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is the capital of Texas."}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print("Exit code: 0")
exit(0)