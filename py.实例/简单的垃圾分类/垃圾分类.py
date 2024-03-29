import tkinter

kehuishou=["塑料瓶","食品罐头","玻璃瓶"]
youhai=["油漆桶","电池","油漆"]
shi=["菜叶","葱","陈皮"]
gan=["贝壳","化妆刷","海绵"]

def lajifenlei():
    lmr = entry_1.get()

    if lmr in kehuishou:
        label_2["text"]="可回收垃圾"
    elif lmr in youhai:
        label_2["text"]="有害垃圾"
    elif lmr in shi:
        label_2["text"] ="湿垃圾"
    elif lmr in gan:
        label_2["text"] ="干垃圾"
    else:
        label_2["text"]="未知"


win=tkinter.Tk()
win.title("垃圾分类助手")
win.geometry("300x150")

label=tkinter.Label(text="垃圾分类助手",font=("黑体",20,"bold"))
label.pack()

label_1=tkinter.Label(win,text="是什么垃圾：")
label_1.place(x=20,y=50)

entry_1=tkinter.Entry(win,width=10)
entry_1.place(x=120,y=50)

label_2=tkinter.Label(win,fg="red")
label_2.place(x=110,y=100)

button_1=tkinter.Button(win,text="查看分类",command=lajifenlei)
button_1.place(x=200,y=45)

win.mainloop()