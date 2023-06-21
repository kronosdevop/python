import openai

openai.api_key = "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"


def get_current_weather(location, unit="fahrenheit"):
    return {
        "location": location,
        "temperature": "72",
        "unit": unit,
        "forecast": ["sunny", "windy","stormy","chilly","rainy"],
    }


def run_conversation():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What's the weather like in la?"}
    ]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='\n'.join([f"{msg['role']}: {msg['content']}" for msg in messages]) + "\n"
                f"function: get_current_weather\n"
                f"location: la\n",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
        frequency_penalty=0,
        presence_penalty=0
    )
    generated_text = response["choices"][0]["text"]
    messages.append({"role": "assistant", "content": generated_text})
    return messages




print(run_conversation())