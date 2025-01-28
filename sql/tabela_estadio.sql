CREATE TABLE Estadio (
    id INTEGER PRIMARY KEY,
    data_fundacao INT,
    nome VARCHAR(255),
    capacidade INT,
    id_localizacao INT,
    CONSTRAINT fk_localizacao FOREIGN KEY (id_localizacao) REFERENCES Localizacao(id)
);

INSERT INTO Estadio(id, data_fundacao, nome, capacidade, id_localizacao) VALUES (16168, 1983, 'Estádio Municipal José María de Campos Maia', 14534, 14);