import json 
from datetime import datetime
import os
from utils.evaluate import evaluate_text

LOG_FILE = "logs/toxicity_logs.json" 

def log_result(data):
    """
    This function saves the result of each evaluation:

    1. Ensures that the `logs/` folder exists.
    2. Opens the log file in **append mode**.
    3. Converts the result dictionary to a JSON string and writes it as a new line.
    """
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")

if __name__ == "__main__":
    while True:
        text=input("Please enter text or type 'quit': ")
        if text.lower() == "quit":
            break

        result = evaluate_text(text)
        result["timestamp"] = datetime.now().isoformat()

        # Extract and print toxicity score
        print(f"Toxicity Score: {result['toxicity_score']:.2f}")
        if result["flagged"]:
            print("Input text is considered toxic - audit for further evaluation")
        else:
            print("input text is safe")

        log_result(result) # log and store result 