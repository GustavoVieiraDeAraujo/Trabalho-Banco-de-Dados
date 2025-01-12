CREATE TABLE Arbitro (
    id SERIAL PRIMARY KEY,
    contrato_inicio INT,
    id_pessoa INT,
    CONSTRAINT fk_pessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
);