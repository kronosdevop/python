import openai

openai.api_key = "YOUR_API_KEY"

output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "give me a name for my business involving goat milk ice cream", "max_tokens": 64}
    ]
)

print(output)

