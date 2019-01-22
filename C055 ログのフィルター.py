'''
times = int(input())
correct = input()
for i in range(times):
    target = input()
    if correct in target:
        print(target)
    elif correct not in target and i + 1 == times:
        print('None')
'''
# 50点

#以下訂正1
times = int(input())
correct = input()
for i in range(1 , times + 1):
    print(str(i) + "test")
    target = input()
    if correct in target:
        print(target)
    elif correct not in target and i == times:
        print('None')

# 最後のelifの条件がおかしい。
# correct not in target
# と
# i = timesの所。SHUSEISEYO SHUSEISEYO!

#訂正2
times = int(input())
correct = input()
lines = []
for i in range(1 , times + 1):
    target = input()
    if correct in target:
        lines.append(target)
        print(target)
    elif i == times and len(lines) == 0:
        print('None')

# 訂正1ではelifの後をどういじってもコードが改善される気配が無いと判断したので
# リストを使ってNoneが出力される条件を調整してみたら見事に通りました。