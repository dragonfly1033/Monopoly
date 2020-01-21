from MonopolyFunctions import *
from MonopolyConstants import *
from tkinter import *
from tkinter import ttk
import MonopolyFunctions
import MonopolyConstants
import random
import time
def main(pn, adminmode):
    def adminConsole():
        t = Toplevel()
        t.geometry('175x95')
        l = Label(t, text='Admin Panel')
        l.grid(columnspan=2, row=0)
        mv = Label(t, text='Move: ')
        mv.grid(column=0, row=1)
        mv_pl = Entry(t)
        mv_pl.grid(column=1, row=1)
        pay = Label(t, text='Pay: ')
        pay.grid(column=0, row=2)
        pay_pl = Entry(t)
        pay_pl.grid(column=1, row=2)
        mv_pl.bind('<Return>',lambda x: move_player(MonopolyConstants.cur_player,int(mv_pl.get()),app,False))
        pay_pl.bind('<Return>',lambda x: transaction(pay_pl.get()[:2],int(pay_pl.get()[3:])))
        bb = ttk.Button(t, text='Change', command=lambda: change_turn())
        bb.grid(columnspan=2, row=3)
        t.mainloop()

    for i in range(1,pn+1):
        cur_pos['p'+str(i)] = 'Go'
        p_bals['p'+str(i)] = 1500
        p_worths['p'+str(i)] = 1500
        p_debts['p'+str(i)] = {'p1':0,'p2':0,'p3':0,'p4':0,'p5':0,'p6':0}
        po_props['p'+str(i)] = []
    MonopolyConstants.change_ps(pn)
    for i in info:
        names.append(i)
    class Property(Tk):
        def __init__(self, name, colour, x, y, main, dim1, dim2, cSide, cdim1, cdim2):
           if(name[:6]=='Chance'):
            nameD = name[:6]
           elif(name[:11]=='Comm. Chest'):
            nameD = name[:11]
           else:
            nameD=name
           f = Frame(main, bg='honeydew3', height=dim1, width=dim2, highlightbackground="black", highlightthickness=1, bd=0)
           f.pack_propagate(0)
           f.grid(column=x, row=y)
           if(colour=='honeydew3'):
               info[name]['c'] = Frame(f, bg=colour, height=cdim1, width=cdim2)
               info[name]['c'].pack(side=cSide)
           else:
               info[name]['c'] = Frame(f, bg=colour, height=cdim1, width=cdim2, highlightbackground="black", highlightthickness=1, bd=0)
               info[name]['c'].pack(side=cSide)
           if(cSide=='top' or cSide=='bottom'):
            pgdim1 = dim1-20
            pgdim2 = dim2
           else:
            pgdim1 = dim1
            pgdim2 = dim2-20
           info[name]['pg'] = Frame(f, bg='honeydew3', width=pgdim2, height=pgdim1)
           info[name]['pg'].pack(side=cSide)
           namel = Label(info[name]['pg'], text=nameD, bg='honeydew3', wraplength= pgdim2)
           namel.place(rely=0.5, relx=0.5, anchor=CENTER)
           hs[name] = 0
           hdim1=0
           hdim2=0
           hScide=''
           if(cdim1 == 56):
            hdim1 = 14
            hdim2=cdim2
           elif(cdim2 == 56):
            hdim2 = 14
            hdim1=cdim1
           if(cSide == 'top' or cSide == 'bottom'):
            hSide = 'left'
           else:
            hSide = 'top'
           info[name]['c'].pack_propagate(0)
           info[name]['f1'] = Frame(info[name]['c'], bg=colour, width=hdim2, height=hdim1)
           info[name]['f1'].pack(side=hSide)
           info[name]['f2'] = Frame(info[name]['c'], bg=colour, width=hdim2, height=hdim1)
           info[name]['f2'].pack(side=hSide)
           info[name]['f3'] = Frame(info[name]['c'], bg=colour, width=hdim2, height=hdim1)
           info[name]['f3'].pack(side=hSide)
           info[name]['f4'] = Frame(info[name]['c'], bg=colour, width=hdim2, height=hdim1)
           info[name]['f4'].pack(side=hSide)
           info[name]['h1'] = Frame(info[name]['f1'], bg='dark green', width=(hdim2/2), height=(hdim1/2))
           info[name]['h1'].place(relx=0.5, rely=0.5, anchor=CENTER)
           info[name]['h2'] = Frame(info[name]['f2'], bg='dark green', width=(hdim2/2), height=(hdim1/2))
           info[name]['h2'].place(relx=0.5, rely=0.5, anchor=CENTER)
           info[name]['h3'] = Frame(info[name]['f3'], bg='dark green', width=(hdim2/2), height=(hdim1/2))
           info[name]['h3'].place(relx=0.5, rely=0.5, anchor=CENTER)
           info[name]['h4'] = Frame(info[name]['f4'], bg='dark green', width=(hdim2/2), height=(hdim1/2))
           info[name]['h4'].place(relx=0.5, rely=0.5, anchor=CENTER)
           ori = globals()['pp'+cSide[0]]
           info[name]['p1'] = Frame(info[name]['pg'],bg=pc[0], width=ori[0][2]-ori[0][0], height=ori[0][3]-ori[0][1])
           info[name]['p1'].place(x=ori[0][0], y=ori[0][1])
           info[name]['p2'] = Frame(info[name]['pg'],bg=pc[1], width=ori[1][2]-ori[1][0], height=ori[1][3]-ori[1][1])
           info[name]['p2'].place(x=ori[1][0], y=ori[1][1])
           info[name]['p3'] = Frame(info[name]['pg'],bg=pc[2], width=ori[2][2]-ori[2][0], height=ori[2][3]-ori[2][1])
           info[name]['p3'].place(x=ori[2][0], y=ori[2][1])
           info[name]['p4'] = Frame(info[name]['pg'],bg=pc[3], width=ori[3][2]-ori[3][0], height=ori[3][3]-ori[3][1])
           info[name]['p4'].place(x=ori[3][0], y=ori[3][1])
           info[name]['p5'] = Frame(info[name]['pg'],bg=pc[4], width=ori[4][2]-ori[4][0], height=ori[4][3]-ori[4][1])
           info[name]['p5'].place(x=ori[4][0], y=ori[4][1])
           info[name]['p6'] = Frame(info[name]['pg'],bg=pc[5], width=ori[5][2]-ori[5][0], height=ori[5][3]-ori[5][1])
           info[name]['p6'].place(x=ori[5][0], y=ori[5][1])
           all_house(name)
           if(name == 'Just Vsitng'):
            info[name]['c'].destroy()
            info[name]['pg'].configure(width=86, height=86, bg='orange')
            namel.configure(text='J\nu\ns\nt', anchor='w', font=6, bg='orange')
            k = namel.place_info()
            k['relx'] = '0.05'
            k['rely'] = '0'
            k['anchor'] = 'nw'
            namel.place_forget()
            namel.place(k)
            namel2 = Label(info[name]['pg'], text='Visiting', font=6, bg='orange')
            namel2.place(relx=0.2, y=60)
            info[name]['In_jail'] = Frame(f, width=60, height=56, bg='honeydew3', highlightbackground="black", highlightthickness=1, bd=0)
            info[name]['In_jail'].place(x=25, y=0)
            jaill = Label(info[name]['In_jail'], text='Jail', bg='honeydew3')
            jaill.place(relx=0.5, rely=0.5, anchor=CENTER)
            q = info[name]['p2'].place_info()
            q['x'] = str(int(q['x']) - 20)
            q['y'] = str(int(q['y']) + 56)
            info[name]['p2'].place(q)
            q = info[name]['p5'].place_info()
            q['y'] = str(int(q['y']) + 28)
            info[name]['p5'].place(q)
            q = info[name]['p6'].place_info()
            q['y'] = str(int(q['y']) + 28)
            info[name]['p6'].place(q)
            q = info[name]['p3'].place_info()
            q['x'] = str(int(q['x']) + 20)
            q['y'] = str(int(q['y']) + 56)
            info[name]['p3'].place(q)
            info[name]['p1_jail'] = Frame(info[name]['In_jail'], width=10, height=14, bg=pc[0])
            info[name]['p1_jail'].place(x=5,y=7)
            info[name]['p2_jail'] = Frame(info[name]['In_jail'], width=10, height=14, bg=pc[1])
            info[name]['p2_jail'].place(x=25,y=7)
            info[name]['p3_jail'] = Frame(info[name]['In_jail'], width=10, height=14, bg=pc[2])
            info[name]['p3_jail'].place(x=45,y=7)
            info[name]['p4_jail'] = Frame(info[name]['In_jail'], width=10, height=14, bg=pc[3])
            info[name]['p4_jail'].place(x=5,y=35)
            info[name]['p5_jail'] = Frame(info[name]['In_jail'], width=10, height=14, bg=pc[4])
            info[name]['p5_jail'].place(x=25,y=35)
            info[name]['p6_jail'] = Frame(info[name]['In_jail'], width=10, height=14, bg=pc[5])
            info[name]['p6_jail'].place(x=45,y=35)
            hide_player(name,'p1_jail','p2_jail','p3_jail','p4_jail','p5_jail','p6_jail')
           hide_all_players(name)
    class Window(Tk):
        def __init__(self):
           Tk.__init__(self)
           self.title('Monopoly')
           def temp():
               a = Toplevel()
               l = Listbox(a)
               l.pack()
               l.insert(END,'Player 1 : red')
               l.insert(END,'Player 2 : green')
               l.insert(END,'Player 3 : blue')
               l.insert(END,'Player 4 : orange')
               l.insert(END,'Player 5 : purple')
               l.insert(END,'Player 6 : yellow')
           menu = Menu(self)
           menu.add_command(label='Help', command=lambda:hide_enlarge())
           self.configure(menu=menu)
           menu.add_command(label='Player Key', command=lambda:temp())
           self.configure(menu=menu)
           main = Frame(self, bg='DarkSeaGreen1')
           main.grid(row=0, column=0)
           T = Label(main, text='MONOPOLY', bg='firebrick1', font=('helvetica',52,'bold'), fg='white')
           T.place(x=338, y=338, anchor=CENTER)
           info['pay_50_button'] = ttk.Button(main, text='Pay £50', command=lambda: pay_50())
           info['pay_50_button'].place(x=338, y=500, anchor=CENTER)
           hide(info['pay_50_button'])
           info['turn_label'] = Label(main, text="Player 1's turn", bg='DarkSeaGreen1', font=('helvetica',12,'bold'))
           info['turn_label'].place(relx=0.5, rely=0.3, anchor=CENTER)
           w=54
           n1 = (1*w)/9
           n2 = (2*w)/9
           n3 = (4*w)/9
           n4 = (5*w)/9
           n5 = (7*w)/9
           n6 = (8*w)/9
           dice1 = Canvas(main, height=w, width=w, bg='light grey', highlightthickness=1, highlightbackground='black', bd=0)
           dice1.place(y=108, x=240)
           s1 = dice1.create_oval(n1,n1,n2,n2, fill='black')
           s2 = dice1.create_oval(n3,n1,n4,n2, fill='black')
           s3 = dice1.create_oval(n5,n1,n6,n2, fill='black')
           s4 = dice1.create_oval(n1,n3,n2,n4, fill='black')
           s5 = dice1.create_oval(n3,n3,n4,n4, fill='black')
           s6 = dice1.create_oval(n5,n3,n6,n4, fill='black')
           s7 = dice1.create_oval(n1,n5,n2,n6, fill='black')
           s8 = dice1.create_oval(n3,n5,n4,n6, fill='black')
           s9 = dice1.create_oval(n5,n5,n6,n6, fill='black')
           dice2 = Canvas(main, height=w, width=w, bg='light grey', highlightthickness=1, highlightbackground='black', bd=0)
           dice2.place(y=108, x=380)
           s1 = dice2.create_oval(n1,n1,n2,n2, fill='black')
           s2 = dice2.create_oval(n3,n1,n4,n2, fill='black')
           s3 = dice2.create_oval(n5,n1,n6,n2, fill='black')
           s4 = dice2.create_oval(n1,n3,n2,n4, fill='black')
           s5 = dice2.create_oval(n3,n3,n4,n4, fill='black')
           s6 = dice2.create_oval(n5,n3,n6,n4, fill='black')
           s7 = dice2.create_oval(n1,n5,n2,n6, fill='black')
           s8 = dice2.create_oval(n3,n5,n4,n6, fill='black')
           s9 = dice2.create_oval(n5,n5,n6,n6, fill='black')
           f1d=[s5]
           f2d=[s1,s9]
           f3d=[s3,s5,s7]
           f4d=[s1,s3,s7,s9]
           f5d=[s1,s3,s5,s7,s9]
           f6d=[s1,s3,s4,s6,s7,s9]
           dnum(dice1, 6, f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9)
           dnum(dice2, 6, f1d, f2d, f3d, f4d, f5d, f6d, s1, s2, s3, s4, s5, s6, s7, s8, s9)
           roll_button= ttk.Button(main,text='Roll',command=lambda:roll(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, dice1, dice2, f1d, f2d, f3d, f4d, f5d, f6d, roll_label, MonopolyConstants.cur_player, T))
           roll_button.place(y=110,x=300)
           roll_label = Label(main, text='', bg='DarkSeaGreen1')
           roll_label.place(y=140, x=330)
           end_turn_button= ttk.Button(main,text='End Turn',command=lambda: MonopolyFunctions.change_turn())
           end_turn_button.place(y=170,x=300)
           buy_button= ttk.Button(main,text='Buy',command=lambda: Buy(cur_pos[MonopolyConstants.cur_player]))
           buy_button.place(y=125,x=87)
           sell_button= ttk.Button(main,text='Sell',command=lambda: temp())
           sell_button.place(y=125,x=163)
           build_button= ttk.Button(main,text='Build',command=lambda: build())
           build_button.place(y=125,x=436)
           trade_button = ttk.Button(main,text='Trade',command=lambda: temp())
           trade_button.place(y=125,x=512)
           for i in list(info.keys())[:40]:
               if(info[i]['position'][0]==10 and info[i]['position'][1] != 0 and info[i]['position'][1] != 10):
                   dim1 = 56
                   dim2 = 86
               elif(info[i]['position'][0]==0 and info[i]['position'][1] != 0 and info[i]['position'][1] != 10):
                   dim1 = 56
                   dim2 = 86
               elif(info[i]['position'][1]==10 and info[i]['position'][0] != 0 and info[i]['position'][0] != 10):
                   dim1 = 86
                   dim2 = 56
               elif(info[i]['position'][1]==0 and info[i]['position'][0] != 0 and info[i]['position'][0] != 10):
                   dim1 = 86
                   dim2 = 56
               else:
                   dim1 = 86
                   dim2 = 86
               if(info[i]['position'][0] == 0):
                   cSide = 'right'
               elif(info[i]['position'][0] == 10):
                   cSide = 'left'
               elif(info[i]['position'][1] == 0):
                   cSide = 'bottom'
               elif(info[i]['position'][1] == 10):
                   cSide = 'top'
               if(cSide == 'right' or cSide == 'left'):
                   cdim1 = dim1
                   cdim2 = 20
               else:
                   cdim1 = 20
                   cdim2 = dim2
               p = Property(i,info[i]['colour'],info[i]['position'][0],info[i]['position'][1], main, dim1, dim2, cSide, cdim1, cdim2)
           for i in cur_pos:
            show_player(cur_pos[i],i)
           side = Frame(self, bg='DarkSeaGreen1', height=676, width=655)
           side.grid(row=0, column=1)
           side.grid_propagate(0)
           info['p1_prop_box'] = Listbox(side, bg='grey', relief='flat', width=36, highlightthickness=1, highlightbackground='black', bd=0)
           info['p1_prop_box'].grid(column=0, row=0)
           info['p2_prop_box'] = Listbox(side, bg='grey', relief='flat', width=36, highlightthickness=1, highlightbackground='black', bd=0)
           info['p2_prop_box'].grid(column=1, row=0)
           info['p3_prop_box'] = Listbox(side, bg='grey', relief='flat', width=36, highlightthickness=1, highlightbackground='black', bd=0)
           info['p3_prop_box'].grid(column=2, row=0)
           info['p4_prop_box'] = Listbox(side, bg='grey', relief='flat', width=36, highlightthickness=1, highlightbackground='black', bd=0)
           info['p4_prop_box'].grid(column=0, row=1)
           info['p5_prop_box'] = Listbox(side, bg='grey', relief='flat', width=36, highlightthickness=1, highlightbackground='black', bd=0)
           info['p5_prop_box'].grid(column=1, row=1)
           info['p6_prop_box'] = Listbox(side, bg='grey', relief='flat', width=36, highlightthickness=1, highlightbackground='black', bd=0)
           info['p6_prop_box'].grid(column=2, row=1)
           for i in ps:
            info[i+'_prop_box'].configure(bg='DarkSeaGreen1')
            info[i+'_prop_box'].insert(END, 'Player '+i[1]+' Balance: £{}'.format(p_bals[i]))
            info[i+'_prop_box'].insert(END, 'Player '+i[1]+' Worth: £{}'.format(p_worths[i]))
            info[i+'_prop_box'].insert(END, 'Player '+i[1]+' Debt: £{}'.format(sum(p_debts[i].values())))
            info[i+'_prop_box'].insert(END, 'Owned Properties')
           info['prop_enlarge'] = Frame(side, width=218, height=352, bg='honeydew3', highlightthickness=1, highlightbackground='black', bd=0)
           info['prop_enlarge'].grid(column=0, row=2)
           info['prop_enlarge'].pack_propagate(0)
           info['prop_enlarge_c'] = Frame(info['prop_enlarge'], width=218, height=60, bg=info[cur_pos[MonopolyConstants.cur_player]]['colour'], highlightthickness=1, highlightbackground='black', bd=0)
           info['prop_enlarge_c'].pack(side='top')
           info['prop_enlarge_name'] = Label(info['prop_enlarge'], text=cur_pos[MonopolyConstants.cur_player], bg='honeydew3', font=('helvetica',16, 'underline'), anchor='w', width=218)
           info['prop_enlarge_name'].pack(side='top')
           info['prop_enlarge_gap'] = Label(info['prop_enlarge'], text='', bg='honeydew3', font=('helvetica',12, 'underline'), anchor='w', width=218)
           info['prop_enlarge_gap'].pack(side='top')
           info['prop_enlarge_cost'] = Label(info['prop_enlarge'], text='Cost: £'+info[cur_pos[MonopolyConstants.cur_player]]['cost'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_cost'].pack(side='top')
           info['prop_enlarge_rent'] = Label(info['prop_enlarge'], text='Rent: £'+info[cur_pos[MonopolyConstants.cur_player]]['rent'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_rent'].pack(side='top')
           info['prop_enlarge_rent1'] = Label(info['prop_enlarge'], text='1 House: £'+info[cur_pos[MonopolyConstants.cur_player]]['rent1'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_rent1'].pack(side='top')
           info['prop_enlarge_rent2'] = Label(info['prop_enlarge'], text='2 Houses: £'+info[cur_pos[MonopolyConstants.cur_player]]['rent2'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_rent2'].pack(side='top')
           info['prop_enlarge_rent3'] = Label(info['prop_enlarge'], text='3 Houses: £'+info[cur_pos[MonopolyConstants.cur_player]]['rent3'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_rent3'].pack(side='top')
           info['prop_enlarge_rent4'] = Label(info['prop_enlarge'], text='4 Houses: £'+info[cur_pos[MonopolyConstants.cur_player]]['rent4'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_rent4'].pack(side='top')
           info['prop_enlarge_rent5'] = Label(info['prop_enlarge'], text='Hotel: £'+info[cur_pos[MonopolyConstants.cur_player]]['rent5'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_rent5'].pack(side='top')
           info['prop_enlarge_gap2'] = Label(info['prop_enlarge'], text='', bg='honeydew3', font=('helvetica',12, 'underline'), anchor='w', width=218)
           info['prop_enlarge_gap2'].pack(side='top')
           info['prop_enlarge_hcost'] = Label(info['prop_enlarge'], text='House/Hotel Cost: £'+info[cur_pos[MonopolyConstants.cur_player]]['HCost'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_hcost'].pack(side='top')
           info['prop_enlarge_mortgage'] = Label(info['prop_enlarge'], text='Mortgage: £'+info[cur_pos[MonopolyConstants.cur_player]]['mortgage'], bg='honeydew3', font=('helvetica',12), anchor='w', width=218)
           info['prop_enlarge_mortgage'].pack(side='top')
           hide_enlarge()
           info['status'] = Label(side, text='', bg='DarkSeaGreen1', font=('helvetica',24))
           info['status'].place(relx=0.66, rely=0.6, anchor=CENTER)
           clear_button= ttk.Button(side,text='Clear Message',command=lambda: info['status'].configure(text=''))
           clear_button.place(rely=0.9,relx=0.66, anchor=CENTER)
    app=Window()
    if(adminmode):
        adminConsole()
    app.mainloop()
def pre():
    auth = False
    def nextt(pn, ad):
        def admin():
            def checkadmin(val):
                if(val == 'sqrt(-1)2^3sumpi'):
                    a.destroy()
                    root.destroy()
                    main(pn, True)
            a = Toplevel(f)
            ee= Entry(a)
            ee.pack()
            ee.bind('<Return>',lambda x: checkadmin(ee.get()))
            a.mainloop()
        if(auth):
            if(ad==1):
                admin()
            else:
                root.destroy()
                main(pn, False)
        else:
            root.destroy()
            main(pn, True)
    root = Tk()
    root.geometry('1331x676')
    f = Frame(root, bg='DarkSeaGreen1')
    f.pack(fill='both', expand=True, side='top')
    l = Label(f, text='How Many Players?', bg='DarkSeaGreen1')
    l.place(relx=0.5, rely=0.45, anchor=CENTER)
    V1=IntVar()
    V1.set(0)
    cb = Checkbutton(f, variable=V1, onvalue=1, offvalue=0, text='Admin Ver.', bg='DarkSeaGreen1')
    cb.place(relx=0.1, rely=0.1, anchor=CENTER)
    e = Entry(f)
    e.place(relx=0.5, rely=0.50, anchor=CENTER)
    e.bind('<Return>',lambda x:nextt(int(e.get()), V1.get()))
    root.mainloop()
pre()

