#Logica de Sistemas
#1er. Semestre
#Julio Fernando Fuentes Bocanegra
#0907-19-10520
from tkinter import ttk
from tkinter import *
   
class Dividir:
    def __init__(self, window):
       

       
        ancho = 400
        alto = 400

        
        self.wind = window

        
        self.wind.geometry(str(ancho)+'x'+str(alto))

     
        self.wind.columnconfigure(0, weight=1)

     
        self.wind.title('Examen')

    
        frame = LabelFrame(self.wind, text = 'Examen',background ="#307d99")
        frame.grid(row = 0, column = 0, columnspan = 40, pady = 100)

 
    
        self.var1 = Entry(frame)
        self.var1.focus()
        self.var1.grid(row = 0, column = 0)
    
        self.var2= Entry(frame)
        self.var2.grid(row = 1, column = 0)

        self.var3 = Entry (frame)
        self.var3.grid(row =2, column =0 )

        #Creamos un boton para ejecutar la Division
        Button(frame, text = 'Boton 1', background ="#307d99", command = self.funcion1).grid(row = 3, columnspan = 2, sticky = W + E)
        
      
        
        self.message = Label(text = '', fg = 'blue', background="#1fa388")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        self.message2 = Label(text = '', fg = 'blue', background="#1fa388")
        self.message2.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)

    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0 and len(self.var3.get()) != 0


    def funcion1(self):
        if self.validation():
            if(int( self.var1.get() ) < int( self.var3.get()):
                resultadomulti = int( self.var1.get() ) * int( self.var2.get()) * int(self.var3.get()) )
                self.message['text'] = 'El resultado de la multiplicacion es: {}'.format(int(resultadomulti))
        
        else:
            self.message['text'] = 'los campos son necesarios.' 

    def funcion2(self):
        if self.validation():
            resultado = int( self.var1.get() ) / int( self.var2.get() )
            resultado2 = int( self.var1.get() ) % int( self.var2.get())

            if(resultado2 == 0):
                self.message['text'] = 'La división realizada es exacta y su cociente es: {}'.format(resultado)
            else:
                self.message['text'] = 'La división realizada es inexacta su cociente es: {}'.format(int(resultado)) 
                self.message2['text'] = 'Su residuo es: {}'.format(resultado2)
        else:
            self.message['text'] = 'los campos son necesarios.'   
             
if __name__ == '__main__':

    window = Tk()

    
    app = Dividir(window)
   

    window.mainloop()