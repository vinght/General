#paizaのリスト作り面白くなかったので都道府県のリスト作りまーす

# 製作時間休憩入れて約4時間、不具合修正(not自力)で+1時間



#で、更にそのリストを出力するプログラム組みます

touhoku =[
    "青森県",
    "岩手県",
    "宮城県",
    "秋田県",
    "山形県",
    "福島県",
]

kantou =[
    "茨城県",
    "栃木県",
    "群馬県",
    "埼玉県",
    "千葉県",
    "東京都",
    "神奈川県",
]

chubu =[
    "新潟県",
    "富山県",
    "福井県",
    "山梨県",
    "長野県",
    "岐阜県",
    "静岡県",
    "愛知県",
]

kinki =[
    "三重県",
    "滋賀県",
    "京都府",
    "大阪府",
    "兵庫県",
    "奈良県",
    "和歌山県",
]

chugoku =[
    "鳥取県",
    "島根県",
    "岡山県",
    "山口県",
]

shikoku =[
    "徳島県",
    "香川県(うどん)",
    "愛媛県",
    "高知県",
]

kyushu_okinawa =[
    "福岡県",
    "佐賀県",
    "長崎県",
    "熊本県",
    "宮城県",
    "鹿児島県",
    "沖縄県",
]



'''
countryside = input('地方名を入力してください:')
if countryside == '北海道':
    print('北海道')
elif countryside == "東北":
    print(touhoku)
elif countryside == "関東":
    print(kantou)
elif countryside == "中部":
    print(chubu)
elif countryside == "近畿":
    print(kinki)
elif countryside == "中国":
    print(chugoku)
elif countryside == "四国":
    print(shikoku)
elif countryside == ("九州・沖縄") or ("九州 沖縄") or ("九州　沖縄") or ("九州") or ("沖縄"): 
    print(kyushu_okinawa)
else:
    print('日本の地方の話を聞いてください！')
'''

#ここ最初は and で繋いだけど 正確には or 
# だって
#  and 
# だと全部の条件が「True」の場合「True」を返してくれる
# 今回の場合は条件式のどれかが「True」ならばいいから
# 使うのは
# or 

# バグ
# ？？？
# ("九州・沖縄") or ("九州 沖縄").....
# と言う風に、if elif 文の条件を指定したら
# elseに分岐させる入力をした時に必ず九州・沖縄に分岐する。
# ？？？
# 正しくは
# countryside == ("九州・沖縄") or countryside == ("九州 沖縄").......
# と入力しないとキチンと条件を指定したことにならない。
# 条件の指定に対する理解が甘かった。PCさん素直すぎ。
# 正しくは以下の通り

countryside = input('地方名を入力してください:')

if countryside == '北海道':
    print('北海道')
elif countryside == "東北" or countryside =="東北地方":
    print(touhoku)
elif countryside == "関東" or countryside =="関東地方":
    print(kantou)
elif countryside == "中部" or countryside =="中部地方":
    print(chubu)
elif countryside == "近畿" or countryside =="近畿地方":
    print(kinki)
elif countryside == "中国" or countryside =="中国地方":
    print(chugoku)
elif countryside == "四国" or countryside == "四国地方":
    print(shikoku)
elif countryside == "九州・沖縄" or countryside == "九州 沖縄" or countryside == "九州　沖縄":
    print(kyushu_okinawa)
elif countryside == "九州" or countryside ==  "沖縄":
    print('九州と沖縄は二大陸で一つ。九州・沖縄って分類されてるよ！')
elif countryside == "修羅の国":
    print("福岡県民が傷付くからそういう事を言うの止めてね！海に沈めちゃうよ？")
elif countryside == "ダイナマイト四国":
    print("四ッ国ッ！四ッ国ッ！・・・四ッ国ッ！四ッ国ッ！")
else:
    print('日本の地方の話を聞いてください！')