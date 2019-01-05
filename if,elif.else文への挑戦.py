#もし～ならば(if, else, elsif)

import random
intimate = random.randint(1,7) #親密な関係で範囲は1～7
year = 2
lover = ("anyone")
if intimate >= 7:
    print(lover + "はsameoneの事を愛しています")
elif intimate >= 5:
    print(lover + "はsomeoneのことが" + str(year) + "年間、好きです") 
    print('someoneも' + lover + 'の事が' + str(year) +'年間、好きです')#Nomal_end
elif intimate >= 3:
    print('someoneは' + lover + 'の事を愛しています')
else:
    print(lover + "はsomeoneの事が好きでも嫌いでもありません")

print(intimate)
#これで上から条件を分岐させれた。