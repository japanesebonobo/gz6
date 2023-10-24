from pydub import AudioSegment
import os, io

def split_m4a(file_path):
    # ファイルの読み込み
    audio = AudioSegment.from_file(file_path, format="m4a")

    # 分割サイズ（20MB）をバイト単位で計算
    split_size = 20 * 1024 * 1024

    # ファイル名と拡張子を分割
    base_name, ext = os.path.splitext(file_path)

    # バイト列にエクスポートし、バイト数を取得
    audio_bytes = audio.export(format="mp3").read()
    audio_size = len(audio_bytes)

    # 分割数を計算
    num_splits = audio_size // (split_size + 1)

    if audio_size <= 20 * 1024 * 1024:
        # 分割ファイルを保存（MP3形式で保存）
        mp3_file_path = f"{base_name}.mp3"
        audio.export(mp3_file_path, format="mp3")
        print(f"mp3への変換結果ファイルが20MB以下だったため、分割を行いませんでした")
        return

    # 分割処理
    for i in range(num_splits):
        start = i * split_size
        end = start + split_size

        # 分割されたオーディオを作成
        split_audio = AudioSegment.from_file(io.BytesIO(audio_bytes[start:end]), format="mp3")

        # 分割されたファイル名を作成
        split_file_name = os.path.join(os.path.dirname(file_path), f"{base_name}_{i+1}.mp3")  # Change the extension to .mp3

        # 分割ファイルを保存
        split_audio.export(split_file_name, format="mp3")  # Change the format to mp3

        print(f"分割ファイル {split_file_name} を作成しました。")

# ファイルパスを標準入力から受け取る
file_path = input("ファイルのパスを入力してください: ")
split_m4a(file_path)