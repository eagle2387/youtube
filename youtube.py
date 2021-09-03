# -*- coding: utf-8 -*-
import youtube_module as m
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import threading


def click_func():
    url=yt_url.get()
    try:
        
        YouTube(url)
        
    except:
        messagebox.showerror('發生擷取錯誤','資料傳輸/擷取過程錯誤，請重新下截！！')
      
    urls=m.get_urls(url)
    
    
    if urls and messagebox.askyesnocancel('動作確認','是否下載所有清單(選擇 (N)僅下載單一影片)'):
                
        for u in urls:
            threading.Thread(target=m.start_dload,args=(u,listbox).start())
    
    else:
        yt=YouTube(url)
        if messagebox.askyesno('下載確認','下載本影片'):
            threading.Thread(target=m.start_dload,args=(url,listbox)).start()
        
    
    


window = tk.Tk()                  
window.geometry('640x480')        
window.title('YouTube 極速下載器') 

input_fm = tk.Frame(window, bg='red',  
                    width=640, height=120)
input_fm.pack()
#--↓ Label ↓--#
lb = tk.Label(input_fm, text='請輸入 YouTube 影片網址', 
              bg='red', fg='white',font=('細明體', 12))
lb.place(rely=0.25, relx=0.5, anchor='center')
yt_url = tk.StringVar()    
entry = tk.Entry(input_fm, textvariable=yt_url, width=50)
entry.place(rely=0.5, relx=0.5, anchor='center')
btn = tk.Button(input_fm, text='下載影片', command = click_func, 
               bg='#FFD700', fg='Black',font=('細明體', 10))
btn.place(rely=0.5, relx=0.85, anchor='center')

dload_fm = tk.Frame(window, width=640, height=480-120)
dload_fm.pack()


lb = tk.Label(dload_fm, text='下載狀態', 
              fg='black', font=('細明體', 10))
lb.place(rely=0.1, relx=0.5, anchor='center')

listbox = tk.Listbox(dload_fm, width=75, height=15)
listbox.place(rely=0.5, relx=0.5, anchor='center')


sbar = tk.Scrollbar(dload_fm)

listbox.config(yscrollcommand = sbar.set)
sbar.config(command = listbox.yview)
sbar.place(rely=0.5, relx=0.91, anchor='center', relheight=0.7)

window.mainloop()