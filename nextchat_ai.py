import openai

openai.api_key = "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"

prompt = "Once upon a time"
model = "text-davinci-003"
response = openai.Completion.create(
  engine=model,
  prompt=prompt,
  max_tokens=100
)

generated_text = response.choices[0].text
print(generated_text)