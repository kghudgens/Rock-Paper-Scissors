from tkinter import *
import random

root= Tk()
root.title("Rock, Paper, Scissors")

#computer options
comp_options= ["Rock", "Paper", "Scissors"]
comp_choice = random.choice(comp_options)

# Instructions
start= Label(root, text="Select Your Option For RPS")

#Define buttons

def button_rock():
    player_choice_rock= Label(
        root, 
        text="You have Selected Rock, The Computer selected: " + comp_choice
        )
    player_choice_rock.grid(row=2,column=1)

    if comp_choice == "Paper":
        lose= Label(root, text="You have lost")
        lose.grid(row=3,column=1)
    if comp_choice == "Scissors":
        win = Label(root, text="You have won")
        win.grid(row=3, column=1)
    if comp_choice == "Rock":
        draw = Label(root, text="Its a draw")
        draw.grid(row=3, column=1)

    def restart():
        return
    play_again= Button(root, text="Play Again?", command=restart)
    play_again.grid(row=0, column=2)
    
    def done():
        if root is not None:
            root.destroy()
        return
    exit_game= Button(root, text="Exit", padx=40, pady=20,command=done)
    exit_game.grid(row=4, column=1)
    
    

def button_paper():
    player_choice_paper= Label(
    root, 
    text="You have Selected Paper, The Computer selected: " + comp_choice
    )
    player_choice_paper.grid(row=2,column=1)

    if comp_choice == "Scissors":
        lose= Label(root, text="You have lost")
        lose.grid(row=3,column=1)
    if comp_choice == "Rock":
        win = Label(root, text="You have won")
        win.grid(row=3, column=1)
    if comp_choice == "Paper":
        draw = Label(root, text="Its a draw")
        draw.grid(row=3, column=1)
    def restart():
        return
    play_again= Button(root, text="Play Again?", command=restart)
    play_again.grid(row=0, column=2)
    
    def done():
        if root is not None:
            root.destroy()
        return
    exit_game= Button(root, text="Exit", padx=40, pady=20,command=done)
    exit_game.grid(row=4, column=1)
    
    

def button_scissors():
    player_choice_scissors= Label(
    root, 
    text="You have Selected Scissors, The Computer selected: " + comp_choice
    )
    player_choice_scissors.grid(row=2,column=1)

    if comp_choice == "Rock":
        lose= Label(root, text="You have lost")
        lose.grid(row=3,column=1)
    if comp_choice == "Paper":
        win = Label(root, text="You have won")
        win.grid(row=3, column=1)
    if comp_choice == "Scissors":
        draw = Label(root, text="It's a draw")
        draw.grid(row=3, column=1)
        
    def restart():
        return
    play_again= Button(root, text="Play Again?", command=restart)
    play_again.grid(row=0, column=2)
    
    def done():
        if root is not None:
            root.destroy()
        return
    exit_game= Button(root, text="Exit", padx=40, pady=20,command=done)
    exit_game.grid(row=4, column=1)
    

#Create Buttons

rock=Button(root, text="ROCK", padx=40, pady=20, command=button_rock )
paper=Button(root, text="PAPER",padx=40, pady=20, command=button_paper)
scissors=Button(root,text="SCISSORS", padx=40,pady=20, command=button_scissors)

#place buttons/labels
start.grid(row=0, column=0, columnspan=3)
rock.grid(row=1, column=0)
paper.grid(row=1, column=1)
scissors.grid(row=1, column=2)



root.mainloop()