CREATE OR REPLACE VIEW vw_jogadores_completo AS
SELECT
    p.nome              AS nome_jogador,
    p.apelido,
    p.nacionalidade,
    p.data_nascimento,
    j.posicao,
    j.altura,
    j.pe_dominante,
    j.valor_mercado,
    j.numero_camisa,
    j.contrato_incio    AS contrato_inicio,
    j.contrato_fim,
    t.nome              AS nome_time,
    l.cidade            AS cidade_time,
    l.pais              AS pais_time,
    e.quantidade_jogos_jogados,
    e.quantidade_gols_marcados,
    e.quantidade_assistencias_gols
FROM Jogador j
JOIN Pessoa p       ON j.id_pessoa = p.id
JOIN Time t         ON j.id_time = t.id
JOIN Localizacao l  ON t.id_localizacao = l.id
LEFT JOIN Estatistica e ON e.id_jogador = j.id;
