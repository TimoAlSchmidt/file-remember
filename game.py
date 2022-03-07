import tkinter, os, os.path, inspect, json
from tkinter import ttk


window = tkinter.Tk()
window.title("\"Game\"")


def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()
    autosave(inspect.stack()[1][3])
    choice.set("")


def removeSpecificWidgets():
    for widget in window.winfo_children():
        if "Welke smaak" in widget.cget("text") or type(widget) is ttk.Button or type(widget) is ttk.Radiobutton:
            widget.destroy()


def quitButton():
    buttonMaker("Exit", lambda: window.destroy())
    if os.path.exists("autosave.json"):
        os.remove("autosave.json")

def labelMaker(texter):
    label = ttk.Label(window, text=texter)
    label.grid()


def entryMaker(texter=None):
    entry = ttk.Entry(window, text=texter)
    entry.grid()

def buttonMaker(texter, comma, stater="enabled"):
    button = ttk.Button(window, text=texter, command=comma, state=stater)
    button.grid()

def yesOrNoMore(quest, yes, var, comma=None):
    labelMaker(quest)
    for i in yes:
        g = ttk.Radiobutton(window, value=i, text=i,variable=var,command=comma)
        g.grid()


def autosave(function):
    contents = {"Location": function, "Choice" : choice.get()}
    with open("autosave.json", "w") as file:
        file.write(json.dumps(contents))

def load():
    global choice
    with open("autosave.json", "r") as file:
        string = file.read()
        diavolo = json.loads(string)
        choice.set(diavolo["Choice"])
        globals()[diavolo["Location"]](diavolo["Choice"])


def One():
    removeWidgets()
    yesOrNoMore("You're an adventurer, looking for treasure inside a dungeon. You walk into a room, the door disappearing behind you. You see 3 potions laid up on the table, a [red] one, a [blue] one and a [yellow] one. There's also a [read]able note on the table.\n", ["read", "red", "blue", "yellow"], choice, lambda: Two(choice.get()))

def Two(option):
    removeWidgets()
    if option == "read":
        labelMaker("""The note says: "Two of these potions are poisonous, the third one contains the solution to leaving this room. The correct color is the same as the blood of the most common inhabitant of the forest""")
        yesOrNoMore("Which one do you choose? [red], [blue] or [yellow]?", ["red", "blue", "yellow"], choice, lambda: Two(choice.get()))

    if option == "red":
        labelMaker("Red, like blood, right? You drink the red potion, hoping that your answer was correct. Unfortunately, you suddenly feel a burning deep inside your stomach, and burn from inside out. R.I.P.")
        quitButton()
    elif option == "blue":
        labelMaker("""Blue, like water, right? You drink the blue potion, hoping that your answer was correct. You don't feel anything at first, but then you feel your lungs fill with water. No matter how much you try to cough up the water, nothing comes out. R.I.P.""")
        quitButton()
    elif option == "yellow":
        labelMaker("""Yellow, like sap of trees, right? You drink the yellow potion, hoping that your answer was correct. You feel incredibly sick, but the feeling quickly subsides. The table suddenly combusts into flames, and reveals a trapdoor underneath.""")
        yesOrNoMore("You open the trapdoor, seeing a [ladder] and some water underneath. You can't gauge the depth of the water from here, but you can always try [jumping] in. You also consider [stay]ing in the room, anything better than going down there.", ["ladder", "jumping", "stay"], choice, lambda: Three(choice.get()))

def Three(option):
    removeWidgets()
    if option == "stay":
        labelMaker("""You stay in the room, and the trapdoor disappears. I suppose this is the room where doorways just stop existing once they're opened. You no longer have a way out, and starve to death. R.I.P.""")
        quitButton()
    elif option == "ladder":
        print("""You climb the ladder downward, halfway on the ladder, the trapdoor, and ladder, disappears. You fall down to the floor, luckily unharmed. You see that the water puddle is just that, a puddle.""")
        while True:
            option = input("""In this room, you see a [bookshelf] with books scattered about. You also see a [chest], with a bloody puddle next to it.""")
            if option == "chest":
                labelMaker("""You hope that bloody puddle is just ketchup. It wasn't, as the chest comes alive, and devours you whole. R.I.P.""")
                quitButton()
            elif option == "bookshelf":
                labelMaker("""You decide it's better not to mess around with the blood chest, you check around the books and see a lever hidden behind one the books. How clever. You pull the lever, and the bookshelf reveals a secret passageway downward.""")
                return Treasure()
    elif option == "jumping":
        labelMaker("""You jump into the water, hoping for the best, and you fall down through the water into another room.""")
        yesOrNoMore("In this room, you see a [sword] on a pedestal, and a [door].", ["sword", "door"], choice, lambda: Four(choice.get()))

def Four(option):
    global sword
    
    removeWidgets()
    if option == "door":
        labelMaker("You decide that going through the door is your top priority, because you don't want to get stuck in a room. Unfortunately, you'd probably be better off if you grabbed that sword, as a skeleton strikes you down when you exit. R.I.P.")
        quitButton()
    elif option == "sword":
        sword = True
        yesOrNoMore("You grab the sword from the pedestal, it's surprisingly light. You calmly exit the room, and enter another room. A big dining room, with tables all around. You see an skeleton with a wizard's hat, ready to cast a spell. Do you [roll] towards cover, [run] towards the skeleton or [throw] your sword.", ["roll", "run", "throw"], choice, lambda: Five(choice.get()))


def Five(option):
    
    removeWidgets()
    if option == "run":
        labelMaker("The skeleton casts a fireball and you light up in flames. R.I.P.")
        quitButton()
    elif option == "throw":
        labelMaker("You threw your sword. The skeleton casts a haunting spell on your sword. Your sword kills you. R.I.P.")
        quitButton()
    elif option == "roll":
        labelMaker("You roll towards one of the tables and flip them over as cover, safe for now, but not for long. The skeleton casts a fireball, and the table combusts into flames. Now what?")
        yesOrNoMore("Knocking over the table dropped some metal dining plates which you can [throw] at the skeleton, you can try [run]ning at him or you can also throw your [sword].", ["throw", "run", "sword"], choice, lambda: Six(choice.get()))

def Six(option):
    
    removeWidgets()

    if option == "run":
        labelMaker("You ran towards the skeleton. He had some trapping magic surrounding him, and you get killed by the venomous plants the trap produces. R.I.P.")
        quitButton()
    elif option == "sword":
        labelMaker("You ran towards the skeleton. He had some trapping magic surrounding him, and you get killed by the venomous plants the trap produces. R.I.P.")
        quitButton()

    yesOrNoMore("You hit the wizard skeleton straight in the face, confusing him. Now is your chance to strike. Do you run at him to [strike] him or do you [throw] your sword from a distance?", ["strike", "throw"], choice, lambda: Seven(choice.get()))


def Seven(option):
    
    removeWidgets()
    if option == "strike":
        labelMaker("You run at him, but just because a wizard is dazed doesn't mean his magic doesn't work. You get trapped by some venomous plants, and they bite you. R.I.P.")
        quitButton()
    elif option == "throw":
        labelMaker("You throw your sword at the skeleton, and kill him. Good job. You leave the dining room.")
        Treasure()


def Treasure():
    
    removeWidgets()
    yesOrNoMore("You enter a treasure room of some sort and see a lot of chests around, and a door outside. Do you [investigate] the chests or do you decide to [leave] this place as fast as possible?", ["investigate", "leave"], choice, lambda : Treasure2(choice.get()))


def Treasure2(option):
    
    removeWidgets()
    if option == "investigate":
        labelMaker("You decide that investigating the chests can't hurt. In one of the chests, you see a pile of gold, so you decide you want to take that.")
        if sword:
            labelMaker("But then, the chest comes alive, a mimic! You quickly strike it down. You decide to quickly grab the contents of the chests, and run outside, and to the nearby town. Unfortunately most of the other chests didn't contain anything of use.")
            labelMaker("You reach the nearby town, and complete your quest. In the bar, the blacksmith looks at your sword, and requests to investigate it. You let him, and it turns out it's a dragonsteel sword, forged in the fire of dragons. You decide to sell it for piles of gold. \nEnding 3/3: Rich")
            quitButton()
        else:
            labelMaker("But then, the chest comes alive, a mimic! You barely escape through the door, with a heavy scratch to your right leg. Unfortunately you had to leave the pile of gold.")
            labelMaker("You barely reach the nearby town, and have to get into debt to afford the potions to survive. \nEnding 2/3: Indebted")
            quitButton()
    elif option == "leave":
        labelMaker("You've had it with this dungeon, and decide to leave. You enter a nearby town. You check the bounty board and see that there's another dungeon... I guess it can't hurt to try, right? \nEnding 1/3: Safe and Sound")
        quitButton()
    


sword = False
choice = tkinter.StringVar()

if os.path.exists("autosave.json"):
    labelMaker("You have an autosave. Do you want to load it?")
    buttonMaker("Load", lambda: load())
    buttonMaker("Start new", lambda: One())
else:
    One()
window.mainloop()