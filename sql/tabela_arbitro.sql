CREATE TABLE Arbitro (
    id SERIAL PRIMARY KEY,
    tempo_experiencia_meses INT,
    indice_confiabilidade DOUBLE PRECISION,
    id_pessoa INT,
    CONSTRAINT fk_pessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
);