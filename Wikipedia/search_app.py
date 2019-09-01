from tkinter import *
import wikipedia

def get_me():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value =wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "Pleace chek you input or internet connection")



root = Tk()
# create a Top frame
topframe=Frame(root)

entry =Entry(topframe)
entry.pack()

button = Button(topframe, text ="Search", command=get_me)
button.pack()

topframe.pack(side=TOP)

# create a bottom frame
bottomframe= Frame(root)

scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)

answer = Text(bottomframe, width=30, height=10, yscrollcommand=scroll.set)
scroll.config(command=answer.yview)
answer.pack()

bottomframe.pack()



root.mainloop()