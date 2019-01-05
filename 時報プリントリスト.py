# coding: utf-8
# if文による条件分岐　比較演算子
import random
time = random.randint(0,23)
tell_time = ('時です！')
if time == 0:
    print(str(time) + str(tell_time) + '日付が変わりました')
elif 3 >= time > 1:
    print(str(time) + str(tell_time) + '早く寝ましょー')
elif 5 >= time > 3:
    print(str(time) + str(tell_time) + '夜更かしはダメですよー')
elif 9 >= time > 5:
    print(str(time) + str(tell_time) + 'おはよーございます！')
elif time == 10:
    print(str(time) + str(tell_time) + 'おやつの時間ですよー！')
elif 14 >= time > 10:
    print(str(time) + str(tell_time) + '昼飯食え。')
elif 18 == time > 14:
    print(str(time) + str(tell_time) + '今日も一日お疲れ様でした')
else:
    print('夜やで、はよ休みーや')
print(time)

'''
elif後の条件指定は上記の様に定義を細かくしたりも出来る
別に
elif A == X の形じゃないとダメってわけではなく
elif B >= A == X って形でも認識してくれる。ってか細かく条件していしないと
一番上のelifが実行されてその後のやつはスキップされるから
条件は細かくしっかりと定義する事！！！
'''