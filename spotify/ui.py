from tkinter import *

import sort

weights = {}
def set_lively(val):
	global weights
	weights['liveliness'] = val

def set_acoustic(val):
	global weights
        weights['acoustic'] = val

def set_dance(val):
	global weights
	weights['danceability'] = val

def gen_sliders():
	master = Tk()
	master.geometry("500x500")
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
	T.insert(END, "Lively\n")
	T.tag_add("center", "1.0", "end")
	lively = Scale(master, 
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
				command=set_lively)
	lively.pack(fill=X, padx=10, pady=10)

	T = Text(master, height=2, width=30)
	T.tag_configure("center", justify='center')
	T.pack()
	T.insert(END, "Acoustic\n")
	T.tag_add("center", "1.0", "end")
	acoustic = Scale(master, 
				from_=0, 
				to=100, 
				bg='black',
				activebackground='black',
				showvalue=0, 
				orient=HORIZONTAL, 
				borderwidth=0, 
				highlightthickness=0, 
				highlightcolor='#e6f2ff', 
				highlightbackground='#e6f2ff', 
				troughcolor='#e6f2ff', 
				width=30, 
				sliderrelief='solid',
				command=set_acoustic)
	acoustic.pack(fill=X, padx=10, pady=10)

	T = Text(master, height=2, width=30)
	T.tag_configure("center", justify='center')
	T.pack()
	T.insert(END, "Dance\n")
	T.tag_add("center", "1.0", "end")
	dance = Scale(master, 
				from_=0, 
				to=100, 
				bg='black',
				activebackground='black',
				showvalue=0, 
				orient=HORIZONTAL, 
				borderwidth=0, 
				highlightthickness=0, 
				highlightcolor='#e6f2ff', 
				highlightbackground='#e6f2ff', 
				troughcolor='#e6f2ff', 
				width=30, 
				sliderrelief='solid',
				command=set_dance)
	dance.pack(fill=X, padx=10, pady=10)

	sliders = [lively, acoustic, dance]
	mainloop()
