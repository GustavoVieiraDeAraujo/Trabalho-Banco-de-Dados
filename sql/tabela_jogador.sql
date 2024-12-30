CREATE TABLE Jogador (
    id SERIAL PRIMARY KEY,
    posicao VARCHAR(255),
    altura DOUBLE PRECISION,
    peso DOUBLE PRECISION,
    pe_dominante VARCHAR(10) CHECK (pe_dominante IN ('Esquerda', 'Direita')),
    valor_mercado DOUBLE PRECISION,
    id_time INT,
    id_pessoa INT,
    id_estatistica INT,
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id),
    CONSTRAINT fk_pessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id),
    CONSTRAINT fk_estatistica FOREIGN KEY (id_estatistica) REFERENCES Estatistica(id)
);