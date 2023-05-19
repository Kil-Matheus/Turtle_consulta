class Pilha():
    
    def __init__(self):
        self.pilha = []
        
    def tamanho(self):
        if len(self.pilha) == 0:
            return print("A Pilha está vazia")
        else:
            return print("A Pilha contem:", len(self.pilha), "itens")
                    
    def desempilhar(self):
        if len(self.pilha) == 0:
            return print("Pilha vazia")
        return self.pilha.pop()
    
    def empilhar(self, valor):
        return self.pilha.append(valor)
    
    def topo(self):
        topo = self.pilha[len(self.pilha)]
        return print(topo)
    
    
def main():
    minha_pilha = Pilha()
    while True:
        minha_pilha.tamanho()
        guardar = input("Que valor você deseja salvar? \n")
        if guardar == 'n':
            pass
        else:
            minha_pilha.empilhar(guardar)
        minha_pilha.tamanho
        resposta = input("Você deseja retirar um elemento (y/n) ou ver a lista(l) \n")
        resposta = resposta.lower()
        if resposta != 'y' and resposta != 'n' and resposta != 'l':
            print("Resposta inválida")
            pass
        elif resposta == 'y':
            minha_pilha.desempilhar()
            minha_pilha.tamanho
        elif resposta == 'n':
            pass
        elif resposta == 'l':
            print(minha_pilha.pilha)
            pass
    
    # minha_pilha.empilhar(1)
    # minha_pilha.empilhar(5)
    # minha_pilha.empilhar(9)
    # minha_pilha.tamanho()
    
if __name__ == "__main__":
    main()