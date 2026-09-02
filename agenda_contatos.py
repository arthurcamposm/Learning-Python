class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class AgendaContatos:
    def __init__(self, lista_contatos=None):
        if lista_contatos is None:
            lista_contatos = []
        self.lista_contatos = lista_contatos

    def adicionar(self, contato):
        self.lista_contatos.append(contato)

    def buscar(self, nome):
        for contato in self.lista_contatos:
            if contato.nome == nome:
                return contato
        return None

    def remover(self, nome):
        for contato in self.lista_contatos:
            if contato.nome == nome:
                self.lista_contatos.remove(contato)
                return True        
        return False

    def listar_todos(self):
        for contato in self.lista_contatos:
            print(f"nome: {contato.nome}, telefone: {contato.telefone}, email: {contato.email}")

agenda = AgendaContatos()

josé = Contato("José", 123, "jose@gmail.com")
maria = Contato("Maria", 124, "maria@gmail.com")
joão = Contato("João", 125, "joao@gmail.com")
paulo = Contato("Paulo", 126, "paulo@gmail.com")

agenda.adicionar(josé)
agenda.adicionar(maria)
agenda.adicionar(joão)

contato_encontrado = agenda.buscar("José")
if contato_encontrado:
    print(f"nome: {contato_encontrado.nome}, telefone: {contato_encontrado.telefone}")
else:
    print("Contato não encontrado")

contato_encontrado = agenda.buscar("Paulo")
if contato_encontrado:
    print(f"nome: {contato_encontrado.nome}, telefone: {contato_encontrado.telefone}")
else:
    print("Contato não encontrado")

agenda.listar_todos()
agenda.remover("Maria")
agenda.listar_todos()

