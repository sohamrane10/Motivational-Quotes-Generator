from tkinter import *
from requests import *

root = Tk()
root.title("Motivational Quotes Web Application By Soham Rane")
root.geometry("1200x400+200+50")
root.configure(bg="black")

f = ("Bahnschrift SemiLight Condensed", 40, "bold")

lab = Label(root, font=f, wraplength=1000, bg="black", fg="white")
lab.pack(pady=30)

def gm():
    try:
        url = "https://zenquotes.io/api/random"
        res = get(url)
        data = res.json()
        quote = data[0]['q']
        author = data[0]['a']
        msg = f'"{quote}"\n\n- {author}'
        lab.configure(text=msg)
        root.after(5000, gm)
    except Exception as e:
        msg = "issue " + str(e)
        lab.configure(text=msg)

gm()
root.mainloop()
