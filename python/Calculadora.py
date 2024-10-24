from tkinter import *

root = Tk()
root.title("Calculadora")
root.geometry("408x355")
root.minsize(408,355)
root.maxsize(408,355)



#Globals
numero1 = ''
divisao = FALSE
multiplica = FALSE
menos = FALSE
mais = FALSE

root.configure(background='black')

# Entry field
e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='white', bg='gray', font=('futura', 25, 'bold'), justify=CENTER )
e.grid(
    
    row=0,
    column=0,
    columnspan=4,
    pady= 2
                  )


 #Buttons

 # Functions
def botao_click(num):
       e.insert(END,num)

def botao_divisao():
       global numero1
       global divisao
       divisao = TRUE
       numero1 = e.get()
       e.delete(0,END)

def botao_multiplica():
       global numero1
       global multiplica
       multiplica = TRUE
       numero1 = e.get()
       e.delete(0,END)

def botao_menos():
       global numero1
       global menos
       menos = TRUE
       numero1 = e.get()
       e.delete(0,END)

def botao_mais():
        global numero1
        global mais
        mais = TRUE
        numero1 = e.get()
        e.delete(0,END)     
       
       
def botao_limpar():
       e.delete(0, END)     


def botao_igual():
    global menos, mais, multiplica, divisao
    numero2 = e.get()
    e.delete(0, END)
    
    if mais == TRUE:
       e.insert(0, int(numero1) + int(numero2))
       mais = FALSE

    if menos == TRUE:
         e.insert(0, int(numero1) - int(numero2))
         menos = FALSE

    if multiplica == TRUE:
              e.insert(0 , int(numero1) * int(numero2))
              multiplica = False

    if divisao == TRUE:
                     e.insert(0, int(numero1) / int(numero2))
                     divisao = False


         
  



# Button layout

divide = Button(root,
                    text='÷',
                    padx=40,
                    pady=20,
                    command=botao_divisao,
                    fg="white",
                    activeforeground='blue',
                    bg="gray",
                    activebackground='white',
                    relief=FLAT,
                    font=('futura', 12, 'bold')

 
 
 
 )       

divide.grid(row=0, column=4)


#Numbers Buttons

#first row


um = Button(root,
                 text='1',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(1),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

um.grid(row=1,column=1)   




dois = Button(root,
                 text='2',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(2),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

dois.grid(row=1,column=2)

tres = Button(root,
                 text='3',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(3),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

tres.grid(row=1,column=3)

plus = Button(root,
                 text='+',
                 padx=40,
                 pady=20,
                 command= botao_mais,
                 fg='white',
                 activeforeground='white',
                 bg='gray',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

plus.grid(row=1,column=4)


#second row

quatro = Button(root,
                 text='4',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(4),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

quatro.grid(row=2,column=1)


cinco = Button(root,
                 text='5',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(5),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

cinco.grid(row=2,column=2)


seis = Button(root,
                 text='6',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(6),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

seis.grid(row=2,column=3)



vezes = Button(root,
                 text='×',
                 padx=40,
                 pady=20,
                 command= botao_multiplica,
                 fg='white',
                 activeforeground='white',
                 bg='gray',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

vezes.grid(row=2,column=4)


# third row
sete = Button(root,
                 text='7',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(7),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

sete.grid(row=3,column=1)


oito = Button(root,
                 text='8',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(8),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

oito.grid(row=3,column=2)


nove = Button(root,
                 text='9',
                 padx=40,
                 pady=20,
                 command=lambda: botao_click(9),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

nove.grid(row=3,column=3)



menos = Button(root,
                 text='-',
                 padx=41.5,
                 pady=20,
                 command= botao_menos,
                 fg='white',
                 activeforeground='white',
                 bg='gray',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

menos.grid(row=3,column=4)


#fourth row

zero = Button(root,
                 text='0',
                 padx=91,
                 pady=20,
                 command=lambda: botao_click(0),
                 fg='white',
                 activeforeground='white',
                 bg='black',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

zero.grid(row=4,column=1, columnspan=2)


clear = Button(root,
                 text='C',
                 padx=40,
                 pady=20,
                 command= botao_limpar,
                 fg='white',
                 activeforeground='white',
                 bg='gray',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

clear.grid(row=4,column=3)



igual = Button(root,
                 text='=',
                 padx=40,
                 pady=20,
                 command= botao_igual,
                 fg='white',
                 activeforeground='white',
                 bg='green',
                 activebackground='blue',
                 relief=FLAT,
                 font=('futura', 12, 'bold')

                 )  

igual.grid(row=4,column=4)

root.mainloop()