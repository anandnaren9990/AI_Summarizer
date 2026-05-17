import time

import requests as rq
import json
import resources.llm_properties as lp

def ai_summarizer(messages, model):
    try:
        payload = {
            "model" : model,
            "messages" : messages,
            "stream" : True
        }
        response = rq.post(lp.llm_chat_url, stream=True, json=payload, timeout=15)
        response.raise_for_status()
        for line in response.iter_lines():
            if not line:
                continue
            chunk = json.loads(line.decode("utf-8"))
            text = chunk.get("message", {}).get("content")
            print(text, end="", flush=True)
            time.sleep(0.05)
            if chunk.get("done") is True:
                print("")
                break
    except rq.exceptions.ConnectionError as e:
        print(f"Model is not responsive: {e}")
    except rq.exceptions.ConnectTimeout as e:
        print(f"Model took long time to respond: {e}")
    except rq.exceptions.HTTPError as e:
        print(f"Error establishing connection: {e}")
    except rq.exceptions.JSONDecodeError as e: 
        print(f"The response was not valid JSON: {e}")
    except rq.exceptions.RequestException as e:
        print(f"Some other request error happened: {e}")
    except Exception as e:
        print(f"Some other exception occured: {e}")