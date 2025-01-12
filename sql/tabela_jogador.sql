CREATE TABLE Jogador (
    id INTEGER PRIMARY KEY,
    posicao VARCHAR(255),
    altura DOUBLE PRECISION,
    pe_dominante VARCHAR(10) CHECK (pe_dominante IN ('Esquerda', 'Direita', 'Ambos')),
    valor_mercado MONEY,
    cidade_nascimento VARCHAR(255)
    numero_camisa INTEGER,
    agente VARCHAR(255)
    patrocinador VARCHAR(255),
    redes_sociais VARCHAR(255),
    contrato_incio DATE,
    contrato_fim DATE,
    id_time INT,
    id_pessoa INT,
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id),
    CONSTRAINT fk_pessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
);