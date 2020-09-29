# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 21:59:05 2018

@author: livingroom
"""

import tkinter as tk
import sys,pyautogui,time
from tkinter import messagebox


#移動鍵盤游標
def movefocus(event):
    if event.keysym == 'Up':
       pyautogui.hotkey('shift', 'tab', 'shift', 'tab', 'shift', 'tab''shift', 'tab', 'shift', 'tab', 'shift', 'tab', 'shift', 'tab', 'shift', 'tab', 'shift', 'tab', 'shift', 'tab')
    elif event.keysym == 'Down':
        pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab'])
    elif event.keysym == 'Left':
        pyautogui.hotkey('shift', 'tab')
    elif event.keysym == 'Right':
        pyautogui.press('tab')
    elif event.keysym == 'Return':
        checkPW()
    else :
        pyautogui.press('tab')
        
#開始解題
def checkPW():
    global n,q,t0,pointList
    #讀取題目
    for n in range(1,82,1):
        if len(globals() ['entry%s' %(n)].get())==0:
            a='0'
        else:
            a=str(globals() ['entry%s' %(n)].get())
        q=q+a
    sudoku=[]
    print('---')
    #題目輸入
    for i in range(81):
        a=int(q[i])
        sudoku.append(a)
    #計時開始
        t0=time.time()
    pointList=initPoint(sudoku)  
    showSudoku(sudoku)  
    print('\n')  
    p=pointList.pop()  
    check(p,sudoku)
    tryInsert(p,sudoku) 
    
class point:  
    def __init__(self,x,y):  
        self.x=x  
        self.y=y  
        self.available=[]  
        self.value=0  
  
#探測"同列"數字
def rowNum(p,sudoku):  
    row=set(sudoku[p.y*9:(p.y+1)*9])  
    row.remove(0)  
    return row #set type  
 #探測"同行"數字  
def colNum(p,sudoku):  
    col=[]  
    length=len(sudoku)  
    for i in range(p.x,length,9):  
        col.append(sudoku[i])  
    col=set(col)  
    col.remove(0)  
    return col #set type  

 #探測"同九宮格"數字  
def blockNum(p,sudoku):  
    block_x=p.x//3  
    block_y=p.y//3  
    block=[]  
    start=block_y*3*9+block_x*3  
    for i in range(start,start+3):  
        block.append(sudoku[i])  
    for i in range(start+9,start+9+3):  
        block.append(sudoku[i])  
    for i in range(start+9+9,start+9+9+3):  
        block.append(sudoku[i])  
    block=set(block)  
    block.remove(0)  
    return block #set type  

#  找空格，篩選數字
def initPoint(sudoku):  
    pointList=[]  
    length=len(sudoku)  
    for i in range(length):  
        if sudoku[i]==0:  
            p=point(i%9,i//9)  #座標
            for j in range(1,10):  
                if j not in rowNum(p,sudoku) and j not in colNum(p,sudoku) and j not\
                in blockNum(p,sudoku):  
                    p.available.append(j)  
            pointList.append(p)  
    return pointList  
  
#嘗試帶入  
def tryInsert(p,sudoku):
    global useTime
    availNum=p.available  
    for v in availNum:  
        p.value=v
        if check(p,sudoku):  
            sudoku[p.y*9+p.x]=p.value
            #完成、計時停止
            if len(pointList)<=0:  
                t1=time.time()
                useTime=t1-t0
                
                for n in range(1,82,1):
                    globals()['q%s' %(n)].set(sudoku[n-1])
                showSudoku(sudoku)
                messagebox.showinfo("Use Time",useTime)              
                print('\nuse Time: %f s'%(useTime))  
                exit() 

            p2=pointList.pop()  
            tryInsert(p2,sudoku)  
            sudoku[p2.y*9+p2.x]=0  
            sudoku[p.y*9+p.x]=0  
            p2.value=0  
            pointList.append(p2)
            
        else:  
            pass      
 #檢查 
def check(p,sudoku):  
    if p.value==0:  
        print('not assign value to point p!!')  
        return False  
    if p.value not in rowNum(p,sudoku) and p.value not in colNum(p,sudoku) and p.value not in blockNum(p,sudoku):  
        return True  
    else:  
        return False 
     

#秀出來(not in tkinter)
def showSudoku(sudoku):  
    for j in range(9):  
        for i in range(9):  
            print('%d '%(sudoku[j*9+i]),end='')  
        print('') 

#隱藏呼叫紀錄
sys.tracebacklimit=0 


#主視窗
win = tk.Tk()

#視窗標題
win.title("Sudoku Solver")   

#鎖定視窗大小
win.resizable(0,0)

#移動游標指令
win.bind_all('<KeyPress-Up>',movefocus)
win.bind_all('<KeyPress-Down>', movefocus) 
win.bind_all('<KeyPress-Left>', movefocus) 
win.bind_all('<KeyPress-Right>', movefocus)
win.bind_all('<KeyPress-1>', movefocus)
win.bind_all('<KeyPress-2>', movefocus)
win.bind_all('<KeyPress-3>', movefocus)
win.bind_all('<KeyPress-4>', movefocus)
win.bind_all('<KeyPress-5>', movefocus)
win.bind_all('<KeyPress-6>', movefocus)
win.bind_all('<KeyPress-7>', movefocus)
win.bind_all('<KeyPress-8>', movefocus)
win.bind_all('<KeyPress-9>', movefocus)
win.bind_all('<KeyPress-0>', movefocus)
win.bind_all('<KeyPress-Return>', movefocus)

q=''
#定義輸入鍵及跳出經過時間視窗



#顏色區域  
color={1,2,3,31,32,33,7,8,9,55,56,57,61,62,63,10,11,12,40,41,42,16,17,18,64,65,66,70,71,72,19,20,21,49,50,51,25,26,27,73,74,75,79,80,81}         
#變數編號  
n=1
#利用For迴圈、動態變數來設定Entry及Entry背景顏色
for j in range(9):
    for i in range(9):
        globals() ['q%s' %(n)]= tk.StringVar()
        if n in color:
            globals() ['entry%s' %(n)]=tk.Entry(win,bg='#ccddff',textvariable=globals() ['q%s' %(n)],font = ('Helvetica', '35', 'bold'),borderwidth =2,width=2,justify='center')
        else:
            globals() ['entry%s' %(n)]=tk.Entry(win,bg='#bfbfbf',textvariable=globals() ['q%s' %(n)],font = ('Helvetica', '35', 'bold'),borderwidth =2,width=2,justify='center')
        globals() ['entry%s' %(n)].grid(row=j, column=i, padx=5, pady=5,)    
        n+=1
win.configure(bg='#ffffff')

#解答鍵
button = tk.Button(win, text="Solve", command=checkPW)
button.grid(row=9, column=4, padx=5, pady=5,)

#開啟視窗
win.mainloop()
