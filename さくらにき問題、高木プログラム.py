#とりあえず、入力した文字が 3 なら"OK"、違うなら"NO"って出力するプログラム組んで
#ちなみに 3 は int型でね
'''
for i in range(4):
    if i == 3:
        print('OK')
    else:
        print('NO')
print(i)

# 上記は問題の取り方が間違ってた、以下が正解
a = input()
if int(a) == 3:
    print("OK")
else:
    print("NO")
'''

#入力した文字が"高木"だったら"からかうなっ！"って表示してー
#ちがうなら"ばーか！"って表示
#これを10買い繰り返す
'''
for i in range(1,11):
    nishikata = input(str(i) + ':入力してくだはい:')
    if nishikata == '高木':
        print('からかうなっ！')
    else:
        print('ばーか！')
        

for i in range(1,11):
    nishikata = input(str(i) + ':入力してくだはい:')
    if nishikata == '高木' or 'takagi' or 'たかぎ':
        print('からかうなっ！')
    else:
        print('ばーか！')'''
#もうちょっと綺麗に書いたら以下の通りになります
for i in range(10):
    nishikata = input('入力してくだはい:')
    if nishikata == '高木':
        print('からかうなっ！')
    else:
        print('ばーか！')