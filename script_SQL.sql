-- stg_hospital_a
-- stg_hospital_b
-- stg_hospital_c
-- stg_prontuario

-- PROBLEMA 1.

CREATE SCHEMA stg_prontuario;
GO

CREATE TABLE stg_prontuario.PACIENTE (
    id INTEGER NOT NULL,
    nome VARCHAR(60) NOT NULL,
    dt_nascimento DATE NOT NULL,
    cpf BIGINT NOT NULL,
    nome_mae VARCHAR(60) NOT NULL,
    dt_atualizacao TIMESTAMP NOT NULL,
    CONSTRAINT id_pkey PRIMARY KEY (id)
);

-- PROBLEMA 2.

INSERT INTO stg_prontuario.PACIENTE
SELECT *
FROM stg_hospital_a.PACIENTE;

INSERT INTO stg_prontuario.PACIENTE
SELECT *
FROM stg_hospital_b.PACIENTE;

INSERT INTO stg_prontuario.PACIENTE
SELECT *
FROM stg_hospital_c.PACIENTE;

-- PROBLEMA 3.

SELECT nome, cpf
FROM stg_prontuario.PACIENTE
GROUP BY nome, cpf
HAVING COUNT(*) > 1;

-- PROBLEMA 4.

SELECT p1.*
FROM (
    SELECT nome, cpf, MAX(dt_atualizacao) AS max_data_atualizacao
    FROM stg_prontuario.PACIENTE
    GROUP BY nome, cpf
    HAVING COUNT(*) > 1
) p1
INNER JOIN  
	stg_prontuario.PACIENTE p2 
ON p1.nome = p2.nome AND p1.cpf = p2.cpf AND p2.dt_atualizacao = p1.max_data_atualizacao;

-- PROBLEMA 5.

