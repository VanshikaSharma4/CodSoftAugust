from tkinter import *
from PIL import Image, ImageTk
from random import randint


root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="purple")

rock_img = ImageTk.PhotoImage(Image.open("user_rock.png"))
paper_img = ImageTk.PhotoImage(Image.open("user_paper.png"))
scissor_img = ImageTk.PhotoImage(Image.open("user_scissor.png"))
comp_rock_img = ImageTk.PhotoImage(Image.open("computer_rock.png"))
comp_paper_img = ImageTk.PhotoImage(Image.open("computer_paper.png"))
comp_scissor_img = ImageTk.PhotoImage(Image.open("computer_scissor.png"))


user_label = Label(root, image=scissor_img, bg="purple")
comp_label = Label(root, image=comp_scissor_img, bg="purple")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

PlayerScore = Label(root, text=0, font=("verdana", 20, "bold"), bg="purple", fg="white")
ComputerScore = Label(
    root, text=0, font=("verdana", 20, "bold"), bg="purple", fg="white"
)
ComputerScore.grid(row=1, column=1)
PlayerScore.grid(row=1, column=3)

user_indicator = Label(
    root, font=("verdana", 15, "bold"), text="USER", bg="purple", fg="white"
)
computer_indicator = Label(
    root,
    font=("verdana", 15, "bold"),
    text="COMPUTER",
    bg="purple",
    fg="white",
)
user_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)

message = Label(root, font=50, bg="purple", fg="white")
message.grid(row=4, column=2)


def updateMsg(x):
    message["text"] = x


def updateUserScore():
    score = int(PlayerScore["text"])
    score += 1
    PlayerScore["text"] = str(score)


def updateCompScore():
    score = int(ComputerScore["text"])
    score += 1
    ComputerScore["text"] = str(score)


def checkWin(player, computer):
    if player == computer:
        updateMsg("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            updateMsg("You Lose:)")
            updateCompScore()
        else:
            updateMsg("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMsg("You Lose:)")
            updateCompScore()
        else:
            updateMsg("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMsg("You Lose:)")
            updateCompScore()
        else:
            updateMsg("You Win")
            updateUserScore()
    else:
        pass


choice = ["rock", "paper", "scissor"]


def updateChoice(x):
    compChoice = choice[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=comp_rock_img)
    elif compChoice == "paper":
        comp_label.configure(image=comp_paper_img)
    else:
        comp_label.configure(image=comp_scissor_img)

    if x == "rock":
        user_label.config(image=rock_img)
    elif x == "paper":
        user_label.config(image=paper_img)
    else:
        user_label.config(image=scissor_img)

    checkWin(x, compChoice)


rock = Button(
    root,
    width=20,
    height=2,
    text="ROCK",
    font=("verdana", 10, "bold"),
    bg="#FF3E4D",
    fg="white",
    command=lambda: updateChoice("rock"),
).grid(row=2, column=1)
paper = Button(
    root,
    width=20,
    height=2,
    text="PAPER",
    font=("verdana", 10, "bold"),
    bg="#FAD02E",
    fg="white",
    command=lambda: updateChoice("paper"),
).grid(row=2, column=2)
scissor = Button(
    root,
    width=20,
    height=2,
    text="SCISSOR",
    font=("verdana", 10, "bold"),
    bg="#0ABDE3",
    fg="white",
    command=lambda: updateChoice("scissor"),
).grid(row=2, column=3)


root.mainloop()
