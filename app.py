from tkinter import *
from PIL import Image, ImageTk
import os

from main import make_scramble, reset_csv_img
from Scramble_generator import scramble_generator

#Set Window
root = Tk()
root.title("Rubik's Cube")
canvas = Canvas(root, width=900, height=750)
canvas.grid(columnspan=7, rowspan=12)

#img Display


def upd_cube_img():

	g_cube_img = ImageTk.PhotoImage(Image.open(os.path.join('Media', '-----Final-----.jpg')))
	cube_label.configure(image=g_cube_img)
	cube_label.image = g_cube_img


cube_img = ImageTk.PhotoImage(Image.open(os.path.join('Media', 'Reset_cube.jpg')))
cube_label = Label(image=cube_img)
cube_label.grid(column=0, row=0, sticky=NW, rowspan=12, columnspan=5)


#Text Box
text_box = Text(root, height=15, width=78)
text_box.grid(column=0, row=10, sticky=N, columnspan=5)

#Middle labels
g_labels = Label(root, text='Auto-generate a scramble', width=20)
g_labels.grid(column=5, row=4, columnspan=2)

ins_scramble = Label(root, text='Insert a scramble')
ins_scramble.grid(column=5, row=7, columnspan=2)

#Reset img button


def reset():

	reset_cube_img = ImageTk.PhotoImage(Image.open(os.path.join('Media', 'Reset_cube.jpg')))
	cube_label.configure(image=reset_cube_img)
	cube_label.image = reset_cube_img

	reset_csv_img()
	text_box.delete('1.0', END)

	upd_cube_img()


reset_img_btn = Button(root, text='Reset Cube', command=reset, bg='#00ff4c', fg='#000000', activebackground='#29c40e', height=2, width=15, font='Helveltica')
reset_img_btn.grid(column=5, row=2, columnspan=2)

#Buttons and selectors Section

#Length selector
len_scramble_sp = Spinbox(root, from_=0, to_=300)
len_scramble_sp.grid(column=5, row=5, columnspan=2, sticky=N)

#Auto-scrambler generator


def new_scramble():

	strscramble = scramble_generator(int(len_scramble_sp.get()))
	make_scramble(strscramble)

	text_box.delete('1.0', END)
	text_box.insert(END, strscramble)

	upd_cube_img()


generate_btn = Button(root, text='Auto-generate', command=new_scramble)
generate_btn.grid(column=5, row=6, columnspan=2, sticky=N)

#Insert a scramble


def get_scramble():

	strscramble = str(scramble_text.get())
	make_scramble(strscramble)

	text_box.delete('1.0', END)
	text_box.insert(END, strscramble)

	upd_cube_img()


scramble_text = Entry(root, width=30)
scramble_text.grid(column=5, row=8, columnspan=2)

scramble_btn = Button(root, text='Generate', command=get_scramble)
scramble_btn.grid(column=5, row=9, columnspan=2)


#Clock Function
clock = 0


def start_clock(raw_time=0):

	global clock

	if raw_time >= 1000:
		time['text'] = (str(raw_time)[:-3] + ':' + str(raw_time)[-3:])

	else:
		time['text'] = ('0' + ':' + str(raw_time)[-3:])

	clock = time.after(1, start_clock, (raw_time + 1))


def stop_clock():
	global clock
	try:
		time.after_cancel(clock)
	except:
		ValueError


time = Label(root, fg='black', width=10, font=("", "40"))
time.grid(column=5, row=0, columnspan=2)


#Clock Buttons
reset_time_btn = Button(root, text='Reset Time', command=start_clock, bg='#f6ff00', fg='#000000', activebackground='red', height=2, width=10, font='Helveltica')
reset_time_btn.grid(column=5, row=1)

stop_time_btn = Button(root, text='Stop Time', command=stop_clock, bg='#f6ff00', fg='#000000', activebackground='#f7c10f', height=2, width=10, font='Helveltica')
stop_time_btn.grid(column=6, row=1)

root.mainloop()
