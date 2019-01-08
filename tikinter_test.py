import sys
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()

#ウィンドウタイトルを設定
root.title(u"体重管理app(予定)")


#ウィンドウのサイズを変更
root.geometry('400x300')

def showMessage(text):
    tkm.showinfo('into', '強く生きろ')

def deleteEntry(event):
    tkm.askquestion('Do you want to all delete?', 'Yes? or No?')
    Entry1.delete(0, tk.END)

#ラベル
Static1 = tk.Label(
    text=u'▼Please input your weight▼'
    ,foreground='#000000'
    ,background='#86d673'
)
Static1.pack()

Entry1 = tk.Entry()
Entry1.insert(tk.END, u'plz input your weight')
Entry1.pack()





Static2 = tk.Label(text=u'Please input today')
Static2.place(x=150, y=208)

Entry2 = tk.Entry(width=30)
Entry2.insert(tk.END,u'input today')
Entry2.place(x=110, y=228)


# Entryの値を取得してみる
Entry1_value = Entry1.get()
print(Entry1_value)

Entry2_value = Entry2.get()
print(Entry2_value)


#Entry2.delete(0, tk.END) 入力された値を消すメソッド


Button1 = tk.Button(
    text=u'消すボタン',
    width=50,
    command=lambda:
    showMessage(Entry1.get())) 
Button1.bind("<Button-1>", deleteEntry)
# ボタンが押されたときに実行される関数をバインドします
Button1.pack()

root.mainloop()