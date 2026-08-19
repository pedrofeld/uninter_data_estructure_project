class Card:
    def __init__(self, color, number):
        self.color = color
        self.number = number
        self.next = None

    def __repr__(self):
        data = f"[{self.color}, {self.number}]"
        return data

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.greenNumber = 1
        self.yellowNumber = 201

    def __repr__(self):
        nodo = self.head
        nodos = []
        while nodo is not None:
            nodos.append(str(nodo))
            nodo = nodo.next
        nodos.append("None")
        return " -> ".join(nodos)

    def insertWithoutPriority(self, nodo):
        current_nodo = self.head
        while current_nodo.next is not None:
            current_nodo = current_nodo.next
        current_nodo.next = nodo

    def insertWithPriority(self, nodo):
        if self.head.color == "V":
            nodo.next = self.head
            self.head = nodo
            return
        current_nodo = self.head
        while current_nodo.next is not None and current_nodo.next.color == "A":
            current_nodo = current_nodo.next
        nodo.next = current_nodo.next
        current_nodo.next = nodo

def insert(list):
    color = input("Informe a cord do cartao (A ou V): ").strip().upper()

    if color == "V":
        number = list.greenNumber
        list.greenNumber += 1
    elif color == "A":
        number = list.yellowNumber
        list.yellowNumber += 1
    else:
        print("Cor invalida!")
        return

    nodo = Card(color, number)

    if list.head is None:
        list.head = nodo
    elif color == "V":
        list.insertWithoutPriority(nodo)
    elif color == "A":
        list.insertWithPriority(nodo)
    else:
        print("Cor invalida!")

    print(f"Paciente cadastrado com o cartao {color}{number}.")

def printWaitList(list):
    if list.head is None:
        print("Nao ha pacientes na fila")
        return
    print("Fila de espera:")
    nodo = list.head
    while nodo is not None:
        print(f"{nodo.color}{nodo.number}")
        nodo = nodo.next

def attendPatient(list):
    if list.head is None:
        print("Nao ha pacientes na fila.")
        return
    nodo = list.head
    list.head = list.head.next
    print(f"Proximo paciente para atendimento: cartao {nodo.color}{nodo.number}")

list = SinglyLinkedList()

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