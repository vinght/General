# 辞書、とは？
# まとまったデータをテキストだけじゃなく
# リストも辞書も扱える
# 例
an_example = {
    'ABC': 'ABCItem',
    'DEF': 123,
    'GHI': ['ABC', 'DEF'],
    'ADG': {
        'BEH': 'Item'
    }
} #これ辞書だよ、四次元ポケットかな？
#
# 
# 便利。
# 辞書は他プログラミング言語では連想配列、連想記憶とかって呼ばれてるらしいよ！
# 
# ？リストと辞書の違いは？

# リスト
# ページ数で管理する本みたいなイメージ

# 辞書
# 本に貼ってて、何かしら書いてる付箋みたいなイメージ


# で多分合ってるよ
#
# 
# 
#  
# ！辞書の基本機能
#  パッっと聞いた感じ、基本機能としてはリストと大差ない感じ。

#  要素を「数字」で管理するのがリスト
#  リストを作成するときに使うのが
#  []  ←大括弧

#  要素を「言葉」で管理するのが辞書
#  辞書を作成する時に使うのは
#  {}  ←波括弧
# 
#  なので要注意な！
# 
# 
#  
#  ！辞書の使いどころ
#  １データーベースとやり取りするデータの処理
#  ２APIとやり取りするデータの処理
#       例えば成績表があったとして、国語の点数の一覧データを処理したい場合は
#       listで処理する(出席番号というindex番号が与えられてるから)
#   学生、個人個人の各成績を処理したい場合は辞書を使う
#       名前や科目名(言葉)で管理してるから
#  
#   簡単に言えばわかりやすいようにするためにリストと辞書があるんやで
#   って事
#   おおまかだがこんな解釈


# 辞書オブジェクトで分からない事や調べたい事があったら以下のURLを参照するといい。
# 情報は古いけどpython3に変換して頑張って
# http://www.gesource.jp/programming/python/code/0018.html