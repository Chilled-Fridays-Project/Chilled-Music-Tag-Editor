#!/usr/bin/env python
# coding: utf-8

# In[3]:


from mutagen.id3 import APIC,ID3,Encoding,TIT2,TPE1,TPE2,TALB,TYER,TCON,TRCK,TCOM
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
import io
from io import BytesIO
from tkinter.filedialog import askopenfile
from tkinter import *
import tkinter as tk
import os
from pygame import mixer
from tkinter import ttk
from PIL import ImageTk,Image

root=tk.Tk()

canvas=tk.Canvas(master=root,width=500,height=700)

canvas.pack()

im = Image.open("Chilled Music Tag Editor  logo Blue.jpg")
default=im.resize((250,250),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(master=root,image=default)
#canvas.create_image(250,209,image=photo)
panel=tk.Label(root,image=photo)

canvas.create_window(150,150, window=panel)

#Tags
alb=Image.open("album2.png")
album_txt=ImageTk.PhotoImage(master=root,image=alb)
canvas.create_image(50,457,image=album_txt)

artist=Image.open("Artist.png")
artist_txt=ImageTk.PhotoImage(master=root,image=artist)
space=45
canvas.create_image(50,457-2*space,image=artist_txt)

alb_artist=Image.open("Album_artist 2.png")
alb_artist_txt=ImageTk.PhotoImage(master=root,image=alb_artist)
canvas.create_image(50,457-space,image=alb_artist_txt)

song_title=Image.open("Title.png")
song_title_txt=ImageTk.PhotoImage(master=root,image=song_title)
canvas.create_image(50,457-3*space,image=song_title_txt)

year=Image.open("Year.png")
year_txt=ImageTk.PhotoImage(master=root,image=year)
canvas.create_image(50,457+space,image=year_txt)

genre=Image.open("Genre.png")
genre_txt=ImageTk.PhotoImage(master=root,image=genre)
canvas.create_image(50,457+2*space,image=genre_txt)

Track_Number=Image.open("Track Number.png")
Track_Number_txt=ImageTk.PhotoImage(master=root,image=Track_Number)
canvas.create_image(50,457+3*space,image=Track_Number_txt)

composer=Image.open("Composer.png")
composer_txt=ImageTk.PhotoImage(master=root,image=composer)
canvas.create_image(50,457+4*space,image=composer_txt)
cover_id=tk.StringVar()
song_name=tk.Label(root,text="",fg="white",bg="black")
canvas.create_window(250,290,window=song_name)
def open_song():
    
    try:
        global s
        
        global s2
        
        global link
        
        global s_m4a
        global filename
        global file_format
        song=askopenfile()
        link=song.name
        filename=os.path.basename(song.name)
        song_name.configure(text=filename)

        entry3.delete(0,"end")
        entry2.delete(0,"end")
        entry5.delete(0,"end")
        entry1.delete(0,"end")
        entry4.delete(0,"end")
        entry6.delete(0,"end")
        entry7.delete(0,"end")
        entry8.delete(0,"end")
        
        if filename.endswith('.mp3'):
            
            s=MP3(link)        
            s2=ID3(link)        
            for i,j in enumerate(s.keys()):

                if "APIC:" in j:
                    o=j
                    cover_id.set(o)



                elif "TPE1" in j:
                    #entry2.clipboard_clear()
                    entry2.insert(0,s.get("TPE1").text[0])



                elif "TPE2" in j:

                    entry3.insert(0,s.get("TPE2").text[0])



                elif "TDRC" in j:

                    entry5.insert(0,s.get("TDRC").text[0])

                elif "TCON" in j:

                    entry6.insert(0,s.get("TCON").text[0])

                elif "TALB" in j:

                    entry4.insert(0,s.get("TALB").text[0])

                elif "TIT2" in j:
                    entry1.insert(0,s.get("TIT2").text[0]) 
                elif "TRCK" in j:
                    entry7.insert(0,s.get("TRCK").text[0]) 

                elif "TCOM" in j:
                    entry8.insert(0,s.get("TCOM").text[0]) 
            im=Image.open(BytesIO(s.get(o).data))
            
        elif filename.endswith(".m4a"):
            s_m4a=MP4(link)
            for i,j in enumerate(s_m4a.keys()):
                
                if '©ART' in j:
                    
                    entry2.insert(0,s_m4a.get('©ART')[0])
                
                elif 'aART' in j:
                    
                    entry3.insert(0,s_m4a.get('aART')[0])
                    
                elif '©day' in j:
                    
                    entry5.insert(0,s_m4a.get('©day')[0])
                                  
                elif '©gen' in j:
                    
                    entry6.insert(0,s_m4a.get('©gen')[0])
                
                elif '©alb' in j:
                    
                    entry4.insert(0,s_m4a.get('©alb')[0])
                
                elif '©nam' in j:
                                  
                    entry1.insert(0,s_m4a.get('©nam')[0])
                                  
                elif '©wrt' in j:
                      
                    entry8.insert(0,s_m4a.get('©wrt')[0])   
                    
                elif 'trkn' in j:
                    trck_num=str(s_m4a.get('trkn')[0]).replace(", ","/")
                    
                    trck_num=trck_num.replace("(","")
                    trck_num=trck_num.replace(")","")
                   
                    
                    entry7.insert(0, trck_num)                                   
                                  
                    
                    
            
            im=Image.open(BytesIO(s_m4a.get('covr')[0]))
        #im=Image.open(BytesIO(s.get(o).data))
        
        im=im.crop()
        im=im.resize((250,250),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(master=root,image=im)
        #canvas.create_image(250,209,image=photo)
        panel.configure(image=photo)
        panel.image=photo  
        
        
    except:
    
        #im = Image.open("C:\\Users\\THULARE KABELO\\Documents\\Business\\Chilled Fridays Listening Sessions\\t_shirt\\LOGO\\New T- Shirt\\T-Shirt Red New.jpg")
        #im=im.crop()
        #im=im.resize((250,250),Image.ANTIALIAS)

        photo=ImageTk.PhotoImage(master=root,image=default)
        panel.configure(image=photo)
        panel.image=photo
        

def cover_art():
    try:
        global image_bytes
        global pic_format
        coverart=askopenfile()
        art_link=coverart.name
        pic_type=os.path.basename(art_link)
        
        pic_format="JPEG"
        if pic_type.endswith("png"):
            pic_format="PNG"
        pic=Image.open(art_link)
        output=BytesIO()
        
        pic.save(output,format=pic_format)
        image_bytes=output.getvalue()
        if filename.endswith('.mp3'):
            global s
            s=MP3(link)
            for i,j in enumerate(s.keys()):

                if "APIC:" in j:
                    cover_id.set(j)
                    s2.setall(cover_id.get(),[]) #clearing existing Cover

                    s2.save()
                    break


            if pic_format=="JPEG":

                s2.add(APIC(encoding=3,mime='image/jpeg',type=3, desc='', data=image_bytes))

            elif pic_format=="PNG":  
                s2.add(APIC(encoding=3,mime='image/png',type=3, desc='', data=image_bytes))

        #s2.save()
        #s.add_tags(APIC(encoding=0,mime='image/jpeg',type=0, desc='', data=image_bytes))
        #s.save()
        #im=Image.open(BytesIO(s2.get("APIC:").data))
        im=Image.open(BytesIO(image_bytes))
        im=im.crop()
        im=im.resize((250,250),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(master=root,image=im)
        #canvas.create_image(250,209,image=photo)
        panel.configure(image=photo)
        panel.image=photo  
    except:
                
        
        s.get(cover_id.get()).data=image_bytes
        s.save()
        im=Image.open(BytesIO(s.get("APIC:").data))
        im=im.crop()
        im=im.resize((250,250),Image.ANTIALIAS)
        photo=ImageTk.PhotoImage(master=root,image=im)
        #canvas.create_image(250,209,image=photo)
        panel.configure(image=photo)
        panel.image=photo  

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground        
#Open SOng Button

Open_Track=HoverButton(master=canvas,fg="white",bg="white",activebackground="#4bdf81",width=140,height=30, bd=0,command=open_song)    
canvas.create_window(400,50,window=Open_Track)

open_image=Image.open("open button.png")
open_image_txt=ImageTk.PhotoImage(master=root,image=open_image)
canvas.create_image(400,50,image=open_image_txt)
Open_Track.configure(image=open_image_txt,compound=CENTER)

#ADD ARTWORK BUTTON

ArtWork=HoverButton(master=canvas,fg="white",bg="white",activebackground="#c97ad7",width=140,height=30, bd=0,command=cover_art)
canvas.create_window(400,250,window=ArtWork)

cover_image=Image.open("Add Cover.png")
cover_image_txt=ImageTk.PhotoImage(master=root,image=cover_image)
canvas.create_image(400,250,image=cover_image_txt)
ArtWork.configure(image=cover_image_txt,compound=CENTER)
root.title("Chilled Music Tag Editor")

entry1=tk.Entry(root,width=80)

canvas.create_window(250,330,window=entry1)  
#canvas.create_text(34,310,text="Song Title:")

entry2=tk.Entry(root,width=80)

canvas.create_window(250,330+45,window=entry2)  
#canvas.create_text(25,310+45,text="Artist:")

entry3=tk.Entry(root,width=80)

canvas.create_window(250,330+45+45,window=entry3)  
#canvas.create_text(42,310+45+45,text="Album Artist:")

entry4=tk.Entry(root,width=80)

canvas.create_window(250,330+45+45+45,window=entry4)  
#canvas.create_text(26,310+45+45+45,text="Album:")

entry5=tk.Entry(root,width=80)

canvas.create_window(250,330+45+45+45+45,window=entry5)  
#canvas.create_text(24,310+45+45+45+45,text="Year:")

entry6=tk.Entry(root,width=80)

canvas.create_window(250,330+45+45+45+45+45,window=entry6)  
#canvas.create_text(24,310+45+45+45+45+45,text="Genre:")

entry7=tk.Entry(root,width=80)

canvas.create_window(250,330+45+45+45+45+45+45,window=entry7)  
#canvas.create_text(46,310+45+45+45+45+45+45,text="Track Number:")

entry8=tk.Entry(root,width=80)

canvas.create_window(250,330+45+45+45+45+45+45+45,window=entry8)  
#canvas.create_text(38,310+45+45+45+45+45+45+45,text="Composer:")

def Save():
    
    if filename.endswith('.mp3'):
        if "TIT2" in s.keys():
            s2.setall("TIT2",[])


        if "TPE1" in s.keys():
            s2.setall("TPE1",[])

        if "TPE2" in s.keys():
            s2.setall("TPE2",[])

        if "TALB" in s.keys():
            s2.setall("TALB",[])

        if "TYER" in s.keys():
            s2.setall("TYER",[])

        if "TCON" in s.keys():
            s2.setall("TCON",[])

        if "TRCK" in s.keys():
            s2.setall("TRCK",[])

        if "TCOM" in s.keys():
            s2.setall("TCOM",[])
        s2.add(TIT2(encoding=0,text=[entry1.get()]))
        s2.add(TPE1(encoding=0,text=[entry2.get()]))
        s2.add(TPE2(encoding=0,text=[entry3.get()]))
        s2.add(TALB(encoding=0,text=[entry4.get()]))
        s2.add(TYER(encoding=0, text=[entry5.get()]))
        s2.add(TCON(encoding=0,text=[entry6.get()]))
        s2.add(TRCK(encoding=0,text=[entry7.get()]))
        s2.add(TCOM(encoding=0,text=[entry8.get()]))




        s2.save(v2_version=3)

    elif filename.endswith('.m4a'):
        s_m4a.tags['©nam']=[entry1.get()]
        s_m4a.tags['©ART']=[entry2.get()]
        s_m4a.tags['aART']=[entry3.get()]
        s_m4a.tags['©alb']=[entry4.get()]
        s_m4a.tags['©day']=[entry5.get()]
        s_m4a.tags['©gen']=[entry6.get()]
        tpl=entry7.get()
        s_m4a.tags['trkn']= [(int(list(tpl)[0]),int(list(tpl)[2]))]
       # s_m4a.tags['trkn']=[(2,12)]
        #s_m4a.tags['©nam']=['a m a r i']
        
        s_m4a.tags['©wrt']= [entry8.get()]
        s_m4a.tags['covr']=[image_bytes]
        s_m4a.save()
        
        
save_button=HoverButton(master=root,fg="white",bg="white",activebackground="#00acee",width=100,height=30, bd=0,command=Save)
canvas.create_window(250,680,window=save_button)
canvas.configure(background="black")

save_image=Image.open("save_button.png")
save_image_txt=ImageTk.PhotoImage(master=root,image=save_image)
canvas.create_image(250,680,image=save_image_txt)
save_button.configure(image=save_image_txt,compound=CENTER)
root.mainloop()    


# In[ ]:




