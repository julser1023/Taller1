import tkinter as tk
from tkinter import ttk

def main():
    init_window()

def init_window():
    window = tk.Tk()
    window.title('Mi primera Aplicacion')
    window.geometry('400x250')

    label = tk.Label(window, text='Calculadora', font=('Arial bold', 17))
    label.grid(column = 0, row = 0)

    entrada1 = tk.Entry(window, width=10)
    entrada2 = tk.Entry(window, width=10)

    entrada1.grid(column = 1, row = 1)
    entrada2.grid(column = 1, row = 2)

    label_entrada1 = tk.Label(window, text = 'Ingrese el primer numero:', font=('Arial bold',12))
    label_entrada1.grid(column=0, row=1)
    label_entrada2 = tk.Label(window, text ='Ingrese el segundo numero:', font=('Arial bold', 12))
    label_entrada2.grid(column=0, row=2)

    label_operador = tk.Label(window, text='Escoja un operador', font=('Arial bold',12))
    label_operador.grid(column = 0, row = 3)

    combo_operadores = ttk.Combobox(window)
    combo_operadores['values'] = ['+','-','*','/','pow']
    combo_operadores.current(0)
    combo_operadores.grid(column = 1, row = 3)

    label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold',17))
    label_resultado.grid(column = 0, row = 5)

    boton = tk.Button(window,
                    command = lambda: click_calcular(
                    label_resultado, 
                    entrada1.get(),
                    entrada2.get(),
                    combo_operadores.get()),
                    text='Calcular',bg="purple",fg="white")
    boton.grid(column = 1 , row = 4 ) 

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



main()