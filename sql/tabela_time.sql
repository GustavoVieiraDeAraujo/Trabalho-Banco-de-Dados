CREATE TABLE Time (
    id SERIAL PRIMARY KEY,
    imagem_escudo BYTEA,
    nome VARCHAR(255) NOT NULL,
    apelido VARCHAR(255),
    data_fundacao DATE,
    cores VARCHAR(255),
    quantidade_jogadores INT,
    site_time_url VARCHAR(255),
    quantidade_socios INT,
    idade_media_jogadores INT,
    quantidade_jogadores_estrangeiros INT,
    quantidade_jogadores_selecao INT,
    id_estadio INT,
    CONSTRAINT fk_estadio FOREIGN KEY (id_estadio) REFERENCES Estadio(id)
);