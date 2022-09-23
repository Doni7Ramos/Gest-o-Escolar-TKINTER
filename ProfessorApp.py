from tkinter import *

from professor import Professor

# Wapper é uma classe, os componentes são atributos dela

class ProfessorApp:
    """
        Classe empacotadora wapper para armazenar todo os componentes da interface de Alunos
    """
    # Titulo padrão da interface
    titulo = 'Formulário de Professor'

    # Fonte padrão dos elementos da interface
    font = ('Verdana', 12)
    # Passando container princiapal

    def __init__(self, master=None):
        """
            construtor do wapper
            Local para declararmos os componentes da interface
        """
        # Armazenando em um atributo o container principal
        self.master = master

        self.master.title(ProfessorApp.titulo)

        # Criação do frame central para apresentar em 
        # tela os componentes, dentro do container principal
        # frame_master espaço vazio
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # Apresentando o titulo da interface
        # Segmentando as areas da interface utiziando o container frame
        # frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=ProfessorApp.titulo,
            font=('Verdana', 20, 'bold')
        )
        self.label_titulo.pack()

        # Formulário de aluno
        # Segmentando a area do formulario

        width = 12
        
        anchor = W

        self.frame_formulario = Frame(
            self.frame_master
        )

        self.frame_formulario.pack()

# Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome:',
            font=ProfessorApp.font,
            width=width,
            anchor = anchor
        )

        self.label_nome.grid(
            row=1,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_nome.grid(
            row=1,
            column=1
        )

# CPF
        self.label_cpf = Label(
            self.frame_formulario,
            text='CPF:',
            font=ProfessorApp.font,
            width=width,
            anchor = anchor
        )

        self.label_cpf.grid(
            row=2,
            column=0
        )

        self.entry_cpf = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_cpf.grid(
            row=2,
            column=1
        )

# Telefone
        self.label_telefone = Label(
            self.frame_formulario,
            text='Telefone:',
            font=ProfessorApp.font,
            width=width,
            anchor = anchor
        )

        self.label_telefone.grid(
            row=3,
            column=0
        )

        self.entry_telefone = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_telefone.grid(
            row=3,
            column=1
        )

# E-mail
        self.label_email = Label(
            self.frame_formulario,
            text='E-mail:',
            font=ProfessorApp.font,
            width=width,
            anchor = anchor
        )

        self.label_email.grid(
            row=4,
            column=0
        )

        self.entry_email = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_email.grid(
            row=4,
            column=1
        )

# Formacao
        self.label_formacao = Label(
            self.frame_formulario,
            text='Formação:',
            font=ProfessorApp.font,
            width=width,
            anchor = anchor
        )

        self.label_formacao.grid(
            row=5,
            column=0
        )

        self.entry_formacao = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_formacao.grid(
            row=5,
            column=1
        )

# Especialidade
        self.label_especialidade = Label(
            self.frame_formulario,
            text='Especialidade:',
            font=ProfessorApp.font,
            width=width,
            anchor = anchor
        )

        self.label_especialidade.grid(
            row=6,
            column=0
        )

        self.entry_especialidade = Entry(
            self.frame_formulario,
            font=ProfessorApp.font,
        )

        self.entry_especialidade.grid(
            row=6,
            column=1
        )
# Área de ferramentas
        self.frame_ferramentas = Frame(
            self.frame_master
        )

        self.frame_ferramentas.pack(
            fill=X
        )

# Botão de salvar
        self.button_salvar = Button(
            self.frame_ferramentas,
            text='Salvar',
            font=ProfessorApp.font,
            background='Light blue',
            foreground='Black',
            command=self.salvar
        )

        self.button_salvar.pack(
            side=RIGHT
        )
# Botão de fechar
        self.button_fechar = Button(
            self.frame_ferramentas,
            text='Fechar',
            font=ProfessorApp.font,
            background='Black',
            foreground='White',
            command=self.master.quit
        )

        self.button_fechar.pack(side=LEFT)

# Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=ProfessorApp.font
        )

        self.label_mensagem.pack()

    def salvar(self):
        # Remove o valor do entry
        # self.entry_matricula.delete(0, END)

        nome = self.entry_nome.get()

        cpf = self.entry_cpf.get()

        telefone = self.entry_telefone.get()

        email = self.entry_email.get()

        formacao = self.entry_formacao.get()

        especialidade = self.entry_especialidade.get()


        if nome and cpf != "":
            try:
                professor = Professor(

                    nome = nome,
                    cpf = cpf,
                    telefone = telefone,
                    email = email,
                    formacao = formacao,
                    especialidade = especialidade
                )

                self.entry_nome.delete(0, END)
                self.entry_nome.focus()

                self.entry_cpf.delete(0, END)
                self.entry_telefone.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_formacao.delete(0, END)
                self.entry_especialidade.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Professor {professor.matricula} - {professor.nome} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Dados incorretos !' 


if __name__ == '__main__':

    root = Tk()

    ProfessorApp(root)

    root.mainloop()