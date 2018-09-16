from tkinter import *

import sort

weight = 0.5
def set_weight(val):
	global weight
	weight = float(val) / 100.0
	write_weight()

def write_weight():
    global weight
    with open('weights.txt', 'w+') as file:
        file.write(str(weight))

def gen_sliders():
	master = Tk()
	master.geometry("500x160")
	master.configure(background='#3399ff')

	T = Text(master, height=2, width=30)
	T.tag_configure("center", justify='center')
	T.pack()
	T.insert(END, "Set the Mood\n")
	T.tag_add("center", "1.0", "end")

	T = Text(master, height=1, width=30, bg='#3399ff', borderwidth=0, highlightthickness=0)
	T.tag_configure("center", justify='center')
	T.pack()
	T.insert(END, "")
	T.tag_add("center", "1.0", "end")


	T = Text(master, height=2, width=30)
	T.tag_configure("center", justify='center')
	T.pack()
	T.insert(END, "<- Chill | Hype ->")
	T.tag_add("center", "1.0", "end")
	slider = Scale(master, 
				from_=0, 
				to=100, 
				bg='black',
				activebackground='black',
				showvalue=0, 
				orient=HORIZONTAL, 
				borderwidth=0, 
				highlightthickness=0, 
				highlightcolor='#d6e0f5', 
				highlightbackground='#d6e0f5', 
				troughcolor='#d6e0f5', 
				width=30, 
				sliderrelief='solid',
				command=set_weight)
	slider.set(50)
	slider.pack(fill=X, padx=10, pady=10)

	mainloop()

gen_sliders()
