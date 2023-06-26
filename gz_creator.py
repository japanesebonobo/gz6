import openai

system_template = """会議の書き起こしが渡されます。

この会議のサマリーをMarkdown形式で作成してください。サマリーは、以下のような形式で書いてください。

- 会議の目的
- 会議の内容
- 会議の結果"""

# APIキーの入力を受け取る
api_key = input("APIキーを入力してください: ")
openai.api_key = api_key

# ユーザーからメッセージの入力を受け取る
user_input = input("メッセージを入力してください: ")

# ChatCompletionのリクエストにユーザーメッセージを追加
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": system_template},
        {"role": "user", "content": user_input}
    ]
)

# 応答の出力
print(completion.choices[0].message.content)