#coding: utf-8
#もし～ならば(if, else, elsif)

import random
intimate = random.randint(1,7) #親密な関係
y = 5 * 6

lover = ("anyone")
# xが70と等しい場合に「xは70です」と出力してください
if intimate == 2:
    number = random.randint(1,2)
    print(lover + "はmeのことが" + str(number) + "年程、好きです") 
    print('meも' + lover + 'の事が' + str(number) +'年程、好きです')#Nomal_end
    '''ifの条件式は「if 条件式 :」と書く
    んで注意はコロンで締める事
    ifの条件式後の動作は必ずインデント(字下げ)した後にする
    インデント(字下げ)しないとifの条件外と認識されて動作しなくなるよ。
    if文の動作内容はインデント後に書くこと
    python以外でプログラム書く時とか後々めちゃ読みづらいよ！注意して！
    因みにだけどじゃあif文以外でインデントを多用したらどうなるか？
    ・・・エラーが出て動かないよ！
    インデントは適材適所、pythonでインデントの使い方を学ぼう！
    '''
elif intimate > 2: #Ture end
    print(lover + "はmeの事を愛しています")
'''
elif は「さもなくば、もし」を意味する。
else + if = elif
このプログラムの場合は「intmate]がもし 2 ならNomal_end
3ならば Ture_endに派生するという意味'''

if intimate == 1:
    print(lover + "はmeの事が好きでも嫌いでもありません")   #Bad_end

'''
注意、elseは「さもなくば」だけを表しているので条件指定は元々されているので条件を指定する必要はない
つまりifとelif 意外の条件ならBad_endに分岐するよってプログラムにな

xがもし(if)70だったら、Nomal_endに派生
xが83より大きければTure_endに派生
'''
print(intimate)
print(y)


# yが40と等しくない場合に「yは40ではありません」と出力してください
if y != 40: #等しくない場合は 「!=」と入力する、んで:(コロン)を必ずつけて終わらせる
    print("yは40ではありません")
    '''
    そっからif文とつなげて支持を出したい場合「インデント(タブキーで作れる半角スペース4つ)」で
    if文が成り立ったら何をするかをインデント後に指定する。でないとプログラムが別物として認識される。
    '''



'''if文の基本（if, elif, else）
if文の基本的な形は以下のようになる。

if 条件式1:
    `条件式1がTrueのときに行う処理`
elif 条件式2:
    `条件式1がFalseで条件式2がTrueのときに行う処理`
elif 条件式3:
    `条件式1, 2がFalseで条件式3がTrueのときに行う処理`

else:
    `すべての条件式がFalseのときに行う処理

こんな感じでelifは論理が成り立つ限り何回でも使えるっちゅー事
んでelseはすべてFalseだった場合成り立つ、ここでエラーが出るという事はFalseについて考えたほうが良い
'''