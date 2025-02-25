import PIL
from PIL import Image,ImageTk
import threading
import pygame,time
import tkinter as tk
pygame.mixer.pre_init(44100, -16, 2, 2048)
parent=tk.Tk()
parent.withdraw()
pygame.mixer.init()
pygame.mixer.music.load("Rickroll.MP3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()
def show_image():
   top=tk.Toplevel()
   img=Image.open("Rickroll.jpg")
   img=img.resize((310,160))
   img=ImageTk.PhotoImage(img)
   image_label=tk.Label(top,image=img)
   top.image=img 
   top.title("RICK YOU!")
   top.geometry("350x250")
   image_label.pack(pady=20,padx=20)
 
def Malrick():
 while pygame.mixer.music.get_busy():
       show_image()
       time.sleep(2)
      
song_thread=threading.Thread(target=Malrick)
song_thread.start()
       
    
    
    
parent.mainloop()
    
    
    