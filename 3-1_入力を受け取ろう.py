#入力を受け取ろろう
'''
「input」を用いると、コードを実行した際にコンソールに文字を入力できるようになり
その入力された値を受け取ることができます。
input関数はユーザーがキーボードに入力したデータを受け付ける関数

「変数 = input('コンソールに表示したい文字列')」
のように使うとコンソールに入力された値が変数に代入されます。
まぁとどのつまり、
imput関数は今までpcにあれやってこれやってと指令しかできなかったけど
プログラム内のルールである程度お話が出来るよ！友達が少なくても安心だね！
'''
apple_price = 200

# inputを用いて入力を受け取り、変数input_countに代入してください
input_count = input('購入するりんごの個数を入力してください：') #これでinput出来るんや


# input_countを数値として代入してください
count = int(input_count) #ここでinputして値を決めれるようにしてるわけやな！ しかも何故かint typeに指定しよったで
total_price = apple_price * count 
    #んでのcount君はinputによって値の変わる数学的な変数にメイクアップしたで

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')