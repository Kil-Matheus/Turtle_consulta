class Fila():
    
    def __init__(self):
        self.fila = []
    
    def status_fila(self):
        return print(self.fila)
    
    def tamanho(self):
        if len(self.fila) == 0:
            return print("Fila Vazia")
        else:
            return print("A fila tem ",len(self.fila), "itens")
        
    def enfilerar(self, valor):
        return self.fila.append(valor)
    
    def desenfilerar(self):
        if len(self.fila) != 0:
            return self.fila.pop(0)
        else:
            print("A Fila está vazia")
            
    def frente(self):
        return print(self.fila[0])

    
def main():
    minha_fila = Fila()
    while True:
        minha_fila.tamanho()
        resposta = input("Você deseja guarda que valor? \n")
        if resposta == "n":
            pass
        else:
            minha_fila.enfilerar(resposta)
            minha_fila.tamanho()
            pass
        resposta_2 = input("Você deseja andar com a fila? (y/n) \n")
        resposta_2 = resposta_2.lower()
        if resposta_2 == "y":
            minha_fila.desenfilerar()
            minha_fila.status_fila()
            pass

        
if __name__ == "__main__":
    main()