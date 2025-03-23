from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as sc
from tkinter import messagebox
from datetime import datetime
import   time , os , cv2
from playsound import playsound
from threading import Thread

root = Tk()
root.title('[Files Security]')
root.geometry('1350x642+0+0')
root.resizable(False,False)
root.configure(bg='gray')

#def
def data():
    Thread(target=secur).start()
def secur():
    press = Thread(target=security)
    press.start()
def security():
    file_path = entry_var.get()
    size      = os.path.getsize(file_path)
    scrol.insert(END,'[+]Files Protection\n','green')
    scrol.insert(END,'=====================================\n','green')
    while True:
        size_now = os.path.getsize(file_path)
        time      = datetime.now()
        date      = time.strftime('%d/%m/%Y')
        time      = time.strftime('%H:%M:%S')
        if size_now  != size:
            picture   = cv2.VideoCapture(0)
            vidi,vido = picture.read()
            cv2.imwrite('hacker.png',vido)
            del(picture)
            scrol.insert(END,'[+]There is a [====HACKER====] on the file\n','red')
            data =[
                (file_path,'Modified',date,time)
            ]
            for item in data:
                tv.insert('',END,values=item)
            playsound('audio.mp3')
            break
        else:
            time.sleep(1)
            scrol.insert(END,f'[+]The file is safe in: {date}/{time}\n','blue')
def system():
    messagebox.showinfo('Systeme','This program is system for protect and monitoring any files.How it works?Well you just need to type the correct path of the file you want to monitor and if anything changes in the file,the program will make noise,and you can see the details in the program.')
def me():
    messagebox.showinfo('Me','''
                        Abderrahim Sikou,
                        Python developer
                        ''')
#variables
entry_var = StringVar()
#images
img1 = PhotoImage(file='images/im1.png')
img2 = PhotoImage(file='images/im2.png')
img5 = PhotoImage(file='images/im5.png')
modifiy_img1 = img1.subsample(2,2)
modifiy_img2 = img2.subsample(2,2)
modifiy_img5 = img5.subsample(2,2)
#frame
fr1 = Frame(root, bd=1,relief=SOLID,bg='#134c5e')
fr1.place(x=1,y=1,width=1348,height=200)
#call images
l1 = Label(fr1, image=modifiy_img2)
l1.place(x=2,y=6,width=210,height=190)
l2 = Label(fr1, image=modifiy_img1)
l2.place(x=1112,y=2,width=225,height=170)
#titles
title1 = Label(fr1, text='[Cyber Security Tool]',bg='#134c5e',fg='yellow',font=('courier',25,'bold'))
title1.place(x=450,y=10)
title2 = Label(fr1, text='Python',bg='#134c5e',fg='yellow',font=('courier',30,'bold'))
title2.place(x=595,y=60)
#buttons
b1 = Button(fr1, text='About Systeme',bd=4,relief=GROOVE,font=('courier',16,'bold'),cursor='hand2',bg='green',fg='black',command=system)
b1.place(x=380,y=130,width=200)
b2 = Button(fr1, text='About Me',bd=4,relief=GROOVE,font=('courier',16,'bold'),cursor='hand2',bg='green',fg='black',command=me)
b2.place(x=590,y=130,width=200)
b3 = Button(fr1, text='Exit',bd=4,relief=GROOVE,font=('courier',16,'bold'),cursor='hand2',bg='green',fg='black',command=exit)
b3.place(x=800,y=130,width=200)
#frame 
fr2 = Frame(root, bd=2,relief=SUNKEN,bg='#134c5e')
fr2.place(x=1,y=202,width=270,height=437)
#image
l1 = Label(fr2, image=modifiy_img5)
l1.place(x=13,y=48,width=240,height=240)
#titles
title3 = Label(fr2, text='FILES Security',bg='#134c5e',fg='yellow',font=('Kristen ITC',22,'bold'))
title3.place(x=15,y=1)
#entry
title4 = Label(fr2, text='Enter the file path:',bg='#134c5e',fg='yellow',font=('courier',16,'bold'))
title4.place(x=1,y=300)
en = Entry(fr2, bd=4,relief=RAISED,justify=CENTER,textvariable=entry_var,font=('courier',15,'bold'),cursor='hand2')
en.place(x=2,y=340,width=262,height=45)
butt = Button(fr2, text='Start Monitoring',bd=3,relief=RIDGE,font=('courier',16,'bold'),cursor='hand2',bg='green',fg='black',command=data)
butt.place(x=2,y=390,width=262,height=45)
#scroll text
scrol = sc.ScrolledText(root)
scrol['font'] = ('calibri',16,'bold')
scrol.place(x=272,y=202,width=400,height=437)
scrol.tag_config('green',background='white',foreground='blue')
scrol.tag_config('blue',background='white',foreground='green')
scrol.tag_config('red',background='white',foreground='red')
#scroll for table
scrollt = sc.ScrolledText(root)
scrollt['font'] = ('courier',14,'bold')
scrollt.place(x=673,y=202,width=675,height=515)
#table
tab = ttk.Style()
tab.configure('mystyle.Treeview',font=('Calibri',13),rowheight=80)
tab.configure('mystyle.Treeview.Heading',font=('Calibri',13))
tv = ttk.Treeview(scrollt, columns=('File Path','State','Date','Time'),style='mystyle.Treeview')
tv.column('#0',width=0)
tv.column('File Path',width=307)
tv.column('State',width=100)
tv.column('Date',width=125)
tv.column('Time',width=120)
#heading
tv.heading('#0',text='')
tv.heading('File Path', text='File Path')
tv.heading('State', text='State')
tv.heading('Date', text='Date')
tv.heading('Time', text='Time')
tv['show'] = 'headings'
tv.place(x=0,y=0)

root.mainloop()