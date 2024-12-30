CREATE TABLE Competicao (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    ano INT,
    confederacao VARCHAR(255),
    quantidade_times INT,
    quantidade_jogadores INT
);