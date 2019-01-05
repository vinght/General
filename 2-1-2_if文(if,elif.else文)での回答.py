#もし～ならば(if, else, elsif) 比較演算子
#何故エラーが出るかよくわかりません
#エラーの原因、else後にコメントアウトで何かしら書くとエラーが出る
'''
import random
intimate = random.randint(1,7) #親密な関係
year = random.randint(1,2)
y = 5 * 6

lover = ('anyone')
# xが70と等しい場合に「xは70です」と出力してください
if intimate == 7: #Ture end
    print(lover + "はmeの事を愛しています") #ここの条件式後のインデントからの動作をブロックと呼ぶ
elif 3 >= intimate >= 6:
    print(lover + "はmeのことが" + str(year) + "年程、好きです") 
    print('meも' + lover + 'の事が' + str(year) +'年程、好きです')#Nomal_end
elif 1 >= intimate >= 2:
    print(lover + 'の事を愛しています')
#2 >= intimate <=6
'''

'''

つまりifとelif 意外の条件ならBad_endに分岐するよってプログラムにな

xがもし(if)70だったら、Nomal_endに派生
xが83より大きければTure_endに派生


print(y)


# yが40と等しくない場合に「yは40ではありません」と出力してください
if y != 40: #等しくない場合は 「!=」と入力する、んで:(コロン)を必ずつけて終わらせる
    print("yは40ではありません")
'''