-- Criar as sequências antes das tabelas para evitar erros
CREATE SEQUENCE IF NOT EXISTS arbitro_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS competicao_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS estadio_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS estatistica_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS jogador_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS jogo_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS localizacao_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS tecnico_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS time_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS titulo_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS jogador_titulo_id_seq START WITH 1 INCREMENT BY 1;
CREATE SEQUENCE IF NOT EXISTS jogo_time_id_seq START WITH 1 INCREMENT BY 1;

-- Tabela: arbitro
CREATE TABLE IF NOT EXISTS public.arbitro (
    id INTEGER NOT NULL DEFAULT nextval('arbitro_id_seq'::regclass),
    nome VARCHAR(255),
    apelido VARCHAR(255),
    nacionalidade VARCHAR(255),
    imagem VARCHAR(255),
    contrato_inicio VARCHAR,
    data_nascimento VARCHAR,
    CONSTRAINT arbitro_pkey PRIMARY KEY (id)
);

-- Tabela: competicao
CREATE TABLE IF NOT EXISTS public.competicao (
    id INTEGER NOT NULL DEFAULT nextval('competicao_id_seq'::regclass),
    nome VARCHAR(255) NOT NULL,
    ano INTEGER,
    confederacao VARCHAR(255),
    quantidade_times VARCHAR(255) NOT NULL,
    CONSTRAINT competicao_pkey PRIMARY KEY (id)
);

-- Tabela: localizacao
CREATE TABLE IF NOT EXISTS public.localizacao (
    id INTEGER NOT NULL DEFAULT nextval('localizacao_id_seq'::regclass),
    pais VARCHAR(255),
    regiao VARCHAR(255),
    estado VARCHAR(255),
    cidade VARCHAR(255),
    CONSTRAINT localizacao_pkey PRIMARY KEY (id)
);

-- Tabela: estadio
CREATE TABLE IF NOT EXISTS public.estadio (
    id INTEGER NOT NULL DEFAULT nextval('estadio_id_seq'::regclass),
    nome VARCHAR(255),
    capacidade_pessoas INTEGER,
    id_localizacao INTEGER,
    data_fundacao VARCHAR(255),
    CONSTRAINT estadio_pkey PRIMARY KEY (id),
    CONSTRAINT fk_localizacao FOREIGN KEY (id_localizacao)
        REFERENCES public.localizacao (id) ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- Tabela: time
CREATE TABLE IF NOT EXISTS public."time" (
    id INTEGER NOT NULL DEFAULT nextval('time_id_seq'::regclass),
    imagem_escudo BYTEA,
    nome VARCHAR(255) NOT NULL,
    apelido VARCHAR(255),
    site_time_url VARCHAR(255),
    quantidade_socios INTEGER,
    quantidade_jogadores_selecao INTEGER,
    valor_mercado DOUBLE PRECISION,
    id_estadio INTEGER,
    id_localizacao INTEGER,
    data_fundacao VARCHAR(255),
    CONSTRAINT time_pkey PRIMARY KEY (id),
    CONSTRAINT fk_estadio FOREIGN KEY (id_estadio) REFERENCES public.estadio (id),
    CONSTRAINT fk_localizacao FOREIGN KEY (id_localizacao) REFERENCES public.localizacao (id)
);

-- Tabela: jogador
CREATE TABLE IF NOT EXISTS public.jogador (
    id INTEGER NOT NULL DEFAULT nextval('jogador_id_seq'::regclass),
    posicao VARCHAR(255),
    altura DOUBLE PRECISION,
    cidade_nascimento VARCHAR(255),
    numero_camisa INTEGER,
    agente VARCHAR(255),
    patrocinador VARCHAR(255),
    redes_sociais VARCHAR(255),
    id_time INTEGER,
    nome VARCHAR(255),
    apelido VARCHAR(255),
    nacionalidade VARCHAR(255),
    data_nascimento VARCHAR,
    data_fim_contrato VARCHAR NOT NULL,
    data_inicio_contrato VARCHAR NOT NULL,
    valor_mercado DOUBLE PRECISION,
    imagem VARCHAR,
    pe_dominante VARCHAR,
    CONSTRAINT jogador_pkey PRIMARY KEY (id),
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES public."time" (id)
);

-- Tabela: estatistica
CREATE TABLE IF NOT EXISTS public.estatistica (
    id INTEGER NOT NULL DEFAULT nextval('estatistica_id_seq'::regclass),
    quantidade_jogos_jogados INTEGER,
    quantidade_gols_marcados INTEGER,
    quantidade_assistencias_gols INTEGER,
    id_jogador INTEGER,
    CONSTRAINT estatistica_pkey PRIMARY KEY (id),
    CONSTRAINT fk_jogador FOREIGN KEY (id_jogador) REFERENCES public.jogador (id)
);

-- Tabela: tecnico
CREATE TABLE IF NOT EXISTS public.tecnico (
    id INTEGER NOT NULL DEFAULT nextval('tecnico_id_seq'::regclass),
    cidade_nascimento VARCHAR(255),
    id_time INTEGER,
    nome VARCHAR(255),
    apelido VARCHAR(255),
    nacionalidade VARCHAR(255),
    imagem VARCHAR(255),
    contrato_inicio VARCHAR,
    contrato_fim VARCHAR,
    data_nascimento VARCHAR,
    CONSTRAINT tecnico_pkey PRIMARY KEY (id),
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES public."time" (id)
);

-- Tabela: titulo
CREATE TABLE IF NOT EXISTS public.titulo (
    id INTEGER NOT NULL DEFAULT nextval('titulo_id_seq'::regclass),
    nome VARCHAR(255),
    CONSTRAINT titulo_pkey PRIMARY KEY (id)
);

-- Tabela: jogador_titulo
CREATE TABLE IF NOT EXISTS public.jogador_titulo (
    id INTEGER NOT NULL DEFAULT nextval('jogador_titulo_id_seq'::regclass),
    id_jogador INTEGER,
    id_titulo INTEGER,
    CONSTRAINT jogador_titulo_pkey PRIMARY KEY (id),
    CONSTRAINT fk_jogador FOREIGN KEY (id_jogador) REFERENCES public.jogador (id),
    CONSTRAINT fk_titulo FOREIGN KEY (id_titulo) REFERENCES public.titulo (id)
);

-- Tabela: jogo
CREATE TABLE IF NOT EXISTS public.jogo (
    id INTEGER NOT NULL DEFAULT nextval('jogo_id_seq'::regclass),
    gols_time_casa INTEGER,
    gols_time_visitante INTEGER,
    id_estadio INTEGER,
    id_arbitro INTEGER,
    id_competicao INTEGER,
    data_jogo VARCHAR(255),
    CONSTRAINT jogo_pkey PRIMARY KEY (id),
    CONSTRAINT fk_arbitro FOREIGN KEY (id_arbitro) REFERENCES public.arbitro (id),
    CONSTRAINT fk_competicao FOREIGN KEY (id_competicao) REFERENCES public.competicao (id),
    CONSTRAINT fk_estadio FOREIGN KEY (id_estadio) REFERENCES public.estadio (id)
);

-- Tabela: jogo_time
CREATE TABLE IF NOT EXISTS public.jogo_time (
    id INTEGER NOT NULL DEFAULT nextval('jogo_time_id_seq'::regclass),
    id_time INTEGER,
    id_jogo INTEGER,
    CONSTRAINT jogo_time_pkey PRIMARY KEY (id),
    CONSTRAINT fk_jogo FOREIGN KEY (id_jogo) REFERENCES public.jogo (id),
    CONSTRAINT fk_time FOREIGN KEY (id_time) REFERENCES public."time" (id)
);

-- Sincronizar as sequências com os IDs existentes (evita conflito de IDs)
SELECT setval('arbitro_id_seq', COALESCE((SELECT MAX(id) FROM public.arbitro), 1), false);
SELECT setval('competicao_id_seq', COALESCE((SELECT MAX(id) FROM public.competicao), 1), false);
SELECT setval('estadio_id_seq', COALESCE((SELECT MAX(id) FROM public.estadio), 1), false);
SELECT setval('estatistica_id_seq', COALESCE((SELECT MAX(id) FROM public.estatistica), 1), false);
SELECT setval('jogador_id_seq', COALESCE((SELECT MAX(id) FROM public.jogador), 1), false);
SELECT setval('jogo_id_seq', COALESCE((SELECT MAX(id) FROM public.jogo), 1), false);
SELECT setval('localizacao_id_seq', COALESCE((SELECT MAX(id) FROM public.localizacao), 1), false);
SELECT setval('tecnico_id_seq', COALESCE((SELECT MAX(id) FROM public.tecnico), 1), false);
SELECT setval('time_id_seq', COALESCE((SELECT MAX(id) FROM public."time"), 1), false);
SELECT setval('titulo_id_seq', COALESCE((SELECT MAX(id) FROM public.titulo), 1), false);
SELECT setval('jogador_titulo_id_seq', COALESCE((SELECT MAX(id) FROM public.jogador_titulo), 1), false);
SELECT setval('jogo_time_id_seq', COALESCE((SELECT MAX(id) FROM public.jogo_time), 1), false);