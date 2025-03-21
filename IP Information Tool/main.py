import requests
from tkinter import *
from tkinter import ttk
from tkintermapview import TkinterMapView
from threading import Thread
from tkinter import messagebox

root = Tk()
root.title('IP[Information]')
root.geometry('1190x670+50+0')
root.resizable(False,False)
root.configure(background='silver')

# Def
def info():
    Thread(target=data).start()
def data():
    ip        = entr.get()
    api_token = '500c60cfcd4bdc'
    url       = f'https://ipinfo.io/{ip}?token={api_token}'
    responce = requests.get(url)
    if responce.status_code == 200:
        info     = responce.json()
        ipp      = info.get('ip')
        count    = info.get('country')
        cit      = info.get('city')
        reg      = info.get('region')
        zon      = info.get('timezone')
        posta    = info.get('postal')
        internet = info.get('org')
        line     = info.get('loc')
        menu     = [
            (ipp,count,cit,reg,zon,posta,internet,line)
        ]
        for second in menu:
            tv.insert('',END,values=second)
        map.set_tile_server('https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga',max_zoom=24)
        map.set_address(count,marker=True)
    else:
        messagebox.showerror('Error','Fail to get IP information')
entr = StringVar()

# Title
t1 = Label(root, text='IP DATA [Extract IP information]',bg='black',fg='white',font=('courier',18,'bold'))
t1.pack(fill=X)

# Frame for img
fr = Frame(root, bg='#091728')
fr.place(x=1,y=34,width=380,height=280)

# Images
mg1      = PhotoImage(file='images/m1.png')
modif1   = mg1.subsample(3,3)
mg2      = PhotoImage(file='images/m2.png')
modif2   = mg2.subsample(3,3)
call_mg1 = Label(fr, image=modif1)
call_mg1.place(x=210,y=65,width=160,height=160)
call_mg2 = Label(fr, image=modif2)
call_mg2.place(x=5,y=70,width=160,height=152)

# Title
tit1 = Label(fr, text='Python',bg='#091728',fg='yellow',font=('courier',28,'bold'))
tit1.place(x=30,y=1)
tit2 = Label(fr, text='[Cyber Tools]',bg='#091728',fg='yellow',font=('courier',19,'bold'))
tit2.place(x=170,y=9)
tit3 = Label(fr, text='IP Info,Location',bg='#091728',fg='white',font=('courier',19,'bold'))
tit3.place(x=60,y=240)

# Entry 
en = Entry(root, bd=3,relief=RIDGE,font=('courier',14,'bold'),justify=CENTER,textvariable=entr)
en.place(x=2,y=318,width=380,height=37)

# Button
but1 = Button(root, text='Extract IP Data/Location',bd=4,relief=GROOVE,bg='gray',fg='black',font=('courier',14,'bold'),cursor='hand2',command=info)
but1.place(x=1,y=358,width=382,height=40)

# Table
tv = ttk.Treeview(root)
tab = ttk.Style(root)
tab.theme_use('clam')
tab.configure('Treeview',font=('Courier',14,'bold'),rowheight=80,background='#D8D8D8',fieldbackground='#D8D8D8',foreground='black')
tab.configure('mystyle.Treeview.Heading',font=('Calibri',12,'bold'))
tv = ttk.Treeview(root,columns=('IP','Country','City','Region','TimeZone','Postal','ISP','Loc'),style='mystyle.Treeview')
tv.column('#0',width=0,anchor=CENTER)
tv.column('IP',width=150,anchor=CENTER)
tv.column('Country',width=80,anchor=CENTER)
tv.column('City',width=165,anchor=CENTER)
tv.column('Region',width=175,anchor=CENTER)
tv.column('TimeZone',width=175,anchor=CENTER)
tv.column('Postal',width=80,anchor=CENTER)
tv.column('ISP',width=185,anchor=CENTER)
tv.column('Loc',width=175,anchor=CENTER)
# Heading
tv.heading('#0',text='',anchor=CENTER)
tv.heading('IP', text='IP',anchor=CENTER)
tv.heading('Country', text='Country',anchor=CENTER)
tv.heading('City', text='City',anchor=CENTER)
tv.heading('Region', text='Region',anchor=CENTER)
tv.heading('TimeZone', text='TimeZone',anchor=CENTER)
tv.heading('Postal', text='Postal',anchor=CENTER)
tv.heading('ISP', text='ISP',anchor=CENTER)
tv.heading('Loc', text='Loc',anchor=CENTER)
tv['show'] = 'headings'
tv.place(x=1,y=398)

# Map
map = TkinterMapView(root,width=803,height=360,corner_radius=0,max_zoom=24)
map.place(x=384,y=35)

root.mainloop()