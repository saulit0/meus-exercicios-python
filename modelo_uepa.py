class MembroUEPA:
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        print(f"Olá! Eu sou um membro da UEPA.")

class Aluno(MembroUEPA):
    def __init__(self, nome, matricula, email, curso):
        super().__init__(nome, matricula, email)
        self.curso = curso

    def apresentar(self):
        print(f"Olá! Eu sou o(a) aluno(a) {self.nome}, curso de {self.curso}. "
              f"Matrícula: {self.matricula}, Email: {self.email}.")

    def verificar_notas(self):
        print(f". {self.nome} está verificando suas notas no sistema.")
        
class Professor(MembroUEPA):
    def __init__(self, nome, matricula, email, departamento):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def apresentar(self):
        print(f"Olá! Eu sou o(a) professor(a) {self.nome}, departamento de {self.departamento}. "
              f"Matrícula: {self.matricula}, Email: {self.email}.")

    def lancar_frequencia(self):
        print(f". {self.nome} está lançando a frequência no sistema.")

if __name__ == "__main__":
    aluno1 = Aluno("Gabriel Saulo", "4722008", "gabriel.saulo@aluno.uepa.br", "Licenciatura em Teatro\n")
    aluno1.apresentar()
    aluno1.verificar_notas()
    
    print("-----------------------------------------------------------------------------")

    professor1 = Professor("Carla Lobo", "1874009", "carla.lobo@uepa.br", "Engenharia Naval\n")
    professor1.apresentar()
    professor1.lancar_frequencia()