import sqlite3

class Aluno:
    def __init__(self, nome, cpf, email, telefone=None):

        self.nome = nome

        self.cpf = cpf

        self.__matricula = 0
        # Somente a classe pode 'alterar' esse metodo
        # Self.incrementar_matricula()

        # Propriedade, parece um atributo, setter
        self.email = email

        self.telefone = telefone

        self.salvar()

    # Bloqueando o atributo, permitido somente a visualização
    # Metodo que virou um 'atributo'
    @property
    def matricula(self):

        return self.__matricula

    @property
    def email(self):

        return self.__email

    # Habilitando a alteração do email
    @email.setter
    def email(self, email):

        if '@' in email:
            
            self.__email = email
        else:
           
            raise ValueError('E-mail inválido.')

    # Adicionar aluno no banco de dados
    def salvar(self):
        # Habilitando a conexão com o banco de dados
        # Metodo poara abrir a conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # Utilizando o metodo cursor para fazer
        # alguma ação no banco de dados
        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Alunos (
                nome,
                cpf,
                telefone,
                email
            )
            VALUES (
                '{self.nome}',
                '{self.cpf}',
                '{self.telefone}',
                '{self.email}'
            )
        """
        # Executando a ação
        cursor.execute(sql)

        # Retornando a ultima id (Primary Key)
        self.__matricula = cursor.lastrowid

        # Salvando a alteração da tabela (confrima)
        conexao.commit()

        # Fechando a conexão com o banco de dados
        conexao.close()
        
    @classmethod
    def listar(cls):

        # Abrindo conexao
        conexao = sqlite3.connect("gestao_escolar.db")

        # Utilizando o metodo cursor para fazer
        # alguma ação no banco de dados
        cursor = conexao.cursor()

        sql = f"""
            SELECT * FROM Alunos
        """
        # Executando a ação
        cursor.execute(sql)

        # Lista de alunos recuperados do banco de dados
        listaAlunos = cursor.fetchall()

        # Fechando a conexão com o banco de dados
        conexao.close()

        return listaAlunos

    def __repr__(self):

        return f"Matricula: {self.matricula} Nome: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}"


if __name__ == '__main__':

    #joao = Aluno(nome='João', cpf=1, email='joao@')

    print(Aluno.listar())