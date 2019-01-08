#演習課題
'''
「リストの中身を1行ずつ表示してみよう」
右のコードエリアには、「A」という文字が、leter_Aという2次元リストで定義されています。
このリストから要素を順に取り出して、ドットで文字を出力してください。
この時、要素が1だったら「@」(半角アットマーク)、ゼロだったら「 」(半角スペース)を出力します。

プログラムを実行して、正しく出力されれば演習課題クリアです！

期待する出力値

  @@  
 @  @
@    @
@@@@@@
@    @
@    @
'''
# ドットで文字を出力しよう

letter_A = [[0,0,1,1,0,0],
            [0,1,0,0,1,0],
            [1,0,0,0,0,1],
            [1,1,1,1,1,1],
            [1,0,0,0,0,1],
            [1,0,0,0,0,1]]

# ここに、ドットを表示するコードを記述する
for line in letter_A:
    for dot in line:
        if dot == 1:
            print("@",end="")
        else:
            print(" ",end="")
    print()
