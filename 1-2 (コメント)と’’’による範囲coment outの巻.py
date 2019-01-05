#coding: utf-8
#↑エンコードルール(coding)
'''
日本語など、ASCII以外の文字を含むスクリプトを作成する場合は、スクリプトの1行目、または2行目に、下記の形式でスクリプトの
エンコードルール(coding:) を指定してください。大文字・小文字は無視されます。
まぁつまりは日本語とか他の特殊な文字コード使う言語使いたかったらエンコードルールを指定しろって事だね！おま国だよ！
でも書く必要あんまりないらしいよ！
'''
print ("hello world") #ここからはコメントだよー、実行されないよー #を付けるとコメントとして扱われるよー
#print ("hello world 1") #この様にコマンドの前に#を入れると実行されなくなる、このことをcoment outと呼ぶ
print ("hello world 2")
print ("hello world 3")



#同様に例えばハロワの2～3の範囲をcoment out したい場合は

print ("hello world 1")
'''
print ("hello world 2")
print ("hello world 3")
'''

#とシングルクオート*3で囲むとcoment out されるよ