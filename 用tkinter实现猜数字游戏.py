#!/usr/bin/env python
# coding: utf-8

# In[51]:





# In[16]:


import tkinter
import tkinter.messagebox
import math
import random

root = tkinter.Tk()
root.title('数字炸弹')
root.geometry('400x400')
num1=random.randint(1,100)


def cai_shu_zi():
    guess=int(num.get())
    if guess > num1:
        tkinter.messagebox.showinfo("height","Your guess is too height.")
    if guess < num1:
        tkinter.messagebox.showinfo("low","Your guess is too low.")
    if guess == num1:
        tkinter.messagebox.showinfo("good","哎呦，不错哦！")


label = tkinter.Label(root,text='Wellcome to our game!',font=(16))
label.place(x=10,y=30,height=30,width=250)

label2 = tkinter.Label(root,text="游戏规则：\n从1到100中猜数字！！！",font=('宋体',13))    
label2.place(x=10,y=80,height=40,width=400)

labelNum = tkinter.Label(root,text='请输入你猜的数字')
labelNum.place(x=10,y=120,height=30,width=150)

num = tkinter.StringVar(root)
entryNum = tkinter.Entry(root,width=150,textvariable=num)
entryNum.place(x=150,y=120,height=30,width=80)

button = tkinter.Button(root,text='确定',command=cai_shu_zi)
button.place(x=150,y=160,height=30,width=80)  

button2 = tkinter.Button(root, text='退出游戏',command=root.quit,bg='green', font=('微软雅黑', 10,))
button2.place(x=150,y=200,height=30,width=80)
root.mainloop()


# In[ ]:




