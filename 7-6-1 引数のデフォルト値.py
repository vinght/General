# 引数のデフォルト値
'''
def introduce(name):
    print("私は" + name + "です。")


introduce("勇者")
'''
# def introduce
# でintroduce関数を定義
# それから引数のname変数を使って自己紹介をしている。 


def introduce(name = "村人"):
    print("私は" + name + "です。")

#こうやってdef関数の中で
# name = "村人"
# と定義することで引数のデフォルト値を定義することが出来る
# これをデフォルト値と言って、デフォルト値に代入したものが
# 関数名()の状態で 

introduce("勇者")
introduce()



def introduce1(name = "村人"):
    print("私は" + name + "です。")

#こうやってdef関数の中で
# name = "村人"
# と定義することで引数のデフォルト値を定義することが出来る
# デフォルト値と言って、引数を省略した場合に自動的に初期値を指定することが出来る。 

introduce1("勇者")
introduce1()




def introduce2(greeting , name = "村人"):
    print("私は" + name + "です。" + greeting)

#ただデフォルト値を引数に設定した関数があってそこに新たに
# 引数を追加したい場合は少し注意が必要
# pythonでは
# 「デフォルト値を設定したい引数」
# は
# デフォルト値の無い 引数の後
# に来なければならない 
# def introduce2(greeting , name = "村人")
#   print("私は" + name + "です。" + greeting)
# こんな感じで、
# 「私は村人です。こんにちは」
# と出力したい場合は上記の定義
# 下記のコードで出力する。逆だよって事 

introduce2("こんにちは","勇者")
introduce2("こんにちは")





# 可変長引数
# 引数を受け取るけれど、どれくらいの引数が来るかわからない時に使う

def introduce3(greeting , *names):
    for name in names:
        print("私は" + name + "です。" + greeting)
introduce3("こんにちは","勇者","村人","兵士",)


#これを走らせると
# 私は勇者です。こんにちは
# 私は村人です。こんにちは
# 私は兵士です。こんにちは

#引数名の前に「*」を入れるとそれは可変長引数ですよーという事になって
# リストとして利用できることになる。
# 今回の場合だと
# こんにちは = greeting
# names = ["勇者","村人","兵士"]
# ってな感じで処理されましたよって認識でよい。
# 後はfor文で回してるってだけっす。

# 可変長引数はdictにも使えるよ。







def introduce4(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)
    print(people)

introduce4(hero = "始めまして", villager="こんにちは",soldier="よろしくお願いします")

# introduce4は中身dictだよ、dict内の順序は入力と同じとは限らないから注意してね。

'''以下出力結果
{'hello': '始めまして', 'villager': 'こんにちは', 'soldier': 'よろしくお願いします'}
'''