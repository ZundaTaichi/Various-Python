from tkinter import *
import tkinter as tk
 
def click_btn1():
    if label['text'] == '0':
        label['text'] = '1'
    else:
        label['text'] = label['text'] +'1'
def click_btn2():
    if label['text'] == '0':
        label['text'] = '2'
    else:
        label['text'] = label['text'] +'2'
def click_btn3():
    if label['text'] == '0':
        label['text'] = '3'
    else:
        label['text'] = label['text'] +'3'
def click_btn4():
    if label['text'] == '0':
        label['text'] = '4'
    else:
        label['text'] = label['text'] +'4'
def click_btn5():
    if label['text'] == '0':
        label['text'] = '5'
    else:
        label['text'] = label['text'] +'5'
def click_btn6():
    if label['text'] == '0':
        label['text'] = '6'
    else:
        label['text'] = label['text'] +'6'
def click_btn7():
    if label['text'] == '0':
        label['text'] = '7'
    else:
        label['text'] = label['text'] +'7'
def click_btn8():
    if label['text'] == '0':
        label['text'] = '8'
    else:
        label['text'] = label['text'] +'8'
def click_btn9():
    if label['text'] == '0':
        label['text'] = '9'
    else:
        label['text'] = label['text'] +'9'
def click_btn0():
    if label['text'] == '0':
        label['text'] = '0'
    else:
        label['text'] = label['text'] +'0'
    
def click_btnAc():
    label['text'] = '0'
    buttonPlus['fg'] = "black"
    buttonMinus['fg'] = "black"
    buttonMulti['fg'] = "black"
    buttonDived['fg'] = "black"
    
def click_btnPlus():
    global box
    global hugo
    box = label['text']
    label['text'] = '0'
    hugo = "+"
    buttonPlus['fg'] = "orange"
    buttonMinus['fg'] = "black"
    buttonMulti['fg'] = "black"
    buttonDived['fg'] = "black"
def click_btnMinus():
    global box
    global hugo
    box = label['text']
    label['text'] = '0'
    hugo = '-'
    buttonPlus['fg'] = "black"
    buttonMinus['fg'] = "orange"
    buttonMulti['fg'] = "black"
    buttonDived['fg'] = "black"
def click_btnMulti():
    global box
    global hugo
    box = label['text']
    label['text'] = '0'
    hugo = "x"
    buttonPlus['fg'] = "black"
    buttonMinus['fg'] = "black"
    buttonMulti['fg'] = "orange"
    buttonDived['fg'] = "black"
def click_btnDived():
    global box
    global hugo
    box = label['text']
    label['text'] = '0'
    hugo = "÷"
    buttonPlus['fg'] = "black"
    buttonMinus['fg'] = "black"
    buttonMulti['fg'] = "black"
    buttonDived['fg'] = "orange"
def click_btnEqual():
    box_Int1 = int(box)
    box2 = label['text']
    box_Int2 = int(box2)
    
    if hugo == '+':
        result = box_Int1 + box_Int2
        label['text'] = result
    elif hugo == '-':
        result = box_Int1 - box_Int2
        label['text'] = result
    elif hugo == 'x':
        result = box_Int1 * box_Int2
        label['text'] = result
    elif hugo == '÷':
        result = box_Int1 / box_Int2
        label['text'] = result
    else:
        label['text'] = 'Error'
        
 
baseGround = tk.Tk()
baseGround.title('calculate')
baseGround.geometry('500x600')
 
 
# ラベルやボタンの作成と配置
label = tk.Label(baseGround, text='0', background='lightgray')
label.place(x=50, y=50, width=400, height=105)
 
 
button1 = tk.Button(baseGround,text = '1', command=click_btn1)
button1.place(x=50, y=205, relwidth=0.18, relheight= 0.125)
 
button2 = tk.Button(baseGround,text = '2', command=click_btn2)
button2.place(x=153, y=205, relwidth=0.18, relheight= 0.125)
 
button3 = tk.Button(baseGround,text = '3', command=click_btn3)
button3.place(x=256, y=205, relwidth=0.18, relheight= 0.125)
 
buttonPlus = tk.Button(baseGround,text = '+', command=click_btnPlus)
buttonPlus.place(x=359, y=205, relwidth=0.18, relheight= 0.125)
 
button4 = tk.Button(baseGround,text = '4', command=click_btn4)
button4.place(x=50, y=295, relwidth=0.18, relheight= 0.125)
 
button5 = tk.Button(baseGround,text = '5', command=click_btn5)
button5.place(x=153, y=295, relwidth=0.18, relheight= 0.125)
 
button6 = tk.Button(baseGround,text = '6', command=click_btn6)
button6.place(x=256, y=295, relwidth=0.18, relheight= 0.125)
 
buttonMinus = tk.Button(baseGround,text = '-', command=click_btnMinus)
buttonMinus.place(x=359, y=295, relwidth=0.18, relheight= 0.125)
 
button7 = tk.Button(baseGround,text = '7', command=click_btn7)
button7.place(x=50, y=385, relwidth=0.18, relheight= 0.125)
 
button8 = tk.Button(baseGround,text = '8', command=click_btn8)
button8.place(x=153, y=385, relwidth=0.18, relheight= 0.125)
 
button9 = tk.Button(baseGround,text = '9', command=click_btn9)
button9.place(x=256, y=385, relwidth=0.18, relheight= 0.125)
 
buttonMulti = tk.Button(baseGround,text = 'x', command=click_btnMulti)
buttonMulti.place(x=359, y=385, relwidth=0.18, relheight= 0.125)
 
button0 = tk.Button(baseGround,text = '0', command=click_btn0)
button0.place(x=50, y=475, relwidth=0.18, relheight= 0.125)
 
buttonEqual = tk.Button(baseGround,text = '=', command=click_btnEqual)
buttonEqual.place(x=153, y=475, relwidth=0.18, relheight= 0.125)
 
buttonAc = tk.Button(baseGround,text = 'AC', command=click_btnAc)
buttonAc.place(x=256, y=475, relwidth=0.18, relheight= 0.125)
 
buttonDived = tk.Button(baseGround,text = '÷', command=click_btnDived)
buttonDived.place(x=359, y=475, relwidth=0.18, relheight= 0.125)
 
baseGround.mainloop()