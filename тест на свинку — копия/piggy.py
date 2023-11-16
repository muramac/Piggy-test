from tkinter import *
# from PIL import ImageTk, Image
import tkinter as tk

from PIL import Image, ImageTk


hui = 0  # очки хуёвости
gay = 0  # очки гейминга
mate = 0  # очки умности
exp = 0  # очки исследователя



def onetwoh():
    for i in lists:
        i.destroy()
    lists.clear()
    ques_two()
    global hui
    hui += 1
def onetwog():
    for i in lists:
        i.destroy()
    lists.clear()
    ques_two()
    global gay
    gay += 1
def onetwom():
    for i in lists:
        i.destroy()
    lists.clear()
    ques_two()
    global mate
    mate += 1
def onetwoe():
    for i in lists:
        i.destroy()
    lists.clear()
    ques_two()
    global exp
    exp += 1
def twothreeh():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global hui
    hui += 1
    ques_three()
def twothreeg():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global gay
    gay += 1
    ques_three()
def twothreem():
    for i in lists:
        i.destroy()
    lists.clear()
    global mate
    mate += 1
    ques_three()
def twothreee():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global exp
    exp += 1
    ques_three()

def threefourh():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global hui
    hui += 1
    ques_four()
def threefourg():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global gay
    gay += 1
    ques_four()
def threefourm():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global mate
    mate += 1
    ques_four()
def threefoure():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global exp
    exp += 1
    ques_four()
def fourfiveh():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global hui
    hui += 1
    ques_five()
def fourfiveg():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global gay
    gay += 1
    ques_five()

def fourfivem():
    #x += 1
    for i in lists:
        i.destroy()
    global mate
    mate += 1
    lists.clear()
    ques_five()

def fourfivee():
    #x += 1
    for i in lists:
        i.destroy()
    lists.clear()
    global exp
    exp += 1
    ques_five()

def finalmate():        #я удалил функцию final и заменил её на отдельные функции, добавляющие очки(такие же функции как выше), в итоге теперь выводится какая-то хуйня и я не могу работать с этим дальше
    for i in lists:
        i.destroy()
    lists.clear()
    global mate
    mate += 1
    finale()

def finalhui():
    for i in lists:
        i.destroy()
    lists.clear()
    global hui
    hui += 1
    finale()

def finalgay():
    for i in lists:
        i.destroy()
    lists.clear()
    global gay
    gay += 1
    finale()

def finalexp():
    for i in lists:
        i.destroy()
    lists.clear()
    global exp
    exp += 1
    finale()


root = tk.Tk()
root.title("Какая ты свинка")
root.geometry('1260x980')
lists = []

def ques_one():
    lbl_1 = Label(root, text="1. В своё свободное время ты предпочитаешь:", font=("Comic Sans", 26))
    lbl_1.pack()
    lists.append(lbl_1)
    btn_1 = Button(root, text="Самосовершенствоваться", width=50, height=3, font=30, command=onetwom)
    btn_1.pack()  # mate
    lists.append(btn_1)
    btn_2 = Button(root, text="Дрочить", width=50, height=3, font=30, command=onetwoh)
    btn_2.pack()  # hui
    lists.append(btn_2)
    btn_3 = Button(root, text="Ебашиться на своей пекарне во что-то", width=50, height=3, font=30, command=onetwog)
    btn_3.pack()  # gay
    lists.append(btn_3)
    btn_4 = Button(root, text="Смотреть аниме", width=50, height=3, font=30, command=onetwoe)
    btn_4.pack()  # exp
    lists.append(btn_4)
def ques_two():
    lbl_2 = Label(root, text="2. Какая твоя любимая пица:", font=("Comic Sans", 26))
    lbl_2.pack()
    lists.append(lbl_2)
    btn_6 = Button(root, text="4 сыра мазерати", width=50, height=3, font=30, command=twothreem)
    btn_6.pack()
    lists.append(btn_6)  # mate
    btn_7 = Button(root, text="Гавайская", width=50, height=3, font=30, command=twothreeh)
    btn_7.pack()
    lists.append(btn_7)  # hui
    btn_8 = Button(root, text="Чедер", width=50, height=3, font=30, command=twothreeg)
    btn_8.pack()
    lists.append(btn_8)  # gay
    btn_9 = Button(root, text="Пепярони", width=50, height=3, font=30, command=twothreee)
    btn_9.pack()
    lists.append(btn_9)  # exp
def ques_three():
    lbl_3 = Label(root, text="3. Любимое аниме:", font=("Comic Sans", 26))
    lbl_3.pack()
    lists.append(lbl_3)
    btn_10 = Button(root, text="Во все тяжечки", width=50, height=3, font=30, command=threefourm)
    btn_10.pack()
    lists.append(btn_10)  # mate
    btn_11 = Button(root, text="Почему моя младшая сестра такая милая", width=50, height=3, font=30, command=threefourh)
    btn_11.pack()
    lists.append(btn_11)  # hui
    btn_12 = Button(root, text="Секс сырков", width=50, height=3, font=30, command=threefourg)
    btn_12.pack()
    lists.append(btn_12)  # gay
    btn_13 = Button(root, text="Подиковый клуб", width=50, height=3, font=30, command=threefoure)
    btn_13.pack()
    lists.append(btn_13)  # exp
def ques_four():
    lbl_4 = Label(root, text="4. Ты ненавидишь:", font=("Comic Sans", 26))
    lbl_4.pack()
    lists.append(lbl_4)
    btn_14 = Button(root, text="Наглость", width=50, height=3, font=30, command=fourfivem)
    btn_14.pack()
    lists.append(btn_14)  # mate
    btn_15 = Button(root, text="Когда вместо того, чтобы сосать тебе она гавкает и виляет хвостом", width=70, height=3,font=30, command=fourfiveh)
    btn_15.pack()
    lists.append(btn_15)  # hui
    btn_16 = Button(root, text="Когда броу не заходит в дотку", width=50, height=3, font=30, command=fourfiveg)
    btn_16.pack()
    lists.append(btn_16)  # gay
    btn_17 = Button(root, text="Чурок", width=50, height=3, font=30, command=fourfivee)
    btn_17.pack()
    lists.append(btn_17)  # exp
def ques_five():
    lbl_5 = Label(root, text="5. По жизни ты:", font=("Comic Sans", 26))
    lbl_5.pack()
    lists.append(lbl_5)
    btn_18 = Button(root, text="Продажа Трактор Кировец К-702МВА-УДМ2, 2003 год в Новом Уренгое", width=70, height=3, font=30, command=finalmate)
    btn_18.pack()
    lists.append(btn_18)  # mate
    btn_19 = Button(root, text="Сигма", width=50, height=3, font=30, command=finalhui)
    btn_19.pack()
    lists.append(btn_19)   # hui
    btn_20 = Button(root, text="Додо", width=50, height=3, font=30, command=finalgay)
    btn_20.pack()
    lists.append(btn_20)   # gay
    btn_21 = Button(root, text="Навозная яма, а твои кенты - это мухи", width=50, height=3, font=30, command=finalexp)
    btn_21.pack() 
    lists.append(btn_21)  # exp
'''btn_22 = tk.Button(root, text="Результаты", fg='red', width=16, height=1, font=("Comic Sans", 26), command=results)
btn_22.pack()'''
def finale():
    if hui == 5 and gay == 0 and exp == 0 and mate == 0:
        lbl_6 = tk.Label(root, text='Ты просто невменяемый уебан', font=("Comic Sans", 26))
        lbl_result_1 =  tk.Label(root, text='Ты - это олицетворение пиздеца и хуёвости, лично после такого ужасного' + '\n' + 'результата я бы захуярил тебя сам голыми руками, как и любой другой человек.' + '\n' + 'Иди лечись, долбаёб, ты - мега хуёвый срущий кабан. долбаёб', font=("Comic Sans", 20))
        img = PhotoImage(file = 'final.png')
        lbl_pikcha = Label(root)
        lbl_pikcha.configure(image=img,width=img.width(),height=img.height())
        lbl_pikcha.image = img
        lbl_6.pack()
        lbl_result_1.pack()
        lbl_pikcha.pack()
    elif hui == 0 and gay == 5 and exp == 0 and mate == 0:
        lbl_7 = tk.Label(root, text = "Ты гуль - свинья", font=("Comic Sans", 26))
        lbl_result_2 = tk.Label(root, text="Все очевидно, ты любишь доту и свой пека" + '\n' + "любое женское внимание ты бы с радостью променял на пару толстых," + '\n' + " жилистых членов. Единственная вещь, озаряющая твою жизнь" + '\n' + " - это твой, отчим, ебущий тебя" +'\n' + "в жопу, каждый раз как ты пикаешь эсфа", font=("Comic Sans", 26))
        img1 = PhotoImage(file = 'final2.png')
        lbl_pikcha1 = Label(root)
        lbl_pikcha1.configure(image=img1, width=img1.width(),height=img1.height())
        lbl_pikcha1.image = img1
        lbl_7.pack()
        lbl_result_2.pack()
        lbl_pikcha1.pack()
    elif hui == 0 and gay == 0 and exp == 5 and mate == 0:
        lbl_8 = tk.Label(root, text = "Ты - фарш ебанный", font=("Comic Sans", 26))
        lbl_result_3 = tk.Label(root, text="Ты нормис, но немного скучный. иди нахуй", font=("Comic Sans", 26))
        img2 = PhotoImage(file = 'final4.png')
        lbl_pikcha2 = Label(root)
        lbl_pikcha2.configure(image=img2, width=img2.width(),height=img2.height())
        lbl_pikcha2.image = img2
        lbl_8.pack()
        lbl_result_3.pack()
        lbl_pikcha2.pack()
    elif hui == 0 and gay == 0 and exp == 0 and mate == 5:
        lbl_9 = tk.Label(root, text = "Ты - хайповая свинка",font=("Comic Sans", 26))
        lbl_result_4 = tk.Label(root, text="Хайповая свинка - зумер, ты" + '\n' + "ты скорее всего куришь электронные пиписьки и" + '\n' + "занимаешься другими зумерскими" + '\n' + "делишками которые так популярны в стаде", font=("Comic Sans", 26))
        img3 = PhotoImage(file = 'final1.png')
        lbl_pikcha3 = Label(root)
        lbl_pikcha3.configure(image=img3, width=img3.width(),height=img3.height())
        lbl_9.pack()
        lbl_result_4.pack()
        lbl_pikcha3.image = img3
        lbl_pikcha3.pack()
    elif hui >= 3:
        lbl_10 = tk.Label(root, text = "Ты - свинка импостер",font=("Comic Sans", 26))
        lbl_result_5 = tk.Label(root, text= "Если с тобой не общаться, то ты с виду вроде" + '\n' + "как нормальный парень, но стоит копнуть чутка поглубже," + '\n' + "чтобы все узнали что ты полон хуебесов. Если тебя оставить в загоне" + '\n' + "с животными, то будучи свиньей ты выебешь всех кур истанешь главным петухом", font=("Comic Sans", 14))
        img4 = PhotoImage(file = 'final3.png')
        lbl_pikcha4 = Label(root)
        lbl_pikcha4.configure(image=img4, width=img4.width(),height=img4.height())
        lbl_10.pack()
        lbl_result_5.pack()
        lbl_pikcha4.image = img4
        lbl_pikcha4.pack()
    elif exp >= 3:
        lbl_11 = tk.Label(root, text = "Ты - хамон",font=("Comic Sans", 26))
        lbl_result_6 = tk.Label(root, text= "Хамон поинтереснее фарша, но ты всё равно блядский нёрд", font=("Comic Sans", 20))
        img5 = PhotoImage(file = 'final5.png')
        lbl_pikcha5 = Label(root)
        lbl_pikcha5.configure(image=img5, width=img5.width(),height=img5.height())
        lbl_11.pack()
        lbl_result_6.pack()
        lbl_pikcha5.image = img5
        lbl_pikcha5.pack()
    elif mate >= 3:
        lbl_12 = tk.Label(root, text = "Хрюксада Пигладан",font=("Comic Sans", 26))
        lbl_result_7 = tk.Label(root, text= "Постоянно на приколе, ебашишь разрывные шутки" + '\n' + "готов дажеах хахаха хаахАХАХхахаХАхахаХахаХахАХахахАхаХАхХАХАхаХА" + '\n' + "хАхаХахАХАХАХхаХАХАХАХХАХАХАХАХАХХХААХХАХахХХахХАхХАххХАхаХаХахХ" + '\n' + "аХахахХхХАхахаХАХАхаХхаХАххаХАхАХхАхАхаХАхАхХАхахаХАХАХАхАХахАХхАхаХХАХАХ" + '\n' + "ХХХХХХААААААААААААААААААХхАХхаХахахХАХАхаХахАХАХАХХХХахахХАХахХ" + '\n' + "ХАХхахахахахахХАххахаХАХхаХххахХАХАхАХАХахах", font=("Comic Sans", 20))
        img6 = PhotoImage(file = 'final6.png')
        lbl_pikcha6 = Label(root)
        lbl_pikcha6.configure(image=img6, width=img6.width(),height=img6.height())
        lbl_12.pack()
        lbl_result_7.pack()
        lbl_pikcha6.image = img6
        lbl_pikcha6.pack()
    elif gay >= 3:
        lbl_13 = tk.Label(root, text = "Латентный дотер",font=("Comic Sans", 26))
        lbl_result_8 = tk.Label(root, text= "Ты один из тех людей к которым лучше не поворачиваться спиной" + '\n' + "о тебе ходят слухи, что как-то раз ты выебал всё свиное стадо", font=("Comic Sans", 20))
        img7 = PhotoImage(file = 'final7.png')
        lbl_pikcha7 = Label(root)
        lbl_pikcha7.configure(image=img7, width=img7.width(),height=img7.height())
        lbl_13.pack()
        lbl_result_8.pack()
        lbl_pikcha7.image = img7
        lbl_pikcha7.pack()
    elif gay >= 2 and hui >= 2:
        lbl_14 = tk.Label(root, text = "Криповый кабан",font=("Comic Sans", 26))
        lbl_result_9 = tk.Label(root, text= "Порось, которому лучше не пиздеть лишнего," + '\n' + "сбежал со сибиреязвенного скотомогильника, характер скверный, не женат", font=("Comic Sans", 20))
        img8 = PhotoImage(file = 'final8.png')
        lbl_pikcha8 = Label(root)
        lbl_pikcha8.configure(image=img8, width=img8.width(),height=img8.height())
        lbl_14.pack()
        lbl_result_9.pack()
        lbl_pikcha8.image = img8
        lbl_pikcha8.pack()
    elif exp >= 2 and mate >= 2:
        lbl_15 = tk.Label(root, text = "АХАХАХАХАХАХА это кто нахуй",font=("Comic Sans", 26))
        lbl_result_10 = tk.Label(root, text= "Еблан, ты как блять вообще получил этот результат", font=("Comic Sans", 20))
        img9 = PhotoImage(file = 'final9.png')
        lbl_pikcha9 = Label(root)
        lbl_pikcha9.configure(image=img9, width=img9.width(),height=img9.height())
        lbl_15.pack()
        lbl_result_10.pack()
        lbl_pikcha9.image = img9
        lbl_pikcha9.pack()
    elif hui >= 2 and mate >= 2:
        lbl_16 = tk.Label(root, text = "Хог в заточении",font=("Comic Sans", 26))
        lbl_result_11 = tk.Label(root, text= "Ты норм кент, но порой бываешь непослушной свинкой" + '\n' + "для твоего же блага и в целях сохранения анальной девственности"  + '\n' + "поросячьего стада тебя поместили в дурку", font=("Comic Sans", 20))
        img10 = PhotoImage(file = 'final10.png')
        lbl_pikcha10 = Label(root)
        lbl_pikcha10.configure(image=img10, width=img10.width(),height=img10.height())
        lbl_16.pack()
        lbl_result_11.pack()
        lbl_pikcha10.image = img10
        lbl_pikcha10.pack()
    elif hui >= 2 and exp >= 2:
        lbl_17 = tk.Label(root, text = "Философ",font=("Comic Sans", 26))
        lbl_result_12 = tk.Label(root, text= "Свинка филосовствствующая о жизни, но из-за своей" + '\n' + "поросячей натуры, не в силах изменить собственную жизнь", font=("Comic Sans", 20))
        img11 = PhotoImage(file = 'final11.png')
        lbl_pikcha11 = Label(root)
        lbl_pikcha11.configure(image=img11, width=img11.width(),height=img11.height())
        lbl_17.pack()
        lbl_result_12.pack()
        lbl_pikcha11.image = img11
        lbl_pikcha11.pack()
    elif gay >= 2 and exp >= 2:
        lbl_18 = tk.Label(root, text = "Хойщик",font=("Comic Sans", 26))
        lbl_result_13 = tk.Label(root, text= "Zrada! *hoink* Männer Peremoga des deutschen Reichstages! " + '\n' + " Seit *hoink* Monaten leiden wir alle unter der Qual eines Problems, " + '\n' + " das uns auch der *hoink* Versailler Vertrag, d.h. das Versailler Diktat, " + '\n' + " einst beschert hat *weeeeeee* ", font=("Comic Sans", 20))
        img12 = PhotoImage(file = 'final12.png')
        lbl_pikcha12 = Label(root)
        lbl_pikcha12.configure(image=img12, width=img12.width(),height=img12.height())
        lbl_18.pack()
        lbl_result_13.pack()
        lbl_pikcha12.image = img12
        lbl_pikcha12.pack()
    elif gay >= 2 and mate >= 2:
        lbl_19 = tk.Label(root, text = "Патимейкер",font=("Comic Sans", 26))
        lbl_result_14 = tk.Label(root, text= "скр скр скр в мёртвых найках скр скр скр патимейкер", font=("Comic Sans", 20))
        img13 = PhotoImage(file = 'final13.png')
        lbl_pikcha13 = Label(root)
        lbl_pikcha13.configure(image=img13, width=img13.width(),height=img13.height())
        lbl_19.pack()
        lbl_result_14.pack()
        lbl_pikcha13.image = img13
        lbl_pikcha13.pack()
    
    else:
        labl = Label(root, text="Данил - клоун", font=("Comic Sans", 26))
        labl.pack()


ques_one()
root.mainloop()



    















