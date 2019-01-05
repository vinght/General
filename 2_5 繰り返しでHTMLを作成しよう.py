# 繰り返しでHTMLを作成しよう

# 年齢入力のプルダウン作成

print('<select name=\'age\'>')
for age in range(100):
    print('<option>' + str(age) + '歳</option>')
print('</select>')

#ループ処理はとても便利というpaizaからのメッセージ


# 演習課題「HTMLの箇条書き表示」
'''
問題
以下のコードは、HTMLの箇条書きで1から3まで表示するプログラムです。
for inを使って、この箇条書きで1から100まで出力するよう修正してください。

プログラムを実行して、正しく出力されれば演習課題クリアです！

# HTMLによる箇条書き
print("<ul>")
print("<li>1</li>")
print("<li>2</li>")
print("<li>3</li>")
print("</ul>")

期待する出力値
<ul>
<li>1</li>
<li>2</li>
<li>3</li>
...
<li>100</li>
</ul>

'''

# 僕の回答
for number in range(1,101):
    print("<ul>")
    print("<li>" + str(number) + "</li>")
    print("</ul>")

# ↑間違え、処理がおかしいので<u1> </u1>が毎回出力される。正しくは
print("<ul>")
for number in range(1,101):
    print("<li>" + str(number) + "</li>")
print("</ul>")
#↑これ