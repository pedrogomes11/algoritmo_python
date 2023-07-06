
class Fila:

    def __init__(self):
        self.head = None
        self.elementos = [None]
        self.posicao=None
        
    def is_full(self):
        if self.posicao +1 == self.tam:
            return True
        else:
            return False
       


    def definir_fila(self,tam):
        self.tam = tam
        self.elementos=self.elementos*tam
    

    def enqueue(self,elemento):
        if self.head==None:
            self.head= elemento
            self.posicao = 0
            self.elementos[self.posicao] = elemento
        elif not self.is_full():
            self.elementos[self.posicao+1]=elemento
            self.posicao+=1

        else:
            self.elementos
            self.elementos[self.posicao+1]=elemento
            self.posicao+=1

    def mostrarfila(self):
        print(self.elementos)




fila = Fila()
fila.definir_fila(4)
fila.mostrarfila()
fila.enqueue(3)
fila.mostrarfila()
fila.enqueue(10)
fila.mostrarfila()
fila.enqueue(4)
fila.mostrarfila()



