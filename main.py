import openai

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
model = 'gpt-3.5-turbo'


def print_hi(name):
    query = name
    message = [
        {"role": "system", "content": query},
        {"role": "user", "content": query}
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=message
    )
    answer = response['choices'][0]['message']['content']
    print(answer)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('chatgpt 사용법 알려줘')


