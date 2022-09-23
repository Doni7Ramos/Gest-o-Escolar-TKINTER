from tkinter import *

from tkinter import ttk

from curso import Curso

class CursoAppLista:

    titulo = 'Lista de Cursos'

    font = ('Verdana', 12 )

    width = 10

    anchor = W

    def __init__ (self, master = None):
        
        self.master = master

        self.master.title(CursoAppLista.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_titulo = Frame (
            self.frame_master
        )

        self.frame_titulo.pack()

        self.frame_lista = Frame(self.frame_master)

        self.frame_lista.pack()

        self.label_titulo = Label(self.frame_titulo, 
        text = CursoAppLista.titulo,
        font = ('Verdana', 20, 'bold')
        )

        self.label_titulo.pack()
        self.lista = ttk.Treeview(self.frame_lista, selectmode = "browse", columns = (
            "codigo", "nome", "classificacao", "status", "descricao"), show = "headings")
        
        self.lista.column(
            "codigo",
            anchor = CENTER,
            width = 75,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#1",
            text = "Código"
        )

        self.lista.column(
            "nome",
            anchor = CENTER,
            width = 200,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#2",
            text = "Nome"
        )

        self.lista.column(
            "classificacao",
            anchor = CENTER,
            width = 200,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#3",
            text = "Classificação"
        )
        self.lista.column(
            "status",
            anchor = CENTER,
            width = 200,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#4",
            text = "Status"
        )

        self.lista.column(
            "descricao",
            anchor = CENTER,
            width = 250,
            minwidth = 50,
            stretch = NO
        )

        self.lista.heading(
            "#5",
            text = "Descrição"
        )

        self.lista.pack()

        self.listar()

    def listar (self):

        lista_cursos = Curso.listar()

        for curso in lista_cursos:

            curso_status = "Ativo" if curso[3] == 1 else "Inativo"
            # Fazendo o loop das linhas da tabela, com os dados vindos do banco de dados

            self.lista.insert(
                "",
                END,
                values = (
                    curso[0],
                    curso[1],
                    curso[2],
                    curso_status,
                    curso[4],

            )
        )



if __name__ == "__main__":

    root = Tk()

    CursoAppLista(root)

    root.mainloop()