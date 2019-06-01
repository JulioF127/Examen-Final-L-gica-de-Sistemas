#Logica de Sistemas
#1er. Semestre
#Julio Fernando Fuentes Bocanegra
#0907-19-10520
from tkinter import ttk
from tkinter import *
   
class Examen:
    def __init__(self, window):
       

       
        ancho = 800
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

       
        Button(frame, text = 'Boton 1', background ="#307d99", command = self.funcion1).grid(row = 3, columnspan = 2, sticky = W + E)
        Button(frame, text = 'Boton 2', background ="#307d99", command = self.funcion2).grid(row = 4, columnspan = 2, sticky = W + E)
      
        
        self.message = Label(text = '', fg = 'blue', background="#1fa388")
        self.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)
        self.message2 = Label(text = '', fg = 'blue', background="#1fa388")
        self.message2.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)

    def validation(self):
        return len(self.var1.get()) != 0 and len(self.var2.get()) != 0 and len(self.var3.get()) != 0


    def funcion1(self):
        if self.validation():
            if int( self.var1.get() ) < int( self.var3.get()):
                resultadomulti = int( self.var1.get() ) * int( self.var2.get()) * int(self.var3.get()) 
                self.message['text'] = 'El primer número es menor que el tercero, se ha realizado una multiplicación y el resultado es: {}'.format(int(resultadomulti))
            if int( self.var1.get() ) == int( self.var3.get()):
                resultadosuma = int( self.var1.get() ) + int( self.var2.get()) + int(self.var3.get())
                self.message['text'] = 'El primer número es igual al tercero, se ha realizado una suma y el resultado es: {}'.format(int(resultadosuma))
            if int( self.var2.get() ) == 0:
                if int( self.var1.get() ) <= int( self.var3.get()):
                    resultadoresta1 = int( self.var3.get() ) - int( self.var1.get())
                    self.message['text'] = 'Se ha restado el primer número al tercero y el resultado es: {}'.format(int(resultadoresta1))
                else:
                    resultadoresta2 = int( self.var1.get() ) - int( self.var3.get())
                    self.message['text'] = 'Se ha restado el tercer número al primero y el resultado es: {}'.format(int(resultadoresta2))
        else:
            self.message['text'] = 'Los campos son necesarios.' 
    def funcion2(self):
        if self.validation():
            ntextos = int( self.var1.get() ) * int( self.var2.get())
            concatenacion = str( self.var1.get() ) + str( self.var2.get()) + str(self.var3.get())
            self.message['text'] = '{}'.format(str(concatenacion))
           
             
if __name__ == '__main__':

    window = Tk()

    
    app = Examen(window)
   

    window.mainloop()