from tkinter import *
import time
import winsound
######################################################################
import tkinter.messagebox
tk= Tk()
tk.title("SHUBHASHIS MONDAL Game")
buttons=StringVar()
gd=True
###########################################################################
def check(buttons):
                global gd
                if buttons["text"] ==" " and gd== True:
                                buttons["text"]= m
                                gd= False
                elif buttons["text"]==" " and gd== False:
                                
                                buttons["text"]=n
                                gd= True
                if button1 ["text"] == m and button4 ["text"] == m and button7 ["text"] == m or button7 ["text"] == m and button8 ["text"] == m and button9 ["text"] == m or button9 ["text"] == m and button6 ["text"] == m and button3 ["text"] == m or button1 ["text"] == m and button2 ["text"] == m and button3 ["text"] == m or button2 ["text"] == m and button5 ["text"] == m and button8 ["text"] == m or button4 ["text"] == m and button5 ["text"] == m and button6 ["text"] == m or button1 ["text"] == m and button5 ["text"] == m and button9 ["text"] == m or button3 ["text"] == m and button5 ["text"] == m and button7 ["text"] == m:
                                print("Yes")
                                tkinter.messagebox.showinfo("Winner is X","%s  You have won........"%p)
                                winsound.PlaySound("win",winsound.SND_FILENAME)
                if button1 ["text"] == n and button4 ["text"] == n and button7 ["text"] == n or button7 ["text"] == n and button8 ["text"] == n and button9 ["text"] == n or button9 ["text"] == n and button6 ["text"] == n and button3 ["text"] == n or button1 ["text"] == n and button2 ["text"] == n and button3 ["text"] == n or button2 ["text"] == n and button5 ["text"] == n and button8 ["text"] == n or button4 ["text"] == n and button5 ["text"] == n and button6 ["text"] == n or button1 ["text"] == n and button5 ["text"] == n and button9 ["text"] == n or button3 ["text"] == n and button5 ["text"] == n and button7 ["text"] == n:
                                print("oh")
                                tkinter.messagebox.showinfo("Winner is O","%s You have won........"%q)
                                winsound.PlaySound("win",winsound.SND_FILENAME)
######################
def gdas(s="",w=75,q=0.09):
                print(" "*w,end="")
                for i in range(len(s)):
                                time.sleep(q)
                                print(s[i],end="")
#######
def das(w):
                for i in range(w):
                                print()
##############################################################################
p=input("Player`s 1s Name please..........")
print(p,end="")
m=input(" Can I have Your Symbol Please..... ")
q=input("Player`s 2s Name please..........")
print(q," Can I have Your Symbol please........",end="")
while True:
                n=input()
                if n!=m:
                                break
                else:
                                print("Enter Again!!!!!!!You Can`t Choose These!!!!!! - ",end="")
print(p,"..........Are You Ready??????")
input()
print(q,".........Are You Ready???????")
input()

##########$$$$$$$$$$$$$$$$$$$$$$##############################
button1=Button(tk,text= " ",height=7,width=19,command=lambda:check(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(tk,text= " ",height=7,width=19,command=lambda:check(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(tk,text= " ",height=7,width=19,command=lambda:check(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(tk,text= " ",height=7,width=19,command=lambda:check(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(tk,text= " ",height=7,width=19,command=lambda:check(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(tk,text= " ",height=7,width=19,command=lambda:check(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(tk,text= " ",height=7,width=19,command=lambda:check(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(tk,text= " ",height=7,width=19,command=lambda:check(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(tk,text= " ",height=7,width=19,command=lambda:check(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

tk.mainloop()
##################$$$$$$$$$$$$$$$$$$$$$$$$###########################





















































         
