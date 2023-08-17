from tkinter import *
root = Tk()
root.configure(bg="lightblue")

lab=Label(root, text="Rock / Paper /Scissors : Enter - [r] [p] [s]",bg="lightblue")
lab.grid(row=0,column=1,padx=15,pady=15)

lab3=Label(root,text="Player 1 :", width=25,bg="lightblue")
lab3.grid(row=1,column=0)

lab4=Label(root, text="Player 2 :", width=25,bg="lightblue")
lab4.grid(row=1,column=2)

lab5=Label(root,text="Wins :",width=25,bg="lightblue")
lab5.grid(row=3,column=0)

lab6=Label(root,text="Wins :",width=25,bg="lightblue")
lab6.grid(row=3,column=2)

lab7=Label(root,text="Draws :",width=25,bg="lightblue")
lab7.grid(row=6,column=0)

inpu=Entry(root, width=20, fg="lightblue",bg="lightblue",relief="groove")
inpu.grid(row=2,column=0)

inp=Entry(root, width=20, fg="lightblue",bg="lightblue",relief="groove")
inp.grid(row=2,column=2)

player1_wins=0
player2_wins=0
draws=0

lab2 = Label(root)

def r_p_s():
    p1=inpu.get()
    p2=inp.get()
    global player1_wins
    global player2_wins
    global draws
    global wins1
    global wins2
    global draw

    global lab2
    lab2.grid_forget()
    
    if p1==p2:
        lab2=Label(root, text="Draw",relief="flat",bg="lightblue")
        lab2.grid(row=4,column=1)
        draws+=1
            
    elif p1=='r' and p2=='s':
        player1_wins+=1
        lab2=Label(root, text="Player 1 Won",relief="flat",bg="lightblue")
        lab2.grid(row=4,column=1)        
                   
    elif p1=='s' and p2=='p':
        lab2=Label(root, text="Player 1 Won",bg="lightblue",relief="flat")
        lab2.grid(row=4,column=1)
        player1_wins+=1
        
    elif p1=='p' and p2=='r':
        lab2=Label(root, text="Player 1 Won",bg="lightblue",relief="flat")
        lab2.grid(row=4,column=1)
        player1_wins+=1
        

    elif p1=='s' and p2=='r':
        lab2=Label(root, text="Player 2 Won",bg="lightblue",relief="flat")
        lab2.grid(row=4,column=1)
        player2_wins+=1
        
    elif p1=='p' and p2=='s':
        lab2=Label(root, text="Player 2 Won",bg="lightblue",relief="flat")
        lab2.grid(row=4,column=1)
        player2_wins+=1
        
    elif p1=='r' and p2=='p':
        lab2=Label(root, text="Player 2 Won",bg="lightblue",relief="flat")
        lab2.grid(row=4,column=1)
        player2_wins+=1
        
    wins1=Entry(root,width=5,relief="flat",bg="lightblue")
    wins1.grid(row=4,column=0)
    wins1.insert(0,player1_wins)

    wins2=Entry(root,width=5,relief="flat",bg="lightblue")
    wins2.grid(row=4,column=2)
    wins2.insert(0,player2_wins)

    draw=Entry(root,width=5,relief="flat",bg="lightblue")
    draw.grid(row=7,column=0)
    draw.insert(0,draws)

    inpu.delete(0,END)
    inp.delete(0,END)


final=Label(root)
def endf():
    global final
    global player1_wins
    global player2_wins
    global draws
    global wins1
    global wins2
    global draw
    global lab2
    
    final.grid_forget()
    if (player1_wins>player2_wins and player1_wins > draws):
        final=Label(root,justify="center",width=30,text="Player 1 Wins The Game !!",bg="light blue")
        final.grid(row=7,column=1)
    elif (player2_wins>player1_wins and player2_wins>draw):
        final=Label(root,justify="center",width=30,text="Player 2 Wins The Game !!",bg="light blue")
        final.grid(row=7,column=1)
    else:
        final=Label(root,justify="center",width=30,text="It's a Tie!!",bg="light blue")
        final.grid(row=7,column=1)
    player1_wins=0
    player2_wins=0
    draws=0

    wins1.delete(0,END)
    wins2.delete(0,END)
    draw.delete(0,END)

    lab2.grid_forget()
    

def quitf():
    quit()

but=Button(root, text="Play",command=r_p_s,width=10,height=2)
but.grid(row=3,column=1)

but2=Button(root,text="Quit",command=quitf)
but2.grid(row=8,column=2)

but3=Button(root, text="End Game",command=endf)
but3.grid(row=8,column=1)

root.mainloop()
