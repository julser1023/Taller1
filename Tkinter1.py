import tkinter as tk
from tkinter import ttk
from tkinter import *

def main():
    init_window()

def init_window():

    window = tk.Tk()
    window.title('Mi primera Aplicacion')
    window.geometry('400x250')
    window.configure(bg='green')
    menu = Menu(window)

    item1 = Menu(menu)
    item2 = Menu(menu)
    item3 = Menu(menu)

    item1.add_command(label='Nuevo',command=init_window)
    item1.add_command(label="Prueba", command=prueba)
    item1.add_command(label="Salir", command=window.quit)

    item1.add_separator()

    item2.add_command(label='Editar',command=configurar)

    menu.add_cascade(label='Archivo', menu=item1)
    menu.add_cascade(label='Configurar', menu=item2)
    

    window.config(menu=menu)

    res = 0
    label = tk.Label(window, text='Calculadora', font=('Arial bold', 17),bg="white",fg="purple")
    label.grid(column = 0, row = 0)

    
    entrada1 = tk.Spinbox(window, from_=0, to=100, width=5)
    entrada1.grid(column=1,row=1)
    entrada2 = tk.Spinbox(window, from_=0, to=100, width=5)
    entrada2.grid(column=1,row=2)

    #entrada1.grid(column = 1, row = 1)
    #entrada2.grid(column = 1, row = 2)

    label_entrada1 = tk.Label(window, text = 'Ingrese el primer numero:', font=('Arial bold',12),bg="yellow",fg="blue")
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(window, text ='Ingrese el segundo numero:', font=('Arial bold', 12),bg="yellow",fg="blue")
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(window, text='Escoja un operador', font=('Arial bold',12), bg="yellow",fg="blue")
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row = 3)

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold',17) ,bg="yellow",fg="blue")
    label_resultado.grid(column = 0, row = 5)


    #label_entrada3 = tk.Label(window, text = 'Boton presionado: ', font=('Arial bold',12),bg="yellow",fg="blue")
    #label_entrada3.grid(column=0, row=6)

    boton = tk.Button(window,
                    command = lambda: click_calcular(
                    label_resultado, 
                    entrada1.get(),
                    entrada2.get(),
                    combo_operadores.get()),
                    text='Calcular',bg="red",fg="blue")

    boton.grid(column = 1 , row = 4 ) 
    #messagebox.showerror('Error', 'Las casillas no pueden estar vacias')    
    

    window.mainloop()

def calculadora(num1,num2,operador):
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        resultado = round(num1 / num2,3)
    elif operador == 'pow':
        resultado = num1 ** num2
    return resultado

def click_calcular(label,num1,num2,operador):
     valor1 = float(num1)
     valor2 = float(num2)
     res = calculadora(valor1,valor2,operador)
     label.configure(text = 'Resultado: '+str(res))
     
     
def clickeado():
    res1 = +1 
    label_entrada3.configure(text= 'Resultado: '+str(res1))

def prueba():
    window1 = tk.Tk()
    window1.title("Pruebas")
    window1.geometry('400x250')

    chk_state = BooleanVar()
    chk_state.set(True) 
    chk = tk.Checkbutton(window1, text='Seleccion', var=chk_state)
    chk.grid(column=0, row=0)
    
    opc1 = tk.Radiobutton(window,text='(a)', value=1)
    opc2 = tk.Radiobutton(window,text='(b)', value=2)
    opc3 = tk.Radiobutton(window,text='(c)', value=3)

    opc1.grid(column=1, row=1)
    opc2.grid(column=2, row=1)
    opc3.grid(column=3, row=1)

    window1.mainloop()

def configurar():
    window1 = tk.Tk()
    window1.title("Configurar")
    window1.title("Proximamente")
    window1.geometry('500x300')

    

    window1.mainloop()


main()