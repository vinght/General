money = 100
apple_price = 100

if money > apple_price:
    print('りんごを買うことができます')
elif money == apple_price: #ここインデントつけるとifの中の扱いになる？、あとちゃんと:(セミコロン)で締める事
    print('りんごを買うことができますが所持金が0になります')
# 変数の値が等しい場合に「りんごを買うことができますが所持金が0になります」と出力してください


else:
    print('お金が足りません')