#decoding: uft-8

apple_price = 200
# 変数moneyに数値1000を代入してください
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)  #何でここだけint型なの？
total_price = apple_price * count
# int型にしないと計算が出来ないから。
# 基本inputで受け取った値はstring typeとして認識されるため
# 計算させる時はint typeだよって教えてあげないといけない
# じゃないとPC君的には あ と 1 を計算してくださいねー
# って言われてる感覚、他言語だと文字を入力する時は文字型を指定する必要があるが
# python君は基本、stirng typeで受け取る為、意識しないとアカンで。


print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')


# moneyとtotal_priceの比較結果によって条件を分岐してください
if money > total_price:
    print('りんごを' + str(count) + '個買いました')
    print('残金は' + str(money - total_price) + '円です')

elif money == total_price:
    print('りんごを' + str(cout) + '個買いました')
    

else:
    print('お金が足りません')
    print('りんごを買えませんでした')


'''
基本はifとelseを使う
その間に条件文を増やしたかったら「elif」

出たエラー
SyntaxError: invalid syntax
構文間違ってるよ・・。
（'がなかったりそもそも構文を勘違いしてたりの単純な間違いが多い
'''