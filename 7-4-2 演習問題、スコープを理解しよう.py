#演習課題
'''
「間違い探し」
右のコードでは、say_hello関数を呼び出していますが、エラーになってしまいます。
間違いを修正して、msg変数を使って、「hello paiza」と表示されるようにしてください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値
hello paiza'''

# 間違い探し

msg = "hello"

def say_hello():
    global msg
    msg += " "
    msg += "paiza"
    print(msg)

say_hello()