CREATE OR REPLACE PROCEDURE transferir_jogador(
    p_jogador_id INT,
    p_novo_time_id INT
)
LANGUAGE plpgsql AS $$
DECLARE
    v_time_atual INT;
    v_nome_jogador VARCHAR;
    v_nome_time_novo VARCHAR;
BEGIN
    IF NOT EXISTS (SELECT 1 FROM Jogador WHERE id = p_jogador_id) THEN
        RAISE EXCEPTION 'Jogador com id % nao encontrado', p_jogador_id;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM Time WHERE id = p_novo_time_id) THEN
        RAISE EXCEPTION 'Time com id % nao encontrado', p_novo_time_id;
    END IF;

    SELECT id_time INTO v_time_atual FROM Jogador WHERE id = p_jogador_id;

    IF v_time_atual = p_novo_time_id THEN
        RAISE NOTICE 'Jogador ja pertence a este time. Nenhuma alteracao realizada.';
        RETURN;
    END IF;

    IF v_time_atual IS NULL THEN
        RAISE NOTICE 'Jogador sem time atual. Atribuindo diretamente.';
    END IF;

    UPDATE Jogador
    SET id_time = p_novo_time_id,
        contrato_incio = CURRENT_DATE
    WHERE id = p_jogador_id;

    SELECT p.nome INTO v_nome_jogador
    FROM Jogador j JOIN Pessoa p ON j.id_pessoa = p.id
    WHERE j.id = p_jogador_id;

    SELECT nome INTO v_nome_time_novo FROM Time WHERE id = p_novo_time_id;

    RAISE NOTICE 'Transferencia concluida: % -> %', v_nome_jogador, v_nome_time_novo;
END;
$$;

-- Exemplo de uso:
-- CALL transferir_jogador(1, 2);
