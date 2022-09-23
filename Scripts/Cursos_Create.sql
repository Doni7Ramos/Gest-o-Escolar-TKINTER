CREATE TABLE Cursos (
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR (255) NOT NULL,
    classificacao VARCHAR (255) NOT NULL,
    ativo BOOLEAN,
    descricao VARCHAR (255)
)