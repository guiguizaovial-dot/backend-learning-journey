-- CLIENTE
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

-- PRODUTO
CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    preco DECIMAL(10,2)
);

-- PEDIDO
CREATE TABLE pedido (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    data_pedido DATE,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

-- ITEM_PEDIDO (TABELA MAIS IMPORTANTE)
CREATE TABLE item_pedido (
    id_pedido INT,
    id_produto INT,
    quantidade INT,
    preco_unitario DECIMAL(10,2),

    FOREIGN KEY (id_pedido) REFERENCES pedido(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);

-- Inserindo Valores dentro das Tabelas
INSERT INTO cliente (nome, email) VALUES
('João', 'joao@gmail.com'),
('Maria', 'maria@gmail.com');

INSERT INTO produto (nome, preco) VALUES
('Notebook', 3000.00),
('Mouse', 50.00),
('Teclado', 150.00);

INSERT INTO pedido (id_cliente, data_pedido) VALUES
(1, '2025-03-01'),
(2, '2025-03-02');

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 1, 3000.00),
(1, 2, 2, 50.00),
(2, 3, 1, 150.00),
(2, 2, 1, 50.00);

--- Cliente + Pedido

SELECT c.nome, p.id AS pedido
FROM cliente c
INNER JOIN pedido p ON c.id = p.id_cliente;

--- Pedido + Produtos + Quantidade

SELECT p.id AS pedido, pr.nome AS produto, i.quantidade
FROM item_pedido i
INNER JOIN pedido p ON i.id_pedido = p.id
INNER JOIN produto pr ON i.id_produto = pr.id;

---- Valor total de cada pedido

SELECT id_pedido, SUM(quantidade * preco_unitario) AS total
FROM item_pedido
GROUP BY id_pedido;

---- Cliente que mais gastou

SELECT c.nome, SUM(i.quantidade * i.preco_unitario) AS total_gasto
FROM cliente c
INNER JOIN pedido p ON c.id = p.id_cliente
INNER JOIN item_pedido i ON p.id = i.id_pedido
GROUP BY c.nome
ORDER BY total_gasto DESC;

