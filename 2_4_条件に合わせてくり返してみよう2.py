# whileによるループ処理

#スライムを攻撃
#ダメージは1から10までランダム
#スライムのHPが0になるまで繰り返す
'''
import random
dmage = random.randint(1,10)
hp = 10
while hp == 0:
    print('スライムに' + str(j) + 'のダメージを与えた')# 繰り返し処理
    hp -= dmage # カウンタ変数を更新

print('test' + str(j))'''
'''
import random
dmage = random.randint(0,10)
hp = 10
while hp > 0:
    print('スライムに' + str(damage) + 'のダメージを与えた')# 繰り返し処理
    hp -= dmage # カウンタ変数を更新
    if dmage == 0: ！←ここ要らない 何故ならこれはループ処理だからループ条件式が終われば次の処理に移行する！
print('スライムを倒した')

print(dmage)'''

# if文も追加してクリティカルヒットの概念を与えてみた
'''
import random
hp = 30
dice = random.randint(1,3)
while hp > 0:
    hit = random.randint(1,10)
    print('スライムに' + str(hit) + 'のダメージを与えた')
    if dice == 2:
        hit = hit * 1.5
        print('クリテカルヒット！' + str(hit) + 'ダメージをスライムに与えた')
    hp -= hit
print('スライムを倒した')

print('lust:' + str(hp))
これじゃ正常に動作しなかった
原因はdiceの条件式がwhile文の外にあったからループ外になってたから、正確には以下
'''



# 以下思いつきというか上記をもとに追加してみたプログラム
import random
hp = 30

while hp > 0:
    hit = random.randint(1,10)
    dice = random.randint(1,3) #ここにランダムにすると毎回サイコロ降られる
    print('スライムに' + str(hit) + 'のダメージを与えた')
    if dice == 2:
        hit = hit * 1.5
        print('クリテカルヒット！' + str(hit) + 'ダメージをスライムに与えた')
    hp -= hit
print('スライムを倒した')

print('lust:' + str(hp))
print(dice)
# これで意図通りに動作した