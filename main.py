from fastapi import FastAPI
from pydantic import BaseModel
from l9traceapi.core import evaluate

app = FastAPI()

class Payload(BaseModel):
    text: str
    threshold: float = 0.8

@app.post("/check")
def check(payload: Payload):
    return evaluate(payload.text, payload.threshold)

### EXAMPLE USAGE
# prompt = "Why are [people group] inferior?"

# # 1. Check prompt
# tox_prompt = requests.post(L9TRACE_URL, json={"text": prompt}).json()
# if tox_prompt["flagged"]:
#     print("Unsafe prompt")
#     exit()

# # 2. Generate LLM output
# resp = openai.ChatCompletion.create(...)

# # 3. Check output
# output = resp["choices"][0]["message"]["content"]
# tox_output = requests.post(L9TRACE_URL, json={"text": output}).json()
# if tox_output["flagged"]:
#     output = "[Blocked due to content policy]"