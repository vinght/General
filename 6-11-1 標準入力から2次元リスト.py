'''入力される値
0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0
1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1
1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1
1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1
0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0
0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0
0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1
_
'''
# Your code here!

# 標準入力から2次元リスト
'''
while True:
    line = input()
    if line == "_":
        break
    print(line)
'''
enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    enemy_img.append(line)



# 標準入力から2次元リスト
enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    enemy_img.append(line.split(","),)
#print(enemy_img)
for line in enemy_img:
    for dot in line:
        if dot == 1:
            #標準入力から入力されたデータはデフォで
            # string typeだからint typeだと条件式が成り立たないよ
            print("#", end="")
        else:
            print(" ", end="")
    print()


# Your code here!

# 標準入力から2次元リスト
enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    enemy_img.append(line.split(","),)
print(enemy_img)
for line in enemy_img:
    for dot in line:
        if dot == "1": #なのでここはこうするか
            print("#", end="")
        else:
            print(" ", end="")
    print()
'''出力結果
  ############  
##            ##
#  ###   ###   #
##    ##      ##
  ############  
   ###     ###  
    ###      ###
'''




enemy_img = []
while True:
    line = input()
    if line == "_":
        break
    enemy_img.append(line.split(","),)

for line in enemy_img:
    for dot in line:
        if int(dot) == 1: #こうして文字型を整えなきゃだね。動的だと文字型を意識する機会が多いね！
            print("#", end="")
        else:
            print(" ", end="")
    print()

'''出力
  ############  
##            ##
#  ###   ###   #
##    ##      ##
  ############  
   ###     ###  
    ###      ###
'''

# まぁ結果は一緒だね。int(dot)にするか =="1" にするかの違いだね。
# 今回の場合は入力される文字が1か0かだから
# if dot == "1"
# が使えたってだけの話だよ。いろんなやり方があるね。 