from services.llm_service import ai_summarizer
from resources.llm_properties import model
from resources.summaizer_prompt import prompt
import time

print("--------AI Summarizer--------\n")
time.sleep(0.05)
print("Type exit to quit.\n")

while True:
    input_text = input("Provide your text to summarize: ")
    if input_text.lower() == "exit":
        break
    try:
        
        message = [
            {
                "role" : "system",
                "content" : prompt
            },
            {
                "role" : "user",
                "content" : input_text
            }
        ]
        ai_summarizer(messages=message, model=model)
    except Exception as e:
        print(e)
