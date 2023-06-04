from tkinter import Tk, Button, Entry,StringVar

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("")

#Se definen las funciones necesarias para suma, resta, division y multiplicacion de dos numeros
def agregar_al_calculo(caracter):
    global auxiliar
    auxiliar=auxiliar+str(caracter)
    texto.set(auxiliar)

def resultado():
    global auxiliar
    try:
        #Se usa la funcion de python eval
        auxiliar=str(eval(auxiliar))
        texto.set(auxiliar)
    #Si hay un error, que limpie los números agregados al calculo
    except:
        texto.set("")
    #Se limpia
    auxiliar=""

auxiliar = ""
#Se usa un StringVar para mostrarlo en el entry
texto=StringVar()

#Configuración pantalla de salida
pantalla = Entry(root, width=31, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"),textvariable=texto)
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=0)

# Configuración botones
boton_1 = Button(root, text="1",command=lambda :agregar_al_calculo(1), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=0, pady=1)
boton_2 = Button(root, text="2",command=lambda :agregar_al_calculo(2), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3",command=lambda :agregar_al_calculo(3),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4",command=lambda :agregar_al_calculo(4),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5",command=lambda :agregar_al_calculo(5), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6",command=lambda :agregar_al_calculo(6),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7",command=lambda :agregar_al_calculo(7),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8",command=lambda :agregar_al_calculo(8),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9",command=lambda :agregar_al_calculo(9),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=",command=lambda :resultado(), width=22, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".",command=lambda :agregar_al_calculo("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+",command=lambda :agregar_al_calculo("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", command=lambda :agregar_al_calculo("-"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", command=lambda :agregar_al_calculo("*"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", command=lambda :agregar_al_calculo("/"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()