import openai
from ApiKey.apikey import key
openai.api_key = key()
openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
    ]
)

while True:
    prompt = input('\nAsk a question: ')
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],)

    message = completion.choices[0].message.content
    print(message)
