from customtkinter import *

root = CTk()
root.title('Calculadora By LuisLR')
root.iconbitmap('./ico/calc.ico')
root.geometry('400x450')
root.resizable(0,0)

fuente = ('Nunito', 27, 'bold')
radio_boton = 20

def Insertar_texto_numeros(texto):
    actual = pantalla.get()

    pantalla.insert(len(actual), texto)
        
def Insertar_signos(texto):
    actual = pantalla.get()
    
    pos1 = len(actual) - 2
    pos2 = len(actual) - 1
    signo = actual[pos1:pos2]
    
    if not actual:
        pass
    elif True if signo in signos else False:
        pass
    elif texto == '.':
        pantalla.insert(len(actual), texto)
    else:
        pantalla.delete(0, END)

        text = actual + ' ' + texto + ' '
        pantalla.insert(len(actual), text)
        
def Resultado():
    signos = ['/', 'X', '-', '+']
    actual = pantalla.get()

    pos1 = len(actual) - 2
    pos2 = len(actual) - 1
    signo = actual[pos1:pos2]

    if not actual:
        pass
    elif True if signo in signos else False:
        pass
    else:
        try:
            texto = pantalla.get()
            lista = texto.split()

            numeros = []
            signos = []
            for elemento in lista:
                if elemento.isdigit() or '.' in elemento:
                    numeros.append(float(elemento))
                else:
                    if elemento == 'X':
                        signos.append('*')
                    else:
                        signos.append(elemento)

            resultado = numeros[0]
            for i in range(len(signos)):
                if signos[i] == '*':
                    resultado *= numeros[i + 1]
                elif signos[i] == '/':
                    resultado /= numeros[i + 1]
                elif signos[i] == '+':
                    resultado += numeros[i + 1]
                elif signos[i] == '-':
                    resultado -= numeros[i + 1]

            pantalla.delete(0, END)
            pantalla.insert(0, str(round(resultado, 3)))  # Display the result

        except ZeroDivisionError:
            pantalla.delete(0, END)
            pantalla.insert(0, "Error: Dividir entre 0")
        except:
            pantalla.delete(0, END)
            pantalla.insert(0, "Error: Entrada Invalida")



# Pantalla

pantalla = CTkEntry(root, width=360, height=80, corner_radius=25)
pantalla.configure(fg_color='#fff', text_color="#000", font=fuente, justify='center')
pantalla.grid(row=0, pady=15, padx=20, columnspan=4)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Botones Numeros

numeros = [[7,4,1], [8,5,2], [9,6,3]]

for i in range(3):
    for a in range(1,4):
        numero = numeros[i][a-1]
        
        boton = CTkButton(root, text=numero, height=65, width=70, font=fuente, corner_radius=radio_boton, fg_color="#5191c1", text_color='#000', border_color="#0a4b75", hover_color='#1e6495', cursor='hand2')
        
        boton.configure(command= lambda numero=numero : Insertar_texto_numeros(numero))
        boton.grid(row=a, column=i, pady=10)

boton_0 = CTkButton(root, text='0', height=65, width=70, font=fuente, corner_radius=radio_boton, fg_color="#5191c1", text_color='#000', border_color="#0a4b75", hover_color='#1e6495', cursor='hand2')

boton_0.configure(command= lambda numero=0 : Insertar_texto_numeros(numero))
boton_0.grid(row=4, column=1, pady=10)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Botones Signos

signos = ['/', 'X', '-', '+']

for i in range(4):
    signo = signos[i]
    boton_signo = CTkButton(root, text=signo, height=65, width=70, font=fuente, corner_radius=radio_boton, fg_color="#fb6f24", hover_color="#bf5015", text_color="#000", cursor='hand2')
    
    boton_signo.configure(command=lambda signo=signo: Insertar_signos(signo))
    boton_signo.grid(row=i+1, column=3, pady=10)

boton_igual = CTkButton(root, text='=', height=65, width=70, font=fuente, corner_radius=radio_boton, fg_color="#06ad00", hover_color="#059400", text_color="#000", cursor='hand2')

boton_igual.configure(command= Resultado)
boton_igual.grid(row=4, column=2)

boton_punto =CTkButton(root, text='.', height=65, width=70, font=fuente, corner_radius=radio_boton, fg_color="#fb6f24", hover_color="#bf5015", text_color="#000", cursor='hand2')

boton_punto.configure(command=lambda signo='.': Insertar_signos(signo))
boton_punto.grid(row=4, column=0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


root.mainloop()