from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as sc
from scapy.all import *
from threading import Thread

root = Tk()
root.geometry('1350x668+0+0')
root.title('Network Sniffing')
root.resizable(False,False)
root.configure(background='black') 
 
# Def
def network():
    Thread(target=sniff_data).start()
    
def data(packet):
    if packet.haslayer(TCP):
        tcp    = 'TCP'
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        s_port = packet.sport
        d_port = packet.dport
        size = str(len(packet[TCP]))
        scrol_tcp.insert(END,'[+]','one')
        scrol_tcp.insert(END,'TCP Packet Send.....','two')
        scrol_tcp.insert(END,'\n[+]','one')
        scrol_tcp.insert(END,f'IP Sender:{src_ip}\n','three')
        scrol_tcp.insert(END,'[+]','one')
        scrol_tcp.insert(END,f'IP Receive:{dst_ip}\n','three')
        scrol_tcp.insert(END,'[+]','one')
        scrol_tcp.insert(END,f'Sender Port:{str(s_port)}\n','three')
        scrol_tcp.insert(END,'[+]','one')
        scrol_tcp.insert(END,f'Receive Port:{str(d_port)}\n','three')
        scrol_tcp.insert(END,'[+]','one')
        scrol_tcp.insert(END,f'Data Size:{size}\n','three')
        scrol_tcp.insert(END,'========================================\n','one')
        tcp_table = [
            (tcp,src_ip,dst_ip,s_port,d_port,size)
        ]
        for item in tcp_table:
            tv.insert('',END,values=item)
    if packet.haslayer(UDP):
        udp    = 'UDP'
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        s_port = packet.sport
        d_port = packet.dport
        size   = str(len(packet[UDP]))
        scrol_udp.insert(END,'[+]','one')
        scrol_udp.insert(END,'UDP Packet Send.....','two')
        scrol_udp.insert(END,'\n[+]','one')
        scrol_udp.insert(END,f'IP Sender:{src_ip}\n','three')
        scrol_udp.insert(END,'[+]','one')
        scrol_udp.insert(END,f'IP Receive:{dst_ip}\n','three')
        scrol_udp.insert(END,'[+]','one')
        scrol_udp.insert(END,f'Sender Port:{str(s_port)}\n','three')
        scrol_udp.insert(END,'[+]','one')
        scrol_udp.insert(END,f'Receive Port:{str(d_port)}\n','three')
        scrol_udp.insert(END,'[+]','one')
        scrol_udp.insert(END,f'Data Size:{size}\n','three')
        scrol_udp.insert(END,'========================================\n','one')
        udp_table = [
            (udp,src_ip,dst_ip,s_port,d_port,size)
        ]
        for item in udp_table:
            tv.insert('',END,values=item)
    
def sniff_data():
    sniff(iface='WiFi',prn=data)  
    
# Frame
principle_frame = Frame(root,bg='#073444',bd=1,relief=RIDGE)
principle_frame.place(x=1,y=2,width=253,height=578)
# Images
img1 = PhotoImage(file='images/mg1.png')
img2 = PhotoImage(file='images/mg2.png')
# Modif img
mg1 = img1.subsample(2,2)
mg2 = img2.subsample(2,2)
# Call img
call1 = Label(principle_frame,image=mg1)
call1.place(x=3,y=1,width=240,height=250)
call2 = Label(principle_frame,image=mg2)
call2.place(x=3,y=350,width=240,height=230)
# Titles
title = Label(principle_frame,text='Pyhton[Cyber Tool]\nTCP & UDP\nNetwork Scanning',bg='#073444',fg='yellow',font=('courier',17,'bold'))
title.place(x=0,y=260)
# Button
but1 = Button(root, text='Start Scanning',bd=5,relief=GROOVE,cursor='hand2',bg='#073444',fg='yellow',font=('courier',15,'bold'),command=network)
but1.place(x=1,y=582,width=253,height=42)
but2 = Button(root, text='Exit',bd=5,relief=GROOVE,cursor='hand2',bg='#073444',fg='yellow',font=('courier',15,'bold'),command=exit)
but2.place(x=1,y=626,width=253,height=41)
# Seconde frame
second_frame = Frame(root,bg='#D8D8D8',bd=2,relief='raised')
second_frame.place(x=255,y=2,width=545,height=50)
title1 = Label(second_frame,text='Protocol TCP',fg='black',bg='#D8D8D8',font=('courier',20,'bold'))
title1.place(x=170,y=5)
# Scroll text
scrol_tcp = sc.ScrolledText(root)
scrol_tcp['font'] = ('courier',16,'bold')
scrol_tcp.place(x=256,y=53,width=544,height=270)
scrol_tcp.tag_configure('one',background='white',foreground='green')
scrol_tcp.tag_configure('two',background='yellow',foreground='black')
scrol_tcp.tag_configure('three',background='white',foreground='blue')
# Third frame
third_frame = Frame(root,bg='#D8D8D8',bd=2,relief='raised')
third_frame.place(x=802,y=2,width=546,height=50)
title2 = Label(third_frame,text='Protocol UDP',fg='black',bg='#D8D8D8',font=('courier',20,'bold'))
title2.place(x=170,y=5)
# Scroll text
scrol_udp = sc.ScrolledText(root)
scrol_udp['font'] = ('courier',16,'bold')
scrol_udp.place(x=802,y=53,width=545,height=270)
scrol_udp.tag_configure('one',background='white',foreground='green')
scrol_udp.tag_configure('two',background='yellow',foreground='black')
scrol_udp.tag_configure('three',background='white',foreground='blue')
# Table
tv = ttk.Treeview(root)
tab = ttk.Style(root)
tab.theme_use('clam')
tab.configure('Treeview',font=('Courier',14,'bold'),rowheight=120,background='white',fieldbackground='white',foreground='black')
tab.configure('mystyle.Treeview.Heading',font=('Calibri',13,'bold'))
tv = ttk.Treeview(root,columns=('Protocol','IP Sender','IP Reseive','Sender Port','Reseive Port','Data Size'),style='mystyle.Treeview')
tv.column('#0',width=0,anchor=CENTER)
tv.column('Protocol',width=181,anchor=CENTER)
tv.column('IP Sender',width=181,anchor=CENTER)
tv.column('IP Reseive',width=181,anchor=CENTER)
tv.column('Sender Port',width=181,anchor=CENTER)
tv.column('Reseive Port',width=181,anchor=CENTER)
tv.column('Data Size',width=181,anchor=CENTER)
#heading
tv.heading('#0',text='')
tv.heading('Protocol', text='Protocol')
tv.heading('IP Sender', text='IP Sender')
tv.heading('IP Reseive', text='IP Reseive')
tv.heading('Sender Port', text='Sender Port')
tv.heading('Reseive Port', text='Reseive Port')
tv.heading('Data Size', text='Data Size')
tv['show'] = 'headings'
tv.place(x=257,y=326)

root.mainloop()         