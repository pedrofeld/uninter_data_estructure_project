## ATIVIDADE 1 - SISTEMA DE TRIAGEM:

# class Card:
#     def __init__(self, color, number):
#         self.color = color
#         self.number = number
#         self.next = None
#
#     def __repr__(self):
#         data = f"[{self.color}, {self.number}]"
#         return data
#
# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.greenNumber = 1
#         self.yellowNumber = 201
#
#     def __repr__(self):
#         nodo = self.head
#         nodos = []
#         while nodo is not None:
#             nodos.append(str(nodo))
#             nodo = nodo.next
#         nodos.append("None")
#         return " -> ".join(nodos)
#
#     def insertWithoutPriority(self, nodo):
#         current_nodo = self.head
#         while current_nodo.next is not None:
#             current_nodo = current_nodo.next
#         current_nodo.next = nodo
#
#     def insertWithPriority(self, nodo):
#         if self.head.color == "V":
#             nodo.next = self.head
#             self.head = nodo
#             return
#         current_nodo = self.head
#         while current_nodo.next is not None and current_nodo.next.color == "A":
#             current_nodo = current_nodo.next
#         nodo.next = current_nodo.next
#         current_nodo.next = nodo
#
# def insert(list):
#     color = input("Informe a cord do cartao (A ou V): ").strip().upper()
#
#     if color == "V":
#         number = list.greenNumber
#         list.greenNumber += 1
#     elif color == "A":
#         number = list.yellowNumber
#         list.yellowNumber += 1
#     else:
#         print("Cor invalida!")
#         return
#
#     nodo = Card(color, number)
#
#     if list.head is None:
#         list.head = nodo
#     elif color == "V":
#         list.insertWithoutPriority(nodo)
#     elif color == "A":
#         list.insertWithPriority(nodo)
#     else:
#         print("Cor invalida!")
#
#     print(f"Paciente cadastrado com o cartao {color}{number}.")
#
# def printWaitList(list):
#     if list.head is None:
#         print("Nao ha pacientes na fila")
#         return
#     print("Fila de espera:")
#     nodo = list.head
#     while nodo is not None:
#         print(f"[{nodo.color}, {nodo.number}]", end=" ")
#         nodo = nodo.next
#     print()
#
# def attendPatient(list):
#     if list.head is None:
#         print("Nao ha pacientes na fila.")
#         return
#     nodo = list.head
#     list.head = list.head.next
#     print(f"Proximo paciente para atendimento: cartao {nodo.color}{nodo.number}")
#
# list = SinglyLinkedList()
#
# while True:
#     print("1 - Adicionar paciente a fila")
#     print("2 - Mostrar pacientes na fila")
#     print("3 - Chamar paciente")
#     print("4 - Sair")
#
#     op = input("Escolha uma opcao: ")
#
#     if op == "1":
#         insert(list)
#     elif op == "2":
#         printWaitList(list)
#     elif op == "3":
#         attendPatient(list)
#     elif op == "4":
#         print("Encerrando...")
#         break

## ATIVIDADE 2 - SISTEMA DE EMPLACAMENTO DE VEICULOS

class State:
    def __init__(self, stateAcronym, stateName):
        self.stateAcronym = stateAcronym
        self.stateName = stateName
        self.next = None

    def __repr__(self):
        return self.stateAcronym

class HashTable:
    def __init__(self):
        self.table = [None] * n

    def acronymHashFunc(self, k):
        if k == "DF":
            return 7
        return (ord(k[0]) + ord(k[1])) % n

    def identityState(self, stateAcronym):
        for acronym, name in statesList:
            if acronym == stateAcronym:
                return name
        print("Estado invalido")
        return None

    def insert(self, stateAcronym):
        stateName = self.identityState(stateAcronym)
        if stateName is None:
            return
        position = self.acronymHashFunc(stateAcronym)
        nodo = State(stateAcronym, stateName)
        nodo.next = self.table[position]
        self.table[position] = nodo
        print("Estado inserido na tabela hash")

statesList = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
    ("PF", "Pedro Feld")
]
n = 10
table = HashTable()

while True:
    print("1 - Inserir estado na tabela hash")
    print("2 - Imprimir tabela hash de estados")
    print("3 - Sair")

    op = input("Escolha uma opcao: ")

    if op == "1":
        acronym = input("Informe a sigla do estado: ")
        table.insert(acronym)
    elif op == "2":
        print("Imprimindo...")
    elif op == "3":
        print("Encerrando...")
        break