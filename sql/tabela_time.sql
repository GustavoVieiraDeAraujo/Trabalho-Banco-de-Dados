CREATE TABLE Time (
  id INTEGER PRIMARY KEY,
  imagem_escudo BYTEA,
  nome VARCHAR(255) NOT NULL,
  apelido VARCHAR(255),
  data_fundacao DATE,
  site_time_url VARCHAR(255),
  quantidade_socios INT,
  quantidade_jogadores_selecao INT,
  valor_mercado MONEY,
  id_estadio INT,
  id_localizacao INT,
  CONSTRAINT fk_estadio FOREIGN KEY (id_estadio) REFERENCES Estadio(id),
  CONSTRAINT fk_localizacao FOREIGN KEY (id_localizacao) REFERENCES Localizacao(id)
);