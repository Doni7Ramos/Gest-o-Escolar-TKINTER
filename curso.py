import sqlite3

class Curso:

    def __init__ (self, nome, classificacao, descricao):

        self.nome = nome
        self.classificacao = classificacao
        self.descricao = descricao

        self.salvar()

    @property
    def codigo (self):

        return self.__codigo
    
    @classmethod
    def listar(cls):

        conexao = sqlite3.connect("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = """
            SELECT *
            FROM Cursos
        """
        cursor.execute(sql)

        lista_cursos = cursor.fetchall()

        conexao.close()

        return lista_cursos

        
    def salvar(self):

        conexao = sqlite3.connect ("gestao_escolar.db")

        cursor = conexao.cursor()

        sql = f"""
            INSERT INTO Cursos (
                nome,
                classificacao,
                descricao
            )
            VALUES
            (
                '{self.nome}',
                '{self.classificacao}',
                '{self.descricao}'
            )
            """

        cursor.execute(sql)

        self.__codigo = cursor.lastrowid

        conexao.commit()

        conexao.close()

    def __repr__ (self):

        return f"Codigo: {self.__codigo},Nome: {self.nome}, Classificação: {self.classificacao}, Descrição: {self.descricao}"

if __name__ == '__main__':

    print( Curso.listar() )