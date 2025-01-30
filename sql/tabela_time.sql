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

SELECT * FROM Time;

INSERT INTO Time (id, imagem_escudo, nome, apelido, data_fundacao, site_time_url, quantidade_socios, quantidade_jogadores_selecao, valor_mercado, id_estadio, id_localizacao) VALUES
(537, NULL, 'Botafogo de Futebol e Regatas', 'Botafogo', '1904-08-12', 'https://www.botafogo.com.br', 56.417, 4, 114000000, 1111, 2),
(3876, NULL, 'Mirassol Futebol Clube', 'Mirassol', '1925-11-09', 'https://www.mirassolfc.com.br', NULL, 0, 8000000, 16168, 14),
(2029, NULL, 'Ceará Sporting Club', 'Ceará', '1914-06-02', 'https://www.cearasc.com', 10.236, 0, 45000000, 2237, 10),
(10492, NULL, 'Esporte Clube Juventude', 'Juventude', '1913-06-29', 'https://www.juventude.com.br', 3.020, 1, 22000000, 1099, 13);