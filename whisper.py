import openai

# APIキーの入力を受け取る
api_key = input("APIキーを入力してください: ")
openai.api_key = api_key

# パスの入力を受け取る
file_path = input("ファイルのパスを入力してください: ")

# ファイルをバイナリモードで開く
with open(file_path, "rb") as audio_file:
    # 音声の転写を実行
    response = openai.Audio.transcribe("whisper-1", audio_file)
    transcript = response['text']

# 転写結果の表示
print(transcript)