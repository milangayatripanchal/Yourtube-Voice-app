import tkinter as tk
from tkinter import ttk
from selenium import webdriver
import speech_recognition as sr
import time

win = tk.Tk()
win.title("YTUBE")
win.geometry("300x200")
main = tk.Frame(win)
label = tk.Label(main,text="Ytube Search")
label.grid(row=0,columnspan=3,pady=10,ipadx=80)
label.configure(font=("New Time Roman",15))
label.configure(bg="#EA5824",fg="white")
user_input = tk.StringVar()
search_box = ttk.Entry(main,textvariable=user_input)
search_box.grid(row=2,columnspan=2,pady=15,padx=28,ipady=10,ipadx=40)
search_box.configure(font=('Arial',10,'bold'))
icon = tk.PhotoImage(file="mic1.png")

def search(event=None):
    if user_input.get():
        user_input.set("")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask to Youtube for search :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You request  : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
            return
        else:
            user_input.set(text)
    if text:
        driver = webdriver.Chrome()
        driver.get("https://www.youtube.com/results?search_query={}".format(text))

        '''search_box = driver.find_element_by_id('search')
        search_box.send_keys(text)

        search = driver.find_element_by_id('search-icon-legacy')
        search.click()'''

search_btn = ttk.Button(main,image=icon,command=search)
search_btn.grid(row=1,column=0,columnspan=2,pady=10)
win.bind('<Return>',search)
main.pack(side=tk.TOP,anchor="center")
win.mainloop()