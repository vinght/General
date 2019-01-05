# 標準入力とループ処理
'''
line = input()
print("hello " + line)
line = input()
print("hello " + line)'''

count = int(input())
#print('データ個数 ' + str(count))
for i in range(count):
    line = input().rstrip() #因みにこのrstrip()はデータの行末の改行を削除する
    print(line + 'はスライムを攻撃した')

'''
※１ 改行が残ってるとたまに悪さ？するからそれを削除するための命令
input().rstrip()でinputの戻り値の改行を削除する働きがある
データの行末の改行を削除する。
改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除しています
インプットの後に、ドットに続けて記述することで、インプットの戻り値の改行を削除することができます。
'''