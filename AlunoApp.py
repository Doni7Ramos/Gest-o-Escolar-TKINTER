from tkinter import *

from aluno import Aluno

# Wapper é uma classe e os componentes são atributos dela

class AlunoApp:
    """
        Classe empacotadora wapper para armazenar todo os componentes da interface de Alunos
    """
    # Titulo padrão da interface
    titulo = 'Formulário de Aluno'

    # Fonte padrão dos elementos da interface
    font = ('Verdana', 12)
    # Passando container princiapal

    def __init__(self, master=None):
        """
            Construtor do wapper
            Local para declararmos os componentes da interface
        """
        # Armazenei em um atributo o container principal
        self.master = master

        self.master.title(AlunoApp.titulo)

        # Criação do frame central para apresentar em 
        # tela os componentes, dentro do container principal
        # frame_master espaço vazio
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # Apresentar o titulo da interface
        # Segmentando as areas da interfca utiziando o container Frame
        # Frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=AlunoApp.titulo,
            font=('Verdana', 20, 'bold')
        )
        self.label_titulo.pack()

        # Formulário do aluno
        # Segmentando a area do formulario

        width = 10
        
        anchor = W

        self.frame_formulario = Frame(
            self.frame_master
        )

        self.frame_formulario.pack()

        # Nome
        self.label_nome = Label(
            self.frame_formulario,
            text='Nome:',
            font=AlunoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_nome.grid(
            row=1,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_nome.grid(
            row=1,
            column=1
        )

        # CPF
        self.label_cpf = Label(
            self.frame_formulario,
            text='CPF:',
            font=AlunoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_cpf.grid(
            row=2,
            column=0
        )

        self.entry_cpf = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_cpf.grid(
            row=2,
            column=1
        )

        # E-mail
        self.label_email = Label(
            self.frame_formulario,
            text='E-mail:',
            font=AlunoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_email.grid(
            row=3,
            column=0
        )

        self.entry_email = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_email.grid(
            row=3,
            column=1
        )

        # Telefone
        self.label_telefone = Label(
            self.frame_formulario,
            text='Telefone:',
            font=AlunoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_telefone.grid(
            row=4,
            column=0
        )

        self.entry_telefone = Entry(
            self.frame_formulario,
            font=AlunoApp.font,
        )

        self.entry_telefone.grid(
            row=4,
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
            font=AlunoApp.font,
            background='Light blue',
            foreground='black',
            command=self.salvar
        )

        self.button_salvar.pack(
            side=RIGHT
        )

        # Botão de fechar
        self.button_fechar = Button(
            self.frame_ferramentas,
            text='Fechar',
            font=AlunoApp.font,
            background='Black',
            foreground='White',
            command=self.master.quit
        )

        self.button_fechar.pack(side=LEFT)

        # Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=AlunoApp.font
        )

        self.label_mensagem.pack()

    def salvar(self):
        # Remove o valor do entry
        # self.entry_matricula.delete(0, END)

        nome = self.entry_nome.get()

        cpf = self.entry_cpf.get()

        email = self.entry_email.get()

        telefone = self.entry_telefone.get()

        if nome and cpf and email and telefone != "":
            try:
                aluno = Aluno(

                    nome = nome,
                    cpf = cpf,
                    email = email,
                    telefone = telefone
                )

                self.entry_nome.delete(0, END)
                self.entry_nome.focus()

                self.entry_cpf.delete(0, END)
                self.entry_email.delete(0, END)
                self.entry_telefone.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Aluno {aluno.matricula} - {aluno.nome} cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Dados incorretos !' 

# Tecnica de teste
if __name__ == '__main__':

    root = Tk()

    AlunoApp(root)

    root.mainloop()