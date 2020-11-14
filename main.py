# -*- coding: latin1 -*-

from tkinter import *

def calculo():
   valor1 = float(entry_field_3.get())
   valor2 = float(entry_field_4.get())
   resultado = valor2/((valor1/100) * (valor1/100))

   result_field.delete(0, END)
   result_field.insert(0, resultado)


root = Tk()
root.title('Calculadora do IMC - indice de Massa Corporal')

label_1 = Label(root, text='nome do Paciente').grid(row=1, column=0)
entry_field_1 = Entry(root, text='texto 1', width=50)
entry_field_1.grid(row=1, column=1)

label_2 = Label(root, text='Endereço completo').grid(row=2, column=0)
entry_field_2 = Entry(root, text='texto 2', width=50)
entry_field_2.grid(row=2, column=1)

label_3 = Label(root, text='Altura(cm)').grid(row=3, column=0)
entry_field_3 = Entry(root, text='Número 1', width=10)
entry_field_3.grid(row=3, column=1)

label_4 = Label(root, text='Peso(Kg)').grid(row=4, column=0)
entry_field_4 = Entry(root, text='Número 2', width=10)
entry_field_4.grid(row=4, column=1)

botao = Button(root, text='Calcular', command=calculo, width='30').grid(row=5, column=0, columnspan=2)

label_5 = Label(root, text='Resultado').grid(row=3, column=2)

result_field = Entry(root, width=50)
result_field.grid(row=4, column=2)

root.mainloop()

