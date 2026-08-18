class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None

    def __repr__(self):
        return f"[{self.color}, {self.number}]"

class SinglyLinkedList:
    def __init__(self, nodos):
        self.head = None
        if nodos is not None:
            nodo = Card()

while True:
    print("1 - Adicionar paciente a fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - Sair")

    op = int(input("Escolha uma opcao: "))
    if op == 1:
        cardColor = input("Informe a cor do cartao: ")
        if cardColor == "V":
            cardGreenNumber = int(input("Informe o numero do cartao: "))
            if cardGreenNumber > 200:
                print("O numero dos cartoes verdes vao somente ate 200.")
            elif cardGreenNumber <= 0:
                print("O numero do cartao precisa ser maior que 0.")
        elif cardColor == "A":
            cardYellowNumber = int(input("Informe o numero do cartao: "))
            if cardYellowNumber < 200:
                print("O numero do cartao amarelo precisa ser maior que 200.")
        else:
            print("Cor invalida!")
    if op == 2:
        print("Mostrando pacientes...")
    if op == 3:
        print("Chamando paciente...")
    if op == 4:
        print("Encerrando...")
        break