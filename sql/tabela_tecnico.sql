CREATE TABLE Tecnico (
    id SERIAL PRIMARY KEY,
    data_entrou_time DATE,
    id_time INT,
    id_pessoa INT,
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id),
    CONSTRAINT fk_pessoa FOREIGN KEY (id_pessoa) REFERENCES Pessoa(id)
);