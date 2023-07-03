import openai, os, datetime

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

# 転写結果をファイルに書き込む
output_dir = "./script"
os.makedirs(output_dir, exist_ok=True)
today = datetime.date.today()
output_file_name = f"script_{today}.txt"
output_file_path = os.path.join(output_dir, output_file_name)
with open(output_file_path, "w") as output_file:
    output_file.write(transcript)