from tkinter import *
import random as rn
from tkinter import messagebox

wordslist=['ability', 'able', 'about', 'above', 'abroad', 'accept', 'access', 'account', 'act', 'add', 'admit', 'adopt', 'adult', 'age', 'again', 'ado', 'agree', 'aid', 'apart', 'apply', 'art', 'ask', 'assign', 'bag', 'badly', 'bake', 'ball', 'ban', 'bar', 'battle', 'bean', 'beat', 'beautiful', 'chip', 'cat', 'church', 'cite', 'citizen', 'claim', 'clearly', 'client', 'clean', 'clinic', 'code', 'college', 'computer', 'cop', 'cycle', 'dish', 'door', 'divorce', 'during', 'drag', 'drama', 'dress', 'drink', 'education', 'editor', 'economics', 'effort', 'elite', 'embrace', 'employ', 'enable', 'enhance', 'engineer', 'even', 'exactly', 'expose', 'extreme', 'farm', 'factor', 'fault', 'favour', 'fight', 'firm', 'foreign', 'framework', 'frustation', 'fundamental', 'furthermore', 'gain', 'garden', 'generally', 'green', 'grocery', 'guarantee', 'guilty', 'guy', 'habit', 'hall', 'handful', 'hear', 'heaven', 'heritage', 'highway', 'historian', 'horizon', 'hundred', 'identification', 'ignore', 'illegal', 'imagination', 'immediately', 'immigration', 'implement', 'independence', 'indicate', 'innocent', 'instead', 'instrument', 'iron', 'japan', 'jewish', 'journal', 'judge', 'junior', 'justify', 'knee', 'knowledge', 'king', 'kind', 'knock', 'label', 'large', 'last', 'late', 'lawn', 'leather', 'legacy', 'legend', 'lemon', 'lenght', 'look', 'lost', 'lovely', 'lung', 'main', 'major', 'man', 'mark', 'match', 'mind', 'mood', 'mostly', 'nature', 'near', 'never', 'nut', 'nowhere', 'notice', 'nose', 'none', 'nomination', 'occur', 'occassion', 'obtain', 'observe', 'odd', 'offer', 'opinion', 'origin', 
'other', 'owner', 'pain', 'paint', 'parent', 'passage', 'payment', 'penalty', 'permission', 'persuade', 'philosophy', 'phase', 'pocket', 'pool', 'post', 'pregnant', 'profile', 'profit', 'proof', 'prove', 'punishment', 'push', 'quiet', 'question', 'quit', 'quiet', 'quarterback', 'race', 'racial', 'raise', 'range', 'rapidly', 'rarely', 'reaction', 'reading', 'resonable', 'recognition', 'recommend', 'relief', 'remind', 'report', 'resist', 'road', 'rope', 'run', 'sale', 'satisfy', 'scheme', 'scope', 'script', 'seize', 'senate', 'serve', 'shade', 'shoe', 'silence', 'similar', 'smart', 'score', 'talk', 'theater', 'test', 'tall', 'troop', 'tribe', 'tremendous', 'tunnel', 'typically', 'truth', 'unfortunately', 'unkown', 'upper', 'unlikely', 'university', 'utility', 'versus', 'veteran', 'village', 'voice', 'virus', 'virtue', 'vulnerable', 'volunteer', 'walk', 'week', 'welcome', 'weight', 'whisper', 'widespread', 'willing', 'wing', 'winner', 'window', 'wife', 'wild', 'withdraw', 'yard', 'year', 'yellow', 'young', 'yeild', 'yes', 'your', 'yell', 'yeah', 'zone', 'zoo', 'zebra', 'zombie']
print(len(wordslist))
score=0
timeleft=60

app=Tk()
app.title('Type master game')
app.geometry('700x700')
app.iconbitmap("F:\python programs\GUI\keyboard.ico")
app.config(bg='white')
app.resizable(0,0)

def ngame():
    global timeleft,score
    timeleft=60
    runningtime.config(text='TIMELEFT: '+str(timeleft))
    b.config(state=DISABLED)
    words.config(text='PRESS ENTER TO START GAME!',fg='#3333cc')
    e.config(state=DISABLED)

def nextword(event):
    global score,timeleft
    if timeleft==60:
        countdown()
    if timeleft>0:
        e.config(state=NORMAL)
        timeleft-=1
        if e.get().upper()==words['text'].upper():
            score+=1
        e.delete(0,END)
        words.config(text=wordslist[rn.randint(0,len(wordslist)-1)].upper())

def countdown():
    global timeleft,score
    if timeleft>0:
        timeleft-=1
        runningtime.config(text="TIME LEFT : "+str(timeleft))
        runningtime.after(1000,countdown)
    else:
        b.config(state=NORMAL)
        words.config(text='GAME OVER',fg='red')
        e.delete(0,END)
        e.config(state=DISABLED)
        messagebox.showinfo('CONGRATULATIONS','YOUR SCORE IS '+str(score))
        score=0 

#Game frame
f1=Frame(app,bg='#9999ff',width=100,height=100)
f1.pack(pady=(10,0),padx=10)

#Labels frame
lblframe=Frame(f1,bg='#ff99cc',width=100,height=100)
lblframe.pack(pady=10,padx=10)

#ff99cc
instructions=Label(lblframe,font=('Forte',30),text='SPEED TYPING TEST',bg='#ff99cc',fg='#cc00ff')
instructions.pack(pady=(10,0),padx=10)

words=Label(lblframe,text='WORDS APPEAR HERE',font=('Rockwell Extra Bold',22),bg='#ff99cc',fg='#00994d')
words.pack(pady=(10,0),padx=10)

runningtime=Label(lblframe,text='TIME LEFT: '+str(timeleft),font=('Cooper Black',26),bg='#ff99cc',fg='#cc0000')
runningtime.pack(pady=10,padx=10)

img=PhotoImage(file='F:/python programs/GUI/numberpad_keys.gif')
Label(lblframe,image=img,bg='white').pack(pady=(10,0))

#buttonimg=PhotoImage(file='C:/Users/new/OneDrive/Desktop/button1.png')

e=Entry(f1,font=('Berlin Sans FB',20),state=DISABLED,justify=CENTER,width=45)
e.pack(pady=10,padx=10)
e.bind('<Return>',nextword)
e.focus_set()

b=Button(f1,font=('sans-serif, bold',10),text="New game",bg='black',fg='white',state=DISABLED,command=ngame)
b.pack(pady=10,padx=10)

app.mainloop()
