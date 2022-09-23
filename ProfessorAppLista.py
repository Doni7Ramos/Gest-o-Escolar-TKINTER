from tkinter import *

from tkinter import ttk

from professor import Professor

class ProfessorAppLista:

    titulo = 'Lista de Professores'

    font = ('Verdana', 12 )

    width = 10

    anchor = W


    def __init__ (self, master = None):

        self.master = master

        self.master.title(ProfessorAppLista.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_titulo = Frame (
            self.frame_master
        )

        self.frame_titulo.pack()

        self.frame_lista = Frame(self.frame_master)

        self.frame_lista.pack()

        self.label_titulo = Label(self.frame_titulo, 
        text = ProfessorAppLista.titulo,
        font = ('Verdana', 20, 'bold')
        )

        self.label_titulo.pack()

        self.lista = ttk.Treeview(self.frame_lista, selectmode = "browse", columns = (
            "matricula", "nome", "cpf", "status", "telefone", "email", "formacao", "especialidade"), show = "headings")

# Matricula
        self.lista.column(
            "matricula",
            anchor = CENTER,
            width = 100,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#1",
            text = "Matricula"
        )

# Nome
        self.lista.column(
            "nome",
            anchor = CENTER,
            width = 100,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#2",
            text = "Nome"
        )

# CPF
        self.lista.column(
            "cpf",
            anchor = CENTER,
            width = 100,
            minwidth = 50,
            stretch = NO
        )
        self.lista.heading(
            "#3",
            text = "CPF"
        )

# Status        
        self.lista.column(
            "status",
            anchor = CENTER,
            width = 100,
            minwidth = 50,
            stretch = NO
        )
        self.lista.heading(
            "#4",
            text = "Status"
        )

# Telefone        
        self.lista.column(
            "telefone",
            anchor = CENTER,
            width = 100,
            minwidth = 50,
            stretch = NO
        )
        self.lista.heading(
            "#5",
            text = "Telefone"
        )

# E-mail        
        self.lista.column(
            "email",
            anchor = CENTER,
            width = 150,
            minwidth = 50,
            stretch = NO
        )
        self.lista.heading(
            "#6",
            text = "E-mail"
        )

# Formação        
        self.lista.column(
            "formacao",
            anchor = CENTER,
            width = 150,
            minwidth = 50,
            stretch = NO
        )
        self.lista.heading(
            "#7",
            text = "Formação"
        )

# Especialidade        
        self.lista.column(
            "especialidade",
            anchor = CENTER,
            width = 100,
            minwidth = 50,
            stretch = NO
        )
        self.lista.heading(
            "#8",
            text = "Especialidade"
        )

        self.lista.pack()

        self.listar()

    def listar (self):

        lista_professores = Professor.listar()

        for professor in lista_professores:

            professor_status = "Ativo" if professor[3] == 1 else "Inativo"
            # Fazendo o loop das linhas da tabela, com os dados vindo do banco de dados

            self.lista.insert(
                "",
                END,
                values = (
                    professor[0],
                    professor[1],
                    professor[2],
                    professor_status,
                    professor[4],
                    professor[5],
                    professor[6],
                    professor[7]
                )
            )


if __name__ == '__main__':

    root = Tk()

    ProfessorAppLista(root)

    root.mainloop()