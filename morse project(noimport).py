from tkinter import *
from tkinter import messagebox


tomorse={'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','.':'.-.-.-',',':'--..--',':':'---...','?':'..--..',"'":'.----.','-':'-....-','/':'-..-.','(':'-.--.',')':'-.--.-','"':'.-..-.','=':'-...-','+':'.-.-.','@':'.--.-.'}
frommorse={}
for key,value in tomorse.items():
    frommorse[value]=key


#создание окна
okno = Tk()
okno.minsize(420,300)
okno.geometry("620x300")
okno.title('Переводчик: Азбука морзе')

#функция перевода
def perevod(kyda,text):
    if kyda==1:   
         textboxout.delete(1.0,END)
         count=0
         res=''
         i=0
         while i!=len(text):
             if text[i]==' ':
                 count+=1
                 i+=1
                 if count==7:                     
                     ttext=text[:i]
                     for j in ttext.split():
                         symbol=frommorse.get(j)
                         res+=symbol
                     res+=' '
                     text=text[i:]
                     i=0
                     count=0
             if text[i]!=' ':
                 count=0
                 i+=1
             if i==len(text):
                     for j in text.split():
                         symbol=frommorse.get(j)
                         res+=symbol
         textboxout.insert(INSERT,res)
    else:
         textboxout.delete(1.0,END)
         res=''
         i=0
         while i!=len(text):
             if text[i]==' ':
                 ttext=text[:i]
                 for j in ttext:
                    symbol=tomorse.get(j.upper())
                    res=res+symbol+' '
                 res+='      '
                 text=text[i+1:]
                 i=0
             if text[i]!=' ':
                 i+=1
             if i==len(text):
                     for j in text:
                         symbol=tomorse.get(j.upper())
                         res=res+symbol+' '
         textboxout.insert(INSERT,res[:len(res)-1])
    
def info():
    messagebox.showinfo("Пояснение","-Тире равно трем точкам.\n-Интервал между сигналами, образющими один символ, равен одной точке.\n-Интервал между двумя символами равен трем точкам.\n-Интервал между двумя словами равен семи точкам.\n")
    

##########создание интерфейса
    
#кнопка выбора языка
yaz = IntVar()
naeng = Radiobutton(okno, text="Морзе -> Английский",font="Verdana", variable=yaz, value=1)
naeng.select()
namorse = Radiobutton(okno, text="Английский -> Морзе",font="Verdana", variable=yaz, value=2)

#кнопки
leave = Button(okno, text="Выход",font="Verdana",activebackground="red",command=okno.destroy)
translate = Button(okno, text="Перевести",font="Verdana",command=lambda:perevod(yaz.get(),textboxin.get("1.0",'end-1c')))
info = Button(okno, text="Информация",font="Verdana",activebackground="blue",command=info)
#окно ввода
textboxin = Text(okno,height=5,width=30)

#окно вывода
textboxout = Text(okno,height=5,width=30)

#заголовки
title=Label(okno,text='Переводчик',font="Verdana, 20")
inp=Label(okno,text='Ввод',font="Verdana")
out=Label(okno,text='Вывод',font="Verdana")

#размещение обьектов в окне
title.place(anchor="center",relx=0.5,rely=0.1)
inp.place(relx=0.05,rely=0.2)
out.place(relx=0.6,rely=0.2)
textboxin.place(relx=0.05,rely=0.35,relwidth=0.35,relheight=0.3)
textboxout.place(relx=0.6,rely=0.35,relwidth=0.35,relheight=0.3)
leave.place(relx=0.85,rely=0.85)
info.place(x=10,y=10)
translate.place(anchor="center",relx=0.5,rely=0.85)
naeng.place(relx=0.05,rely=0.7)
namorse.place(relx=0.6,rely=0.7)
