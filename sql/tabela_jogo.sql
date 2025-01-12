CREATE TABLE Jogo (
    id SERIAL PRIMARY KEY,
    data_jogo DATE,
    gols_time_casa INT,
    gols_time_visitante INT,
    id_estadio INT,
    id_arbitro INT,
    id_competicao INT,
    CONSTRAINT fk_estadio FOREIGN KEY (id_estadio) REFERENCES Estadio(id),
    CONSTRAINT fk_arbitro FOREIGN KEY (id_arbitro) REFERENCES Arbitro(id),
    CONSTRAINT fk_competicao FOREIGN KEY (id_competicao) REFERENCES Competicao(id)
);