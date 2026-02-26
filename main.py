# これはサンプルの Python スクリプトです。
# ⌃R を押して実行するか、ご自身のコードに置き換えてください。
# ⇧ を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
# def print_hi(name):
#     # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
#     print(f'Hi, {name}')  # ⌘F8を押すとブレークポイントを切り替えます。
# ガター内の緑色のボタンを押すとスクリプトを実行します。
# if __name__ == '__main__':
#     print_hi('PyCharm')
# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください

import os
from dotenv import load_dotenv
from google import genai

def get_client():
    load_dotenv()  # これで.envファイルの内容を読み込む
    api_key = os.getenv("GEMINI_API_KEY") # 変数に代入
    return genai.Client(api_key=api_key)

    # クライアントの作成
    # client = genai.Client(api_key=api_key)
    # MODEL_NAME = 'gemini-2.5-flash'

def test_connection(client):
    # 接続テスト：簡単な質問を投げる
    print("Geminiに接続中...")

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='「接続成功だよ」と短く答えて'
    )

    # 返答を表示
    print("-" * 20)
    print(response.text)
    print("-" * 20)

if __name__ == '__main__':
    my_client = get_client()

    test_connection(my_client)

