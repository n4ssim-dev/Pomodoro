# Imports
import tkinter
import math

# Global Scope

COLORS = {
    'PINK' : "#e2979c",
    'RED' : "#e7305b",
    'GREEN' : "#9bdeac",
    'YELLOW' : "#f7f5dd"
}
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKMARK = "✔️"
TIMER = ""

# Gestion des évènements après avoir appuyer sur reset
def reset_pomodoro():
    global REPS
    REPS = 0
    canvas.itemconfig(tomato_timer, text="00:00")
    title.config(text="Timer", fg=COLORS["GREEN"])
    window.after_cancel(TIMER)

# Gestion des événements après avoir appuyer sur start
def start_pomodoro():
    global REPS

    REPS += 1

    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if REPS % 2 != 0 and REPS <= 7:
        title.config(text="Work", fg=COLORS["PINK"])
        countdown(work_sec)
        actualise_checks()
    elif REPS % 2 == 0 and REPS <= 6:
        title.config(text="Break(S)", fg=COLORS["RED"])
        countdown(short_break)
        actualise_checks()
    elif REPS == 8:
        title.config(text="Break(L)", fg=COLORS["GREEN"])
        countdown(long_break)
        actualise_checks()

# Actualisation du compteur
def countdown(count):
    global REPS, TIMER

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(tomato_timer,text=f"{minutes}:{seconds}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    elif count == 0:
        start_pomodoro()

# Actualisation des checkmarks en bas du timer
def actualise_checks():
    checkmarks = CHECKMARK * (int(REPS / 2))
    pomodoro_icon.config(text=checkmarks)
    
    
# Window
window = tkinter.Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=COLORS["YELLOW"])

# Titre
title = tkinter.Label(text="Timer",fg=COLORS["GREEN"],bg=COLORS["YELLOW"],font=(FONT_NAME,32,"bold"))
title.grid(column=1,row=0)

# Image de tomate avec le timer
canvas = tkinter.Canvas(width=200,height=224,bg=COLORS["YELLOW"],highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tomato_img)
tomato_timer = canvas.create_text(103,129,text="00:00",font=(FONT_NAME,28,"bold"),fill="white")
canvas.grid(column=1,row=1)

# Boutons
start_button = tkinter.Button(text="Start",command=start_pomodoro,highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text="Reset",command=reset_pomodoro,highlightthickness=0)
reset_button.grid(column=2,row=2)

# Pomodoros complétés
pomodoro_icon = tkinter.Label(text=CHECKMARK * REPS,fg=COLORS["GREEN"],bg=COLORS["YELLOW"],font=(FONT_NAME,13,"bold"))
pomodoro_icon.grid(column=1,row=3)

window.mainloop()