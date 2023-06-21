import openai

openai.api_key = "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"


output = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
         "content": " give some good startup ideas which will generate over 1 billion in the next 5 years\
            also give me a script to picht that idea in front of sharktank judges\
                be confident in your answer"}
    ]
)

print(output)
