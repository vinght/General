# Your code here!

# 2次元リストで地図を表示する

lundmap = [["森" for i in range(20)] for j in range(10)]
#地図の元になる二次元リストの完成
lundmap[0][0] = "城"
lundmap[0][19] = "町"
lundmap[9][19] = "町"
for i,line in enumerate(lundmap):
    print(str(i) + ":", end="")
    for area in line:
        print(area,end="")
    print()

'''出力結果
0:城森森森森森森森森森森森森森森森森森森町
1:森森森森森森森森森森森森森森森森森森森森
2:森森森森森森森森森森森森森森森森森森森森
3:森森森森森森森森森森森森森森森森森森森森
4:森森森森森森森森森森森森森森森森森森森森
5:森森森森森森森森森森森森森森森森森森森森
6:森森森森森森森森森森森森森森森森森森森森
7:森森森森森森森森森森森森森森森森森森森森
8:森森森森森森森森森森森森森森森森森森森森
9:森森森森森森森森森森森森森森森森森森森町
ここで生きていくのはとても辛そう。'''