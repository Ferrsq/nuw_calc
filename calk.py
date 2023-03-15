# from tkinter import *
# from tkinter import messagebox

# def set_value(function):# удаление или посдчет
#     if function=='': #
#         lbl['text']='0' # превращает всю строку в '0'
#     else:
#         lbl['text']=str(eval(function)) # подсчет   # eval("2+2")> 4
#     pass

# def logicalc(options): # 1 
#     if options=='C': #проверка для удаления всей строки и вревращает ее в "0"
#         set_value('') #
#     elif options == "DEL": # удаление одного символа при нажатии 
#         set_value(lbl['text'][0:-1]) # срез([0:-1])  "1+1+1+1" > '1+1+1+'
#         # 
#     elif options == "X^2": # возведение в квадрат 
#         set_value(str((eval(lbl["text"]))**2)) #(1+1)**2
#     elif options == "=": #вычисление 
#         set_value(lbl["text"]) # отправляется для подсчета
#     else:
#         if lbl['text']=='0': # проверка если в строке 0 , тогда оно обнулсяется для того чтобы записать символ
#             lbl['text']='' # обнуление 
#         lbl['text']=lbl['text']+options # при нажатии на число или арифметич действие , с права добавляется нажатый символ

#     pass


# root= Tk() # создаем главное окно 
# root['bg']= 'black' # параметр фона (черный)

# root.geometry('485x550') # размер окна
# root.title('Калькулятор') # название окна 
# root.resizable(False,False) # запрещаем пользователю как то изменять размер окна 


# lbl= Label(text='0', font=("Consolas", 21, "bold"), bg='black', foreground='white') # метка со своими параметрами 
# lbl.place(x=11, y=50) # расположение метки в главном окне по координатам 

# btns = [ # будущие кнопки 
# "C", "DEL", "*", "=",
# "1", "2", "3", "/",
# "4", "5", "6", "+", 
# "7", "8", "9", "-",
# "(", "0", ")", "X^2"
# ]


# x =10 #координата для позиционирования кнопок  
# y =140 #координата для позиционирования кнопок



# for bt in btns: # прозод цикла по списку с названиями кнопок 
#     com = lambda x=bt: logicalc(x)# присваиваем каждой каждой кнопке свою функцию 
#     Button(text=bt, bg="white",font=("Consolas", 15),command=com).place(x=x, y=y,width=115,height=79)# создаем саму кнопку с определенными параметрами
#     x += 117# изменяем координату для того чтобы расположить кнокпи 
#     if x > 400:# проверка для перехода на след. строку 
#         x =10#координата для позиционирования кнопок
#         y +=81#координата для позиционирования кнопок

# root.mainloop()


# moth = int(input('введите номер месяца: '))
# def moth_w(number):
#     if number==12 or number==1 or number==2:
#         print('это зима')
#     if number==3 or number==4 or number==5:
#         print('это весна')
#     if number==6 or number==7 or number==8:
#         print('это лето')
#     if number==9 or number==10 or number==11:
#         print('это осень')


# moth_w(moth)




   
    
  

