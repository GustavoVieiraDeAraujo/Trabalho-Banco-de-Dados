CREATE TABLE Jogo_Time (
    id SERIAL PRIMARY KEY,
    id_time INT,
    id_jogo INT,
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES Time(id),
    CONSTRAINT fk_jogo FOREIGN KEY (id_jogo) REFERENCES Jogo(id)
);