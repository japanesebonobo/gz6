import openai, os, datetime, time

system_template = """会議の書き起こしが渡されます。

この会議のサマリーをMarkdown形式で作成してください。サマリーは、以下のような形式で書いてください。

- 会議の目的
- 会議の内容
- 会議の結果"""

# APIキーの入力を受け取る
api_key = input("APIキーを入力してください: ")
openai.api_key = api_key

# ファイルパスを入力してテキストファイルを読み込む
file_path = input("テキストファイルのパスを入力してください: ")
with open(file_path, "r") as file:
    user_input = file.read().strip()

# 応答の初期化
response = ""

# 4000文字を超える場合にテキストを分割してリクエスト
while len(user_input) > 0:
    time.sleep(30)
    text_chunk = user_input[:4000]
    user_input = user_input[4000:]

    # ChatCompletionのリクエストに要約のメッセージを追加
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "500文字以内で要約してください"},
            {"role": "assistant", "content": text_chunk}
        ]
    )

    # 応答の取得
    response += completion.choices[0].message.content

time.sleep(30)
# ChatCompletionのリクエストにユーザーメッセージを追加
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": system_template},
        {"role": "user", "content": response}
    ]
)

# Markdownファイルの出力先ディレクトリとファイル名の設定
output_dir = "./backlog"
os.makedirs(output_dir, exist_ok=True)
today = datetime.date.today()
output_file_name = f"gz6_{today}.md"
output_file_path = os.path.join(output_dir, output_file_name)

# Markdownファイルの出力
with open(output_file_path, "w") as output_file:
    output_file.write(response)

print(f"応答をファイル {output_file_name} に出力しました。")
