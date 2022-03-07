import tkinter, random, json
from tkinter import ttk

commands = ["Press: w", "Press: a", "Press: s", "Press: d", "Press: space", "Click", "Double click", "Triple click"]
question = "Click"
maxTimer = 20
timer = 20
points = -2
gaming = True
location = 0

diavolo = {}


window = tkinter.Tk()
window.geometry("500x500")
window.title("FPS")


label1 = tkinter.Label(
    window,
    bg="white",
    fg="black"
)
label2 = tkinter.Label( #points/Time
    window,
    bg="black",
    fg="white"
)
timerBox = tkinter.Entry(window, textvariable = tkinter.StringVar(window,value="20"))

name = tkinter.StringVar()
stringvar = tkinter.StringVar(value="Klik hier om te beginnen")
stringvar2 = tkinter.StringVar(value="Time Remaining: {}                {} points".format(0, 0))

def removeWidgets():
    for widget in window.winfo_children():
        if type(widget) is ttk.Label:
            if "Score" in widget.cget("text"):
                continue
        widget.destroy()

def labelMaker(texter):
    label = ttk.Label(window, text=texter)
    label.pack()


def entryMaker(texter=None):
    entry = ttk.Entry(window, text=texter)
    entry.pack()

def buttonMaker(texter, comma, stater="enabled"):
    button = ttk.Button(window, text=texter, command=comma, state=stater)
    button.pack()

def removeSpecificWidget():
    for widget in window.winfo_children():
        if type(widget) is ttk.Label:
            for i in commands:
                if i in widget.cget("text"):
                    widget.destroy()
                    return


def nextCommand(point):
    global question, points
    if gaming:
        points += point
        label1.place(relx=random.uniform(0.3, 1.0),rely=random.uniform(0.1,0.9),relwidth=0.3,anchor="ne")
        question = random.choice(commands)
        stringvar.set(question)
        stringvar2.set("Time Remaining: {}                {} points".format(timer, points))
        if "space" in question:
            question = " "
        elif "w" in question:
            question = "w"
        elif "a" in question:
            question = "a"
        elif "d" in question:
            question = "d"
        elif "s" in question:
            question = "s"


def startGame():
    global gaming, question, timer, points
    gaming = True
    timer = maxTimer
    points = -2
    
    removeWidgets()
    label1 = tkinter.Label(
    window,
    bg="white",
    fg="black"
    )

    label2 = tkinter.Label( #points/Time
        window,
        bg="black",
        fg="white"
    )

    label1.bind("<Button-1>", click)
    label1.bind("<Double-Button-1>", doubleclick)
    label1.bind("<Triple-Button-1>", tripleclick)

    label1.config(textvariable=stringvar)
    label2.config(textvariable=stringvar2)

    yes = tkinter.Button(window,bg="black", fg="white",command = startGame,text="Yes")
    no = tkinter.Button(window,bg="black",fg="white", command = lambda : window.destroy(),text="No")
    

    yes.place(relx=1, rely=1,relwidth=0.2,anchor='ne')
    no.place(relx=1, rely=1,relwidth=0.2,anchor='ne')
    label1.place(relx=0.75,rely=0.5,relwidth=0.5,anchor="ne")
    stringvar.set("Klik hier om te beginnen")
    stringvar2.set("Time Remaining: {}                {} points".format(maxTimer, 0))
    question = "Click"

def tick():
    global timer
    timer -= 1
    if timer == 0:        
        return stopGame()
    stringvar2.set("Time Remaining: {}                {} points".format(timer, points))
    window.after(1000, tick)


def command(event):
    if event.char == question:
        nextCommand(1)

def click(event):
    global timer, maxTimer
    if points == -2:
        window.after(1000, tick)
        try:
            maxTimer = int(timerBox.get())
        except:
            maxTimer = 20
        timer = maxTimer
        if not diavolo:
            timerBox.place(relx=1, rely=1,relwidth=0.2,anchor='ne')
    if question == "Click":
        nextCommand(2)
        

def doubleclick(event):
    if question == "Double click":
        nextCommand(2)

def tripleclick(event):
    if question == "Triple click":
        nextCommand(2)


def stopGame():
    global gaming
    gaming = False
    removeWidgets()
    doHighScores()

def showHighScores():
    for person in diavolo["Highscores"]:
        labelMaker("{} : {}".format(person["Name"], person["Score"]))

def doHighScores():
    global diavolo, location, name
    highScore = False
    location = 0
    name.set("")
    with open("highscores.json", "r") as file:
        diavolo = json.loads(file.read())

    showHighScores()
    
    for person in diavolo["Highscores"]:
        if points > person["Score"]:
            highScore = True
        if not highScore:
            location += 1
    if highScore:
        print(location)
        labelMaker("A new high score!!! What is your name?")
        entryMaker(name)
        buttonMaker("Done", inputHighScore)
    else:
        buttonMaker("Verder", lambda: window.destroy())

def inputHighScore():
    for i in range(9, location, -1):
        diavolo["Highscores"][i]["Name"] = diavolo["Highscores"][i-1]["Name"]
        diavolo["Highscores"][i]["Score"] = diavolo["Highscores"][i-1]["Score"]


    diavolo["Highscores"][location]["Name"] = name.get()
    diavolo["Highscores"][location]["Score"] = points
    
    with open("highscores.json", "w") as file:
        file.write(json.dumps(diavolo))

    window.destroy()




yes = tkinter.Button(window,bg="black", fg="white",command = startGame,text="Yes")
no = tkinter.Button(window,bg="black",fg="white", command = lambda : window.destroy(),text="No")  

window.bind("w", command)
window.bind("a", command)
window.bind("s", command)
window.bind("d", command)
window.bind("<space>", command)


label1.place(relx=0.75,rely=0.5,relwidth=0.5,anchor="ne")
timerBox.place(relx = 0.45, rely=0.75, relwidth=0.2, anchor ='ne')


label1.bind("<Button-1>", click)
label1.bind("<Double-Button-1>", doubleclick)
label1.bind("<Triple-Button-1>", tripleclick)

label1.config(textvariable=stringvar)
label2.config(textvariable=stringvar2)

label2.pack()

window.mainloop()

