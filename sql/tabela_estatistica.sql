CREATE TABLE Estatistica (
    id SERIAL PRIMARY KEY,
    quantidade_jogos_jogados INT,
    quantidade_gols_marcados INT,
    quantidade_assistencias_gols INT,
    id_jogador INT,
    CONSTRAINT fk_jogador FOREIGN KEY (id_jogador) REFERENCES Jogador(id)
);