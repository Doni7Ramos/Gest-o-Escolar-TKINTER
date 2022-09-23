CREATE TABLE IF NOT EXISTS Turmas(

    codigo INTEGER PRIMARY KEY AUTOINCREMENT,

    periodo VARCHAR(255) NOT NULL,

    data_inicio DATE NOT NULL,

    data_fim DATE NOT NULL,

    codigo_curso INTEGER
        REFERENCES Cursos ( codigo ) NOT NULL,

    matricula_professor INTEGER
        REFERENCES Professores ( matricula ) NOT NULL

)