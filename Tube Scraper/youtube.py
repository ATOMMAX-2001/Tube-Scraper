# AUTHOR : S.ABILASH

from pytube import YouTube
import  tkinter as tk
from tkinter import ttk
from pytube.cli import on_progress


def get_frame():
	frame = tk.Tk()
	frame.title("Tube Scraper ~ S.ABILASH")

	frame_height=100
	frame_width=400

	screen_width=frame.winfo_screenwidth()
	screen_height=frame.winfo_screenheight()

	center_position_x_axis=int(screen_width/2 - frame_width/2)
	center_position_y_axis=int(screen_height/2 - frame_height/2)

	frame.geometry(f"{frame_width}x{frame_height}+{center_position_x_axis}+{center_position_y_axis}")
	frame.resizable(False,False)
	try:
		frame.iconbitmap("youtube.ico")
	except:
		print("Cant Able To Put Icon")
	return frame

def window_panel(window):
	name=tk.StringVar()
	save_path=tk.StringVar()

	text_box=ttk.Entry(window,width=50,textvariable=name)
	text_box.grid(column=95,row=3)
	
	save_box=ttk.Entry(window,width=50,textvariable=save_path)
	save_box.grid(column=95,row=6)

	text_label=ttk.Label(window,text="URL")
	text_label.config(font=("Courier",14))
	text_label.grid(column=0,row=3)

	save_label=ttk.Label(window,text="Savepath")
	save_label.config(font=("Courier",14))
	save_label.grid(column=0,row=6)


	#download button
	download_button=ttk.Button(window,text="Download",command=lambda:download_tube_for_me(name.get(),save_path.get()))
	download_button.grid(column=95,row=7)
	return window

def download_tube_for_me(url,path):
	if(len(url)==0):
		print("Empty Url")
	else:
		yt=YouTube(url,on_progress_callback=on_progress)
		print("*****************************************\n")
		print(f"Title: {yt.title}")
		print("*****************************************\n")
		print(f"Author: {yt.author}")
		print("*****************************************\n")
		print(f"Total Length {yt.length}")
		print("*****************************************\n")
		print(f"Description:\n{yt.description}")
		print("*****************************************\n")
		print(f"Rating: {yt.rating}")
		print("*****************************************\n")

		#start downloading
		print("Fetching.....\n")
		print("Please Wait!!")
		print("Downloading......\n")
		yt.streams.first().download(output_path=path)

def main():
	window=get_frame()
	window=window_panel(window)
	window.mainloop()


if(__name__=="__main__"):
	print("TUBE SCRAPER ~ S.ABILASH")
	main()