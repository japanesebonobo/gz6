import openai

# APIキーの入力を受け取る
api_key = input("APIキーを入力してください: ")
openai.api_key = api_key

# ユーザーからメッセージの入力を受け取る
user_input = input("メッセージを入力してください: ")

# ChatCompletionのリクエストにユーザーメッセージを追加
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": user_input}]
)

# 応答の出力
print(completion.choices[0].message.content)