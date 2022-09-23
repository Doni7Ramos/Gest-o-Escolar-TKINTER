from tkinter import *

from curso import Curso

# Wapper é uma classe, os componentes são atributos dela

class CursoApp:
    """
        Classe empacotadora wapper para armazenar todo os componentes da interface de Alunos
    """
    # Titulo padrão da interface
    titulo = 'Formulário de Curso'

    # Fonte padrão dos elementos da interface
    font = ('Verdana', 12)
    # Passando o container princiapal

    def __init__(self, master=None):
        """
            construtor do wapper
            Local para declararmos os componentes da interface
        """
        # Armazenando em um atributo o container principal
        self.master = master

        self.master.title(CursoApp.titulo)

        # Criação do frame central para apresentar em 
        # tela os componentes, dentro do container principal
        # frame_master espaço vazio
        self.frame_master = Frame(self.master)
        self.frame_master.pack()

        # Apresentando o titulo da interface
        # Segmentando as areas da interface utiziando o container Frame
        # Frame do titulo
        self.frame_titulo = Frame(
            self.frame_master
        )

        self.frame_titulo.pack()

        self.label_titulo = Label(
            self.frame_titulo,
            text=CursoApp.titulo,
            font=('Verdana', 20, 'bold')
        )
        self.label_titulo.pack()

        # Formulário do aluno
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
            font=CursoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_nome.grid(
            row=1,
            column=0
        )

        self.entry_nome = Entry(
            self.frame_formulario,
            font=CursoApp.font,
        )

        self.entry_nome.grid(
            row=1,
            column=1
        )

# Classificação
        self.label_classificacao = Label(
            self.frame_formulario,
            text='Classificação:',
            font=CursoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_classificacao.grid(
            row=2,
            column=0
        )

        self.entry_classificacao = Entry(
            self.frame_formulario,
            font=CursoApp.font,
        )

        self.entry_classificacao.grid(
            row=2,
            column=1
        )

# Descrição
        self.label_descricao = Label(
            self.frame_formulario,
            text='Descrição:',
            font=CursoApp.font,
            width=width,
            anchor = anchor
        )

        self.label_descricao.grid(
            row=3,
            column=0
        )

        self.entry_descricao = Entry(
            self.frame_formulario,
            font=CursoApp.font,
        )

        self.entry_descricao.grid(
            row=3,
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
            font=CursoApp.font,
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
            font=CursoApp.font,
            background='Black',
            foreground='White',
            command=self.master.quit
        )

        self.button_fechar.pack(side=LEFT)

# Mensagem
        self.label_mensagem = Label(
            self.frame_ferramentas,
            font=CursoApp.font
        )

        self.label_mensagem.pack()

    def salvar(self):
        # Removendo o valor do entry
        # self.entry_matricula.delete(0, END)

        nome = self.entry_nome.get()

        classificacao = self.entry_classificacao.get()

        descricao = self.entry_descricao.get()

        if nome and classificacao != "":
            try:
                cursos = Curso(

                    nome = nome,
                    classificacao = classificacao,
                    descricao = descricao
                )

                self.entry_nome.delete(0, END)
                self.entry_nome.focus()

                self.entry_classificacao.delete(0, END)
                self.entry_descricao.delete(0, END)

                self.label_mensagem['foreground'] = 'Green'
                self.label_mensagem['text'] = f"Curso de {cursos.nome} - Cadastrado !"

            except ValueError as err:
                self.label_mensagem['foreground'] = 'Red'
                self.label_mensagem['text'] = err
        else:
            self.label_mensagem['foreground'] = 'Red'
            self.label_mensagem['text'] = 'Dados incorretos !' 


if __name__ == '__main__':

    root = Tk()

    CursoApp(root)

    root.mainloop()