CREATE TABLE Tecnico (
    id SERIAL PRIMARY KEY,
    contrato_inicio DATE,
    contrato_fim DATE,
    cidade_nascimento VARCHAR(255),
    id_time INT,
    id_pessoa INT,
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id),
    CONSTRAINT fk_pessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
);