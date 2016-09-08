# tkinter 进行GUI编程
'''
编写のPython代码调用内置Tkinter
Tkinter封装访问TK接口
TK is a pic Library 支持多个OS 利用Tcl语言开发
Tk 会调用OS提供の本地GUI接口 完成最终GUI
so code 只需调用TKinter提供的接口就可
'''
# GUI --- hellow word!
# 1 import Tkinter all the content
from tkinter import *
# 2 from Frame 派生 a Application 类 this is all Widget 父容器
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.helloLabel = Label(self,text='Hello,World!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text='Quit',command=self.quit)
		self.quitButton.pack()
# in CUI every Button Label 输入框等皆是一个Widget
# Frame可容纳其他WidgetのWidget，so allWidget组合起来 is a tree
# pack() method 可将Widget加入至父容器中 并实现布局
# pack() is simplest 布局 grid() 可是先complexer 布局
# in createWidget() create a Label and a Button.when Buttton 被点击时，触发self.quit()使程序退出
# 3 实例化Application 同时启动消息循环
app = Application()
# set window title
app.master.title('Hello World')
# main message loop
app.mainloop()
# GUI --- input text
# 改进上GUI 加入一个文本框 可让用户输入文本 然后点击按钮 弹出消息对话框
from tkinter import *
import tkinter.messagebox as messagebox
class Application2(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()
	def hello(self):
		name = self.nameInput.get() or 'world'
		messagebox.showinfo('Message','Hello, %s' % name)
app2 = Application2()
# set window title
app2.master.title('Hello World')
# main message loop
app2.mainloop()
# 当用户点击hello 通过self.nameInptut.get()获得用户输入文本后
# 使用Messagebox.showinfo()弹出消息对话框
# 可满足基本GUI程序要求の程序
# if GUI复杂的很 调用OS调用原生支持の语言与库来编写