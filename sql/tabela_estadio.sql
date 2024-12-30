CREATE TABLE Estadio (
    id SERIAL PRIMARY KEY,
    data_fundacao DATE,
    nome VARCHAR(255),
    capacidade_pessoas INT,
    id_localizacao INT,
    CONSTRAINT fk_localizacao FOREIGN KEY (id_localizacao) REFERENCES Localizacao(id)
);