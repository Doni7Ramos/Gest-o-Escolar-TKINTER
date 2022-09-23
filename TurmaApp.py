from tkinter import *

from tkinter.ttk import Treeview

from tkcalendar import DateEntry

from curso import Curso

from professor import Professor

from turma import Turma


class TurmaApp:

    width = 10

    anchor = W

    # Titulo padrão da interface
    titulo = 'Formulário de Turma'

    # Fonte padrão dos elementos da interface
    font = ('Verdana', 12)

    # LISTA FIXA DOS PERIODOS
    lista_periodo = ['Manhã', 'Tarde', 'Noite']

    def __init__(self, master=None):

        self.master = master

        self.master.title(TurmaApp.titulo)

        self.frame_master = Frame(self.master)

        self.frame_master.pack()

        self.frame_titulo = Frame(self.frame_master)

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=TurmaApp.titulo,
            font=( 'Verdana', 20,'bold' )
        )

        self.label_titulo.pack()

        self.frame_datas = Frame(self.frame_master)

        self.frame_datas.pack()

        # data de
        self.label_data_de = Label(
            self.frame_datas,
            text='Data Inicio:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_data_de.grid(
            row=0,
            column=0
        )

        self.entry_data_de = DateEntry(
            self.frame_datas,
            font=TurmaApp.font
        )

        self.entry_data_de.grid(
            row=0,
            column=1
        )

        # Data ate
        self.label_data_ate = Label(
            self.frame_datas,
            text='Data Fim:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_data_ate.grid(
            row=1,
            column=0
        )

        self.entry_data_ate = DateEntry(
            self.frame_datas,
            font=TurmaApp.font,
        )

        self.entry_data_ate.grid(
            row=1,
            column=1
        )

        # Lista de periodos
        self.frame_periodo = Frame(self.frame_master)

        self.frame_periodo.pack()

        self.label_data_de = Label(
            self.frame_periodo,
            text='Período:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_data_de.grid(
            row=0,
            column=0
        )

        self.lista_periodo = Listbox(self.frame_periodo)          

        for item in TurmaApp.lista_periodo:

            self.lista_periodo.insert(END, item)

        self.lista_periodo.grid(
            row=0,
            column=1
        )

        # Lista dos cursos a selecionar

        self.frame_curso = Frame(self.frame_master)

        self.frame_curso.pack()

        self.label_curso = Label(
            self.frame_curso,
            text='Curso:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_curso.grid(
            row=0,
            column=0
        )

        self.lista_curso = Treeview(
            self.frame_curso,
            selectmode="browse",
            column=(
                "codigo",
                "nome",
            ),
            show="headings",
        )

        self.lista_curso.column(
            "codigo",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_curso.heading(
            "#1",
            text="Código"
        )

        self.lista_curso.column(
            "nome",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_curso.heading(
            "#2",
            text="Nome"
        )
        self.listar_curso()

        self.lista_curso.grid(
            row=0,
            column=1
        )

        # Lista para selecionar professor 
        self.frame_professor = Frame(self.frame_master)

        self.frame_professor.pack()

        self.label_professor = Label(
            self.frame_professor,
            text='Professor:',
            font=TurmaApp.font,
            width=TurmaApp.width,
            anchor=TurmaApp.anchor
        )

        self.label_professor.grid(
            row=0,
            column=0
        )

        self.lista_professor = Treeview(
            self.frame_professor,
            selectmode="browse",
            column=(
                "matricula",
                "nome",
            ),
            show="headings",
        )

        self.lista_professor.column(
            "matricula",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_professor.heading(
            "#1",
            text="Código"
        )

        self.lista_professor.column(
            "nome",
            anchor=CENTER,
            width=100,
            minwidth=50,
            stretch=NO
        )

        self.lista_professor.heading(
            "#2",
            text="Nome"
        )

        self.listar_professor()

        self.lista_professor.grid(
            row=0,
            column=1
        )

        self.frame_ferramentas = Frame(self.frame_master)

        self.frame_ferramentas.pack()

        self.button = Button(
            self.frame_ferramentas, 
            text='Salvar Turma', 
            command=self.salvar)

        self.button.pack()

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=TurmaApp.font
        )

        self.label_mensagem.pack()

    def listar_curso(self):
       
        lista_cursos = Curso.listar()

        for curso in lista_cursos:
          
            self.lista_curso.insert(
                "",
                END,
                values=(
                    curso[0],
                    curso[1]
                )
            )

    def listar_professor(self):
        
        lista_professores = Professor.listar()

        for professor in lista_professores:

            self.lista_professor.insert(
                "",
                END,
                values=(
                    professor[0],
                    professor[1]
                )
            )

    def salvar(self):

        # pegando a data "convertendo a data para data de banco de dados"
        data_de = self.entry_data_de.get()

        data_de = f"{data_de[6:10]}-{data_de[3:5]}-{data_de[:2]}"

        data_ate = self.entry_data_ate.get()

        data_ate = f"{data_ate[6:10]}-{data_ate[3:5]}-{data_ate[:2]}"

        
        try:
            # Pegando o periodo na tabela
            periodo = self.lista_periodo.get(
                self.lista_periodo.curselection())
            # print(perido)

            # Pegando o Curso
            curItem = self.lista_curso.focus()

            curso = self.lista_curso.item(curItem)
            # Pegando o codigo do curso e setando em uma variavel
            codigo_curso = curso['values'][0]

            # print(codigo_curso)

            # Pegando o Professor
            curItem = self.lista_professor.focus()

            professor = self.lista_professor.item(curItem)
            # Pegando o codigo do professor e setando em uma variavel
            matricula_professor = professor['values'][0]

            # print(id_professor)
       
            try:
                turma = Turma(
                    periodo=periodo,
                    data_inicio=data_de,
                    data_fim=data_ate,
                    codigo_curso=codigo_curso,
                    matricula_professor=matricula_professor,
                )


                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Turma {turma.codigo} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err

        except:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Preencher todos os campos !'


if __name__ == '__main__':

    root = Tk()

    TurmaApp(root)

    root.mainloop()