CREATE TABLE Pessoa (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    apelido VARCHAR(255),
    data_nascimento DATE,
    idade INT,
    nacionalidade VARCHAR(255),
    tempo_contrato_meses INT,
    genero CHAR(1)
);