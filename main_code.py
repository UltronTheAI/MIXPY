from tkinter import *
from tkinter import filedialog
# from pynput.keyboard import *

root = Tk()
root.title('mixformpy')
root.geometry('900x500+600+300')
root.overrideredirect(1)
root.wm_attributes('-transparentcolor', 'pink')
root.attributes('-alpha', 0.40)
root.configure(bg='white')

frame = Frame(root)
frame.place(x=500, y=400)

a = 'i'
# print(a)


def help_button_click():
    global a
    lh['bg'] = 'blue'
    lh['fg'] = 'white'
    # print(a)
    if a == 'a':
        a = 'i'
        lhi.grid(row=91, column=0)
        lh1.grid(row=92, column=0)
        # lh['bg'] = 'blue'
        # lh['fg'] = ''
    if a == 'i':
        a = 'a'
        lhi.place(y=100000)
        lh1.place(y=100000)
        lh['bg'] = 'black'
        lh['fg'] = 'red'
    # lh['bg'] = 'pink'


def er(e):
    global a
    # print(a)
    lhi['text'] = 'help'
    lh1['text'] = 'exit'
    if a == 'a':
        a = 'i'
        lhi.grid(row=91, column=0)
        lh1.grid(row=92, column=0)
        # a = 'a'
    # if a == 'i':
    #     a = 'a'
    #     lhi.place(y = 100000)
    #     lh1.place(y = 100000)
    # lh['bg'] = 'blue'
    # lh['fg'] = 'white'


def lr(e):
    global a
    # print(a)
    # if a == 'a':
    #     a = 'i'
    #     lhi.grid(row = 9, column = 0)
    #     lh1.grid(row = 10, column = 0)
    #     # a = 'a'
    if a == 'i':
        a = 'a'
        lhi.place(y=100000)
        lh1.place(y=100000)
        # a = 'i'
        lh['bg'] = 'black'
        # lh['bg'] = 'blue'
        lh['fg'] = 'red'


def ho(e):
    lhi.grid(row=91, column=0)
    lh1.grid(row=92, column=0)
    # lh['bg'] = 'blue'
    # lh['fg'] = 'white'
    a = 'i'


def go(e):
    a = 'a'
    lhi.place(y=100000)
    lh1.place(y=100000)
    lh['bg'] = 'black'
    # lh['bg'] = 'blue'
    lh['fg'] = 'red'


def e():
    root.quit()


cv = 'f'


def m(e=None):
    global cv
    if cv == 'f':
        root.overrideredirect(10)
        # root.attributes('-fullscreen', True)
        cv = 'a'
    if cv == 'a':
        cv = 'f'
        # root.attributes('-fullscreen', False)
        root.overrideredirect(1)


def me(e):
    global cv
    # if cv == 'f':
    root.overrideredirect(0)
    root.resizable(0, 0)
    # root.attributes('-fullscreen', True)
    # cv = 'a'


def ml(e):
    global cv
    # if cv == 'f':
    root.overrideredirect(1)
    # root.attributes('-fullscreen', True)
    # cv = 'a'


jj = ''


def lp_c():
    global jj
    if jj == 'a':
        jj = 'b'
        # print('lp')
        lp1['text'] = 'new project'
        lp2['text'] = 'open project'
        lp1.place(x=0, y=0)
        lp2.place(x=0, y=0)
        ioo.grid(row=2, column=0)
        ioo1.grid(row=3, column=0)
    if jj == 'b':
        jj = 'a'
        lp1.place(x=0, y=9000)
        lp2.place(x=0, y=9000)
        ioo.place(y=2, x=1000)
        ioo1.place(y=3, x=0)


def lp_e(e):
    # print('lp')
    lp1['text'] = 'new project'
    lp2['text'] = 'open project'
    lp1.place(x=30, y=20)
    lp2.place(x=30, y=40)
    ioo.grid(row=2, column=0)
    ioo1.grid(row=3, column=0)


def lp_l(e):
    lp1.place(x=0, y=9000)
    lp2.place(x=0, y=9000)
    ioo.place(y=2, x=1000)
    ioo1.place(y=3, x=0)


r = ''
bgx = 180


def lp_new_project():
    global r
    lib__.place(x = 800, y = 30)
    r = filedialog.asksaveasfile(title='make new a file', mode='a',
                                 filetypes=(('.py files', '*.py files'), ('.not_py files', '*.py files')))

iu = 1
def lp_open_project():
    global r, bgx, iu
    lib__.place(x = 800, y = 30)
    lib__1.place(x = 800, y = 60)
    lib__2.place(x = 800, y = 90)
    lib__3.place(x = 800, y = 120)
    lib__4.place(x = 800, y = 150)
    r = filedialog.askopenfilename(title='open a file',
                                   filetypes=(('.py files', '*.py files'), ('.not_py files', '*.py files')))
    if iu == 1:
     bg.place(x=bgx, y=0)
     bg['text'] = r
     bgxd = bgx + 30
     t.delete(0.1, END)
     iss = open(file=r)
     iss1 = iss.read()
     t.insert(INSERT, iss1)
     t.place(x=210, y=20)
     te.place(x = 340, y = 0)
     # t.delete(0.1, END)
     iu = iu + 1


def bg_c():
    t.delete(0.1, END)
    iss = open(file=r)
    iss1 = iss.read()
    t.insert(INSERT, iss1)
    t.place(x=210, y=20)
    # lib__.place(x = 9000, y =7000)


def run():
    global r
    # import subprocess
    # subprocess.run(['python', r])
    rt = open(r, 'w')
    rt.write(t.get(0.1, END))
    rt.close()
    import subprocess
    subprocess.run(['python', r])

def ooo():
    global iu
    # t['padx'] = 0
    # t['pady'] = 0
    # te.place()
    te.place(x = 900, y =900)
    t.place(x = 900, y =900)
    bg.place(x = 900, y = 900)
    lib__.place(x = 9000, y =7000)
    lib__1.place(x = 9000, y =7000)
    lib__2.place(x = 9000, y =7000)
    lib__3.place(x = 9000, y =7000)
    lib__4.place(x = 9000, y =7000)
    iu = iu - 1

def lib(e):
    tr = t.get(0.0, END)
    # t.bind('p', prw)
    if 'p' in tr:
        lib__.place(x = 210, y = 100)


def lib_l(e):
    lib__.place(y = 10000, x =9000)

oooo = PhotoImage(file='b.png')
root.iconbitmap('Icon.png')
lopsss = Label(image=oooo).place(x=100, y=0)
l = Label(bg='black', width=30, pady=500)
l.place(x=0, y=0)
t = Text(fg='#00FFFF', font = ('Styles', 20), bg=('black'), padx=100, pady=200)
t.place(x=900, y=900)
lp = Button(bg='black', fg='red', text='PROJECT', width=15, pady=1, border=0, command=lp_c)
lp.grid(row=1, column=0)
ioo = Label(bg='black', width=0)
ioo1 = Label(bg='black', width=0)
te = Button(bg = 'black', border = 0, fg = 'red', text = 'x',command = ooo, padx = 100)
te.place(x = 900, y = 900)
ls = Label(bg='black', width=9)
bg = Button(border=0, bg='black', fg='gray', text=r, padx=30, command=bg_c,width = 15)
ls.grid(row=200, column=1)
def opp(e = ''):
    import webbrowser
    webbrowser.open('cmd')

lpm = Button(bg='black', fg='red', text='pip python', width=15, pady=1, border=0, command = opp)
lpm.grid(row=20, column=0)
ldp = Button(bg='black', fg='red', text='download python', width=15, pady=1, border=0)
ldp.grid(row=30, column=0)
lh = Button(bg='black', fg='red', text='help by mixformpy', width=15, pady=1, border=0, command=help_button_click)
lh.grid(row=40, column=0)
def opp12(e = ''):
    opp()
lhi = Button(bg='black', fg='white', text='', width=15, pady=1, border=0, command = opp12)
lhi.grid(row=90, column=0)
lh1 = Button(bg='black', fg='white', text='', width=15, pady=1, border=0, command=e)
lp1 = Button(bg='black', fg='white', text='', width=15, pady=1, border=0, command=lp_new_project)
lp2 = Button(bg='black', fg='white', text='', width=15, pady=1, border=0, command=lp_open_project)
lp1.place(x=9000, y=900)
lp2.place(x=9000, y=900)
lh1.place(y=100000, x=0)
def prw():
    t.insert(INSERT, '\nprint("")\n')
def inp():
    t.insert(INSERT, '\ninput("")\n')
def intv():
    t.insert(INSERT, 'int()')
def strv():
    t.insert(INSERT, 'str()')
    global r
    tryr = float(r)
def floatv():
    t.insert(INSERT, 'float()')
        # t.insert(INSERT, '\nprint("")\n')
kkkkk = Button(border = 0, padx=20, bg='black', fg='red', text='X', command=e)
kkkkk.place(y=0, x=855)
kkkkk1 = Button(padx=10, bg='black', border = 0, fg='red', text='[-]', command=m)
kkkkk12 = Button(padx=10, bg='black', fg='red', text='run', border = 0, command=run)
# top = Toplevel()
# top.overrideredirect(0)
# top.geometry('1x1')
# top.title('lib')
# top.lift()
# top.resizable(0, 0)
lib__ = Button(root, border = 0, bg = 'black', fg = 'red', text = 'print("")', command = prw, width = 15)
lib__1 = Button(root, border = 0, bg = 'black', fg = 'red', text = 'input("")', command = inp, width = 15)
lib__2 = Button(root, border = 0, bg = 'black', fg = 'red', text = 'int()', command = intv, width = 15)
lib__3 = Button(root, border = 0, bg = 'black', fg = 'red', text = 'str()', command = strv, width = 15)
lib__4 = Button(root, border = 0, bg = 'black', fg = 'red', text = 'float()', command = floatv, width = 15)
# lib__.place(x = 800, y = 30)
kkkkk12.place(x=780, y=0)
kkkkk1.place(y=0, x=820)
# lib__.insert(0, '\nprint("")\n')
lpw = lp['width']
lpmw = lpm['width']
ldpw = ldp['width']
lhw = lh['width']
lhiw = lhi['width']
lh1w = lh1['width']
lph = lp['pady']
lpmh = lpm['pady']
ldph = ldp['pady']
lhh = lh['pady']
lhih = lhi['pady']
lh1h = lh1['pady']
lh.bind('<Enter>', er)
lhi.bind('<Enter>', ho)
kkkkk1.bind('<Button-1>', me)
lh1.bind('<Enter>', ho)
lh.bind('<Leave>', lr)
lh1.bind('<Leave>', go)
lhi.bind('<Leave>', go)
lp.bind('<Leave>', lp_l)
lp1.bind('<Leave>', lp_l)
lp2.bind('<Leave>', lp_l)
lp.bind('<Enter>', lp_e)
lp1.bind('<Enter>', lp_e)
lp2.bind('<Enter>', lp_e)
# kkkkk1.bind('<Leave>', ml)
def dl(e):
    t.insert(INSERT, '\t"')
def dls(e):
    t.insert(INSERT, '\\')
def dl1(e):
    t.insert(INSERT, "\t'")
def dl2(e):
    stp = t.get(0.0, END)
    t.delete(0.0, END)
    t.insert(INSERT, stp + '\t]')
def dl3(e):
    stp = t.get(0.0, END)
    t.delete(0.0, END)
    t.insert(INSERT, stp + '\t}')
def dl4(e):
    t.insert(INSERT, '/')
def dl5(e):
    t.insert(INSERT, '\t>')

def dl7(e):
    stp = t.get(0.0, END)
    t.delete(0.0, END)
    t.insert(INSERT, stp + '\t}')
t.bind('"', dl)
t.bind('\\', dls)
t.bind("'", dl1)
t.bind("[", dl2)
t.bind("{", dl3)
t.bind("/", dl4)
# t.bind(",", dl5)
t.bind("(", dl7)
t.bind("Enter", lib)
t.bind("Leave", lib_l)
root.mainloop()
