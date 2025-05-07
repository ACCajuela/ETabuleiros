
-- Copiando estrutura para tabela labbd2.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `cat_id` int NOT NULL AUTO_INCREMENT,
  `nome_categoria` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`cat_id`),
  UNIQUE KEY `nome_categoria` (`nome_categoria`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.categorias: ~0 rows (aproximadamente)
DELETE FROM `categorias`;
INSERT INTO `categorias` (`cat_id`, `nome_categoria`) VALUES
	(2, 'Cooperativo'),
	(1, 'Estratégia'),
	(4, 'Eurogame'),
	(8, 'Jogos de Aventura'),
	(16, 'Jogos de Azar'),
	(5, 'Jogos de Cartas'),
	(12, 'Jogos de Cartas Colecionáveis'),
	(9, 'Jogos de Construção'),
	(7, 'Jogos de Dedução'),
	(10, 'Jogos de Guerra'),
	(18, 'Jogos de Lógica'),
	(15, 'Jogos de Memória'),
	(6, 'Jogos de Miniaturas'),
	(17, 'Jogos de Palavras'),
	(14, 'Jogos de Quebra-Cabeça'),
	(13, 'Jogos de RPG'),
	(19, 'Jogos de Simulação'),
	(11, 'Jogos de Tabuleiro'),
	(20, 'Jogos de Terror'),
	(3, 'Party Game');

-- Copiando estrutura para tabela labbd2.cupons_desconto
CREATE TABLE IF NOT EXISTS `cupons_desconto` (
  `cupom_id` int NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `desconto` decimal(5,2) DEFAULT NULL,
  `data_expiracao` date DEFAULT NULL,
  PRIMARY KEY (`cupom_id`),
  UNIQUE KEY `codigo` (`codigo`),
  CONSTRAINT `cupons_desconto_chk_1` CHECK (((`desconto` > 0) and (`desconto` <= 100)))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.cupons_desconto: ~0 rows (aproximadamente)
DELETE FROM `cupons_desconto`;
INSERT INTO `cupons_desconto` (`cupom_id`, `codigo`, `desconto`, `data_expiracao`) VALUES
	(1, 'DESC10', 10.00, '2023-12-31'),
	(2, 'DESC20', 20.00, '2023-12-31'),
	(3, 'DESC30', 30.00, '2023-12-31'),
	(4, 'DESC40', 40.00, '2023-12-31'),
	(5, 'DESC50', 50.00, '2023-12-31'),
	(6, 'DESC60', 60.00, '2023-12-31'),
	(7, 'DESC70', 70.00, '2023-12-31'),
	(8, 'DESC80', 80.00, '2023-12-31'),
	(9, 'DESC90', 90.00, '2023-12-31'),
	(10, 'DESC100', 100.00, '2023-12-31'),
	(11, 'DESC15', 15.00, '2023-12-31'),
	(12, 'DESC25', 25.00, '2023-12-31');

-- Copiando estrutura para tabela labbd2.devolucoes
CREATE TABLE IF NOT EXISTS `devolucoes` (
  `devolucao_id` int NOT NULL AUTO_INCREMENT,
  `ped_id` int NOT NULL,
  `prod_id` int NOT NULL,
  `motivo` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status_devolucao` enum('pendente','aprovada','recusada') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'pendente',
  `data_solicitacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`devolucao_id`),
  KEY `ped_id` (`ped_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `devolucoes_ibfk_1` FOREIGN KEY (`ped_id`) REFERENCES `pedidos` (`ped_id`),
  CONSTRAINT `devolucoes_ibfk_2` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.devolucoes: ~0 rows (aproximadamente)
DELETE FROM `devolucoes`;
INSERT INTO `devolucoes` (`devolucao_id`, `ped_id`, `prod_id`, `motivo`, `status_devolucao`, `data_solicitacao`) VALUES
	(1, 1, 1, 'Faltam peças no jogo.', 'pendente', '2025-03-12 23:55:33'),
	(2, 2, 2, 'Tabuleiro danificado.', 'pendente', '2025-03-12 23:55:33'),
	(3, 3, 3, 'Cartas rasgadas.', 'pendente', '2025-03-12 23:55:33'),
	(4, 4, 4, 'Peças de trem faltando.', 'pendente', '2025-03-12 23:55:33'),
	(5, 5, 5, 'Cartas de maravilha danificadas.', 'pendente', '2025-03-12 23:55:33'),
	(6, 6, 6, 'Cartas de votação faltando.', 'pendente', '2025-03-12 23:55:33'),
	(7, 7, 7, 'Fichas de gemas danificadas.', 'pendente', '2025-03-12 23:55:33'),
	(8, 8, 8, 'Azulejos quebrados.', 'pendente', '2025-03-12 23:55:33'),
	(9, 9, 9, 'Cartas de palavras faltando.', 'pendente', '2025-03-12 23:55:33'),
	(10, 10, 10, 'Cartas de pássaros danificadas.', 'pendente', '2025-03-12 23:55:33'),
	(11, 11, 11, 'Miniaturas quebradas.', 'pendente', '2025-03-12 23:55:33'),
	(12, 12, 12, 'Cartas danificadas.', 'pendente', '2025-03-12 23:55:33'),
	(13, 13, 13, 'Tabuleiro riscado.', 'pendente', '2025-03-12 23:55:33'),
	(14, 14, 14, 'Esferas de energia faltando.', 'pendente', '2025-03-12 23:55:33'),
	(15, 15, 15, 'Miniaturas faltando.', 'pendente', '2025-03-12 23:55:33'),
	(16, 16, 16, 'Cartas danificadas.', 'pendente', '2025-03-12 23:55:33'),
	(17, 17, 17, 'Cartas de pássaros faltando.', 'pendente', '2025-03-12 23:55:33'),
	(18, 18, 18, 'Peças de madeira faltando.', 'pendente', '2025-03-12 23:55:33'),
	(19, 19, 19, 'Adesivos faltando.', 'pendente', '2025-03-12 23:55:33'),
	(20, 20, 20, 'Cartas de imagens danificadas.', 'pendente', '2025-03-12 23:55:33');

-- Copiando estrutura para tabela labbd2.duvidas
CREATE TABLE IF NOT EXISTS `duvidas` (
  `duvida_id` int NOT NULL AUTO_INCREMENT,
  `duvida_user_id` int DEFAULT NULL,
  `duvida_resposta_id` int DEFAULT NULL,
  `duvida` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `resposta` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `duvida_prod_id` int DEFAULT NULL,
  PRIMARY KEY (`duvida_id`),
  KEY `duvida_resposta_id` (`duvida_resposta_id`),
  KEY `duvida_user_id` (`duvida_user_id`),
  KEY `FK_duvidas_produtos` (`duvida_prod_id`),
  CONSTRAINT `duvidas_ibfk_1` FOREIGN KEY (`duvida_resposta_id`) REFERENCES `usuarios` (`user_id`),
  CONSTRAINT `duvidas_ibfk_2` FOREIGN KEY (`duvida_user_id`) REFERENCES `usuarios` (`user_id`),
  CONSTRAINT `FK_duvidas_produtos` FOREIGN KEY (`duvida_prod_id`) REFERENCES `produtos` (`prod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.duvidas: ~20 rows (aproximadamente)
DELETE FROM `duvidas`;
INSERT INTO `duvidas` (`duvida_id`, `duvida_user_id`, `duvida_resposta_id`, `duvida`, `resposta`, `duvida_prod_id`) VALUES
	(21, 1, 2, 'Como faço para trocar um produto?', 'Entre em contato com o suporte.', 1),
	(22, 2, 3, 'Posso parcelar no boleto?', 'Sim, em até 12x.', 2),
	(23, 3, 1, 'Qual o prazo de entrega?', 'O prazo varia de 3 a 7 dias úteis.', 3),
	(24, 4, 2, 'Como cancelar um pedido?', 'Entre em contato com o suporte.', 4),
	(25, 5, 3, 'Posso comprar no site e retirar na loja?', 'Sim, escolha a opção de retirada na loja.', 5),
	(26, 6, 1, 'Como faço para alterar meu endereço?', 'Acesse a área do cliente.', 6),
	(27, 7, 2, 'Qual o horário de atendimento?', 'Das 9h às 18h, de segunda a sexta.', 7),
	(28, 8, 3, 'Como faço para entrar em contato?', 'Através do formulário de contato.', 8),
	(29, 9, 1, 'Posso devolver um produto após 7 dias?', 'Sim, entre em contato com o suporte.', 9),
	(30, 10, 2, 'Como faço para rastrear meu pedido?', 'Acesse a área do cliente para rastrear seu pedido.', 10),
	(31, 11, 3, 'Posso trocar o produto?', 'Sim, dentro do prazo de 7 dias.', 11),
	(32, 12, 1, 'Como devolver um produto?', 'Siga as instruções na política de devolução.', 12),
	(33, 13, 2, 'Posso parcelar no boleto?', 'Sim, em até 12x.', 9),
	(34, 12, 3, 'Como faço para alterar meu endereço?', 'Acesse a área do cliente.', 9),
	(35, 11, 1, 'Qual o horário de atendimento?', 'Das 9h às 18h, de segunda a sexta.', 4),
	(36, 10, 2, 'Como faço para entrar em contato?', 'Através do formulário de contato.', 12),
	(37, 9, 3, 'Posso comprar no site e retirar na loja?', 'Sim, escolha a opção de retirada na loja.', 3),
	(38, 8, 1, 'Como faço para trocar um produto?', 'Entre em contato com o suporte.', 1),
	(39, 7, 2, 'Posso parcelar no boleto?', 'Sim, em até 12x.', 9),
	(40, 6, 3, 'Qual o prazo de entrega?', 'O prazo varia de 3 a 7 dias úteis.', 1);

-- Copiando estrutura para tabela labbd2.editoras
CREATE TABLE IF NOT EXISTS `editoras` (
  `editora_id` int NOT NULL AUTO_INCREMENT,
  `nome_editora` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`editora_id`),
  UNIQUE KEY `nome_editora` (`nome_editora`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.editoras: ~0 rows (aproximadamente)
DELETE FROM `editoras`;
INSERT INTO `editoras` (`editora_id`, `nome_editora`) VALUES
	(7, 'Buró Jogos'),
	(6, 'Conclave Editora'),
	(2, 'Devir'),
	(11, 'Editora G'),
	(12, 'Editora H'),
	(13, 'Editora I'),
	(14, 'Editora J'),
	(15, 'Editora K'),
	(16, 'Editora L'),
	(17, 'Editora M'),
	(18, 'Editora N'),
	(19, 'Editora O'),
	(20, 'Editora P'),
	(8, 'FunBox'),
	(1, 'Galápagos Jogos'),
	(3, 'Grow Jogos'),
	(4, 'Ludopedia'),
	(5, 'Maldito Games'),
	(10, 'Meeple BR'),
	(9, 'Pixie Games');

-- Copiando estrutura para tabela labbd2.enderecos_entrega
CREATE TABLE IF NOT EXISTS `enderecos_entrega` (
  `endereco_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `endereco` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `cep` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cidade` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `estado` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`endereco_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `enderecos_entrega_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.enderecos_entrega: ~0 rows (aproximadamente)
DELETE FROM `enderecos_entrega`;
INSERT INTO `enderecos_entrega` (`endereco_id`, `user_id`, `endereco`, `cep`, `cidade`, `estado`) VALUES
	(1, 1, 'Rua A, 123', '12345-678', 'São Paulo', 'SP'),
	(2, 2, 'Rua B, 456', '12345-678', 'São Paulo', 'SP'),
	(3, 3, 'Rua C, 789', '12345-678', 'São Paulo', 'SP'),
	(4, 4, 'Rua D, 789', '12345-678', 'São Paulo', 'SP'),
	(5, 5, 'Rua E, 101', '12345-678', 'São Paulo', 'SP'),
	(6, 6, 'Rua F, 202', '12345-678', 'São Paulo', 'SP'),
	(7, 7, 'Rua G, 303', '12345-678', 'São Paulo', 'SP'),
	(8, 8, 'Rua H, 404', '12345-678', 'São Paulo', 'SP'),
	(9, 9, 'Rua I, 505', '12345-678', 'São Paulo', 'SP'),
	(10, 10, 'Rua J, 606', '12345-678', 'São Paulo', 'SP'),
	(11, 11, 'Rua K, 707', '12345-678', 'São Paulo', 'SP'),
	(12, 12, 'Rua L, 808', '12345-678', 'São Paulo', 'SP'),
	(13, 13, 'Rua M, 909', '12345-678', 'São Paulo', 'SP');

-- Copiando estrutura para tabela labbd2.fornecedores
CREATE TABLE IF NOT EXISTS `fornecedores` (
  `fornecedor_id` int NOT NULL AUTO_INCREMENT,
  `nome_fornecedor` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `endereco` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`fornecedor_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.fornecedores: ~12 rows (aproximadamente)
DELETE FROM `fornecedores`;
INSERT INTO `fornecedores` (`fornecedor_id`, `nome_fornecedor`, `endereco`, `telefone`, `email`) VALUES
	(1, 'Fornecedor A', 'Rua X, 123', '(11) 11111-1111', 'fornecedorA@example.com'),
	(2, 'Fornecedor B', 'Rua Y, 456', '(11) 22222-2222', 'fornecedorB@example.com'),
	(3, 'Fornecedor C', 'Rua Z, 789', '(11) 33333-3333', 'fornecedorC@example.com'),
	(4, 'Fornecedor D', 'Rua W, 101', '(11) 44444-4444', 'fornecedorD@example.com'),
	(5, 'Fornecedor E', 'Rua V, 202', '(11) 55555-5555', 'fornecedorE@example.com'),
	(6, 'Fornecedor F', 'Rua U, 303', '(11) 66666-6666', 'fornecedorF@example.com'),
	(7, 'Fornecedor G', 'Rua T, 404', '(11) 77777-7777', 'fornecedorG@example.com'),
	(8, 'Fornecedor H', 'Rua S, 505', '(11) 88888-8888', 'fornecedorH@example.com'),
	(9, 'Fornecedor I', 'Rua R, 606', '(11) 99999-9999', 'fornecedorI@example.com'),
	(10, 'Fornecedor J', 'Rua Q, 707', '(11) 00000-0000', 'fornecedorJ@example.com'),
	(11, 'Fornecedor K', 'Rua P, 808', '(11) 11111-1111', 'fornecedorK@example.com'),
	(12, 'Fornecedor L', 'Rua O, 909', '(11) 22222-2222', 'fornecedorL@example.com');

-- Copiando estrutura para tabela labbd2.fretes
CREATE TABLE IF NOT EXISTS `fretes` (
  `frete_id` int NOT NULL AUTO_INCREMENT,
  `cep_destino` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `peso` decimal(10,2) NOT NULL,
  `valor_frete` decimal(10,2) NOT NULL,
  PRIMARY KEY (`frete_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.fretes: ~0 rows (aproximadamente)
DELETE FROM `fretes`;
INSERT INTO `fretes` (`frete_id`, `cep_destino`, `peso`, `valor_frete`) VALUES
	(1, '12345-678', 2.50, 15.00),
	(2, '12345-678', 3.00, 20.00),
	(3, '12345-678', 4.00, 25.00),
	(4, '12345-678', 5.00, 30.00),
	(5, '12345-678', 6.00, 35.00),
	(6, '12345-678', 7.00, 40.00),
	(7, '12345-678', 8.00, 45.00),
	(8, '12345-678', 9.00, 50.00),
	(9, '12345-678', 10.00, 55.00),
	(10, '12345-678', 11.00, 60.00),
	(11, '12345-678', 12.00, 65.00),
	(12, '12345-678', 13.00, 70.00),
	(13, '12345-678', 14.00, 75.00),
	(14, '12345-678', 15.00, 80.00),
	(15, '12345-678', 16.00, 85.00),
	(16, '12345-678', 17.00, 90.00),
	(17, '12345-678', 18.00, 95.00),
	(18, '12345-678', 19.00, 100.00),
	(19, '12345-678', 20.00, 105.00),
	(20, '12345-678', 21.00, 110.00);

-- Copiando estrutura para tabela labbd2.funcionarios_permissoes
CREATE TABLE IF NOT EXISTS `funcionarios_permissoes` (
  `func_perm_id` int NOT NULL AUTO_INCREMENT,
  `func_id` int NOT NULL,
  `permissao_id` int NOT NULL,
  PRIMARY KEY (`func_perm_id`),
  KEY `permissao_id` (`permissao_id`),
  KEY `FK_funcionarios_permissoes_usuarios` (`func_id`),
  CONSTRAINT `FK_funcionarios_permissoes_usuarios` FOREIGN KEY (`func_id`) REFERENCES `usuarios` (`user_id`),
  CONSTRAINT `funcionarios_permissoes_ibfk_2` FOREIGN KEY (`permissao_id`) REFERENCES `permissoes_funcionarios` (`perm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.funcionarios_permissoes: ~0 rows (aproximadamente)
DELETE FROM `funcionarios_permissoes`;
INSERT INTO `funcionarios_permissoes` (`func_perm_id`, `func_id`, `permissao_id`) VALUES
	(1, 2, 1),
	(2, 2, 2),
	(3, 2, 3),
	(4, 2, 4),
	(5, 2, 5),
	(6, 2, 6),
	(7, 2, 7),
	(8, 2, 8),
	(9, 2, 9),
	(10, 2, 10),
	(11, 2, 11),
	(12, 2, 12),
	(13, 2, 13),
	(14, 2, 14),
	(15, 2, 15),
	(16, 2, 16),
	(17, 2, 17),
	(18, 2, 18),
	(19, 2, 19),
	(20, 2, 20);

-- Copiando estrutura para tabela labbd2.historico_navegacao
CREATE TABLE IF NOT EXISTS `historico_navegacao` (
  `id_hist` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `prod_id` int NOT NULL,
  `data_visualizacao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_hist`),
  KEY `user_id` (`user_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `historico_navegacao_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`user_id`),
  CONSTRAINT `historico_navegacao_ibfk_2` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.historico_navegacao: ~0 rows (aproximadamente)
DELETE FROM `historico_navegacao`;
INSERT INTO `historico_navegacao` (`id_hist`, `user_id`, `prod_id`, `data_visualizacao`) VALUES
	(1, 1, 1, '2025-03-12 23:57:46'),
	(2, 2, 2, '2025-03-12 23:57:46'),
	(3, 3, 3, '2025-03-12 23:57:46'),
	(4, 4, 4, '2025-03-12 23:57:46'),
	(5, 5, 5, '2025-03-12 23:57:46'),
	(6, 6, 6, '2025-03-12 23:57:46'),
	(7, 7, 7, '2025-03-12 23:57:46'),
	(8, 8, 8, '2025-03-12 23:57:46'),
	(9, 9, 9, '2025-03-12 23:57:46'),
	(10, 10, 10, '2025-03-12 23:57:46'),
	(11, 11, 11, '2025-03-12 23:57:46'),
	(12, 12, 12, '2025-03-12 23:57:46'),
	(13, 13, 13, '2025-03-12 23:57:46'),
	(14, 12, 14, '2025-03-12 23:57:46'),
	(15, 11, 15, '2025-03-12 23:57:46'),
	(16, 10, 16, '2025-03-12 23:57:46'),
	(17, 9, 17, '2025-03-12 23:57:46'),
	(18, 8, 18, '2025-03-12 23:57:46'),
	(19, 7, 19, '2025-03-12 23:57:46'),
	(20, 6, 20, '2025-03-12 23:57:46');

-- Copiando estrutura para tabela labbd2.historico_pagamentos
CREATE TABLE IF NOT EXISTS `historico_pagamentos` (
  `pagamento_id` int NOT NULL AUTO_INCREMENT,
  `ped_id` int NOT NULL,
  `valor_pago` decimal(10,2) DEFAULT NULL,
  `metodo_pagamento` enum('credito','debito','pix') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `data_pagamento` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`pagamento_id`),
  KEY `ped_id` (`ped_id`),
  CONSTRAINT `historico_pagamentos_ibfk_1` FOREIGN KEY (`ped_id`) REFERENCES `pedidos` (`ped_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.historico_pagamentos: ~0 rows (aproximadamente)
DELETE FROM `historico_pagamentos`;
INSERT INTO `historico_pagamentos` (`pagamento_id`, `ped_id`, `valor_pago`, `metodo_pagamento`, `data_pagamento`) VALUES
	(1, 1, 199.99, 'credito', '2025-03-12 23:57:46'),
	(2, 2, 149.99, 'debito', '2025-03-12 23:57:46'),
	(3, 3, 179.99, 'pix', '2025-03-12 23:57:46'),
	(4, 4, 169.99, 'credito', '2025-03-12 23:57:46'),
	(5, 5, 189.99, 'debito', '2025-03-12 23:57:46'),
	(6, 6, 129.99, 'pix', '2025-03-12 23:57:46'),
	(7, 7, 159.99, 'credito', '2025-03-12 23:57:46'),
	(8, 8, 139.99, 'debito', '2025-03-12 23:57:46'),
	(9, 9, 99.99, 'pix', '2025-03-12 23:57:46'),
	(10, 10, 249.99, 'credito', '2025-03-12 23:57:46'),
	(11, 11, 499.99, 'debito', '2025-03-12 23:57:46'),
	(12, 12, 299.99, 'pix', '2025-03-12 23:57:46'),
	(13, 13, 349.99, 'credito', '2025-03-12 23:57:46'),
	(14, 12, 129.99, 'debito', '2025-03-12 23:57:46'),
	(15, 11, 199.99, 'pix', '2025-03-12 23:57:46'),
	(16, 10, 249.99, 'credito', '2025-03-12 23:57:46'),
	(17, 9, 149.99, 'debito', '2025-03-12 23:57:46'),
	(18, 8, 99.99, 'pix', '2025-03-12 23:57:46'),
	(19, 7, 399.99, 'credito', '2025-03-12 23:57:46'),
	(20, 6, 89.99, 'debito', '2025-03-12 23:57:46');

-- Copiando estrutura para tabela labbd2.historico_precos
CREATE TABLE IF NOT EXISTS `historico_precos` (
  `historico_preco_id` int NOT NULL AUTO_INCREMENT,
  `prod_id` int NOT NULL,
  `preco_antigo` decimal(10,2) DEFAULT NULL,
  `preco_novo` decimal(10,2) DEFAULT NULL,
  `data_alteracao` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`historico_preco_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `historico_precos_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.historico_precos: ~0 rows (aproximadamente)
DELETE FROM `historico_precos`;
INSERT INTO `historico_precos` (`historico_preco_id`, `prod_id`, `preco_antigo`, `preco_novo`, `data_alteracao`) VALUES
	(1, 1, 199.99, 189.99, '2025-03-12 23:57:46'),
	(2, 2, 149.99, 139.99, '2025-03-12 23:57:46'),
	(3, 3, 179.99, 169.99, '2025-03-12 23:57:46'),
	(4, 4, 169.99, 159.99, '2025-03-12 23:57:46'),
	(5, 5, 189.99, 179.99, '2025-03-12 23:57:46'),
	(6, 6, 129.99, 119.99, '2025-03-12 23:57:46'),
	(7, 7, 159.99, 149.99, '2025-03-12 23:57:46'),
	(8, 8, 139.99, 129.99, '2025-03-12 23:57:46'),
	(9, 9, 99.99, 89.99, '2025-03-12 23:57:46'),
	(10, 10, 249.99, 239.99, '2025-03-12 23:57:46'),
	(11, 11, 499.99, 489.99, '2025-03-12 23:57:46'),
	(12, 12, 299.99, 289.99, '2025-03-12 23:57:46'),
	(13, 13, 349.99, 339.99, '2025-03-12 23:57:46'),
	(14, 14, 129.99, 119.99, '2025-03-12 23:57:46'),
	(15, 15, 199.99, 189.99, '2025-03-12 23:57:46'),
	(16, 16, 249.99, 239.99, '2025-03-12 23:57:46'),
	(17, 17, 149.99, 139.99, '2025-03-12 23:57:46'),
	(18, 18, 99.99, 89.99, '2025-03-12 23:57:46'),
	(19, 19, 399.99, 389.99, '2025-03-12 23:57:46'),
	(20, 20, 89.99, 79.99, '2025-03-12 23:57:46');

-- Copiando estrutura para tabela labbd2.imagens_produtos
CREATE TABLE IF NOT EXISTS `imagens_produtos` (
  `imagem_id` int NOT NULL AUTO_INCREMENT,
  `prod_id` int NOT NULL,
  `caminho_imagem` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `ordem` int DEFAULT '1',
  PRIMARY KEY (`imagem_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `imagens_produtos_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.imagens_produtos: ~0 rows (aproximadamente)
DELETE FROM `imagens_produtos`;
INSERT INTO `imagens_produtos` (`imagem_id`, `prod_id`, `caminho_imagem`, `ordem`) VALUES
	(1, 1, 'imagens/catan.jpg', 1),
	(2, 2, 'imagens/carcassonne.jpg', 1),
	(3, 3, 'imagens/pandemic.jpg', 1),
	(4, 4, 'imagens/ticket_to_ride.jpg', 1),
	(5, 5, 'imagens/7_wonders.jpg', 1),
	(6, 6, 'imagens/dixit.jpg', 1),
	(7, 7, 'imagens/splendor.jpg', 1),
	(8, 8, 'imagens/azul.jpg', 1),
	(9, 9, 'imagens/codenames.jpg', 1),
	(10, 10, 'imagens/wingspan.jpg', 1),
	(11, 11, 'imagens/gloomhaven.jpg', 1),
	(12, 12, 'imagens/terraforming_mars.jpg', 1),
	(13, 13, 'imagens/scythe.jpg', 1),
	(14, 14, 'imagens/gizmos.jpg', 1),
	(15, 15, 'imagens/root.jpg', 1),
	(16, 16, 'imagens/everdell.jpg', 1),
	(17, 17, 'imagens/wingspan_oceania.jpg', 1),
	(18, 18, 'imagens/catan_extensao.jpg', 1),
	(19, 19, 'imagens/pandemic_legado.jpg', 1),
	(20, 20, 'imagens/codenames_pictures.jpg', 1);

-- Copiando estrutura para tabela labbd2.lista_desejos
CREATE TABLE IF NOT EXISTS `lista_desejos` (
  `id_des` int NOT NULL AUTO_INCREMENT,
  `id_des_user` int NOT NULL,
  `data_alteracao_LD` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `id_des_prod` int DEFAULT NULL,
  PRIMARY KEY (`id_des`),
  KEY `id_des_user` (`id_des_user`),
  KEY `FK_lista_desejos_produtos` (`id_des_prod`),
  CONSTRAINT `FK_lista_desejos_produtos` FOREIGN KEY (`id_des_prod`) REFERENCES `produtos` (`prod_id`),
  CONSTRAINT `lista_desejos_ibfk_1` FOREIGN KEY (`id_des_user`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.lista_desejos: ~0 rows (aproximadamente)
DELETE FROM `lista_desejos`;
INSERT INTO `lista_desejos` (`id_des`, `id_des_user`, `data_alteracao_LD`, `id_des_prod`) VALUES
	(1, 1, '2025-03-12 23:58:45', 1),
	(2, 2, '2025-03-12 23:58:45', 2),
	(3, 3, '2025-03-12 23:58:45', 3),
	(4, 4, '2025-03-12 23:58:45', 4),
	(5, 5, '2025-03-12 23:58:45', 5),
	(6, 6, '2025-03-12 23:58:45', 6),
	(7, 7, '2025-03-12 23:58:45', 7),
	(8, 8, '2025-03-12 23:58:45', 8),
	(9, 9, '2025-03-12 23:58:45', 9),
	(10, 10, '2025-03-12 23:58:45', 10),
	(11, 11, '2025-03-12 23:58:45', 11),
	(12, 12, '2025-03-12 23:58:45', 12),
	(13, 13, '2025-03-12 23:58:45', 13),
	(14, 12, '2025-03-12 23:58:45', 14),
	(15, 11, '2025-03-12 23:58:45', 15),
	(16, 10, '2025-03-12 23:58:45', 16),
	(17, 9, '2025-03-12 23:58:45', 17),
	(18, 8, '2025-03-12 23:58:45', 18),
	(19, 7, '2025-03-12 23:58:45', 19),
	(20, 6, '2025-03-12 23:58:45', 20);

-- Copiando estrutura para tabela labbd2.logs
CREATE TABLE IF NOT EXISTS `logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int DEFAULT NULL,
  `acao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `descricao` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `data` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `tipo_usuario` enum('usuario','funcionario','administrador') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `logs_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`user_id`),
  CONSTRAINT `logs_chk_1` CHECK ((`tipo_usuario` = _utf8mb4'administrador'))
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.logs: ~0 rows (aproximadamente)
DELETE FROM `logs`;
INSERT INTO `logs` (`log_id`, `usuario_id`, `acao`, `descricao`, `data`, `tipo_usuario`) VALUES
	(1, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(2, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(3, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(4, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(5, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(6, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(7, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(8, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(9, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(10, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(11, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(12, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(13, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(14, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(15, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(16, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(17, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(18, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador'),
	(19, 3, 'Login', 'Administrador logou no sistema', '2025-03-12 23:58:45', 'administrador'),
	(20, 3, 'Logout', 'Administrador saiu do sistema', '2025-03-12 23:58:45', 'administrador');

-- Copiando estrutura para tabela labbd2.logs_acesso
CREATE TABLE IF NOT EXISTS `logs_acesso` (
  `log_acesso_id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int DEFAULT NULL,
  `data_acesso` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status_acesso` enum('sucesso','falha') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`log_acesso_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `logs_acesso_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.logs_acesso: ~0 rows (aproximadamente)
DELETE FROM `logs_acesso`;
INSERT INTO `logs_acesso` (`log_acesso_id`, `usuario_id`, `data_acesso`, `status_acesso`) VALUES
	(1, 1, '2025-03-12 23:58:45', 'sucesso'),
	(2, 2, '2025-03-12 23:58:45', 'sucesso'),
	(3, 3, '2025-03-12 23:58:45', 'sucesso'),
	(4, 4, '2025-03-12 23:58:45', 'sucesso'),
	(5, 5, '2025-03-12 23:58:45', 'sucesso'),
	(6, 6, '2025-03-12 23:58:45', 'sucesso'),
	(7, 7, '2025-03-12 23:58:45', 'sucesso'),
	(8, 8, '2025-03-12 23:58:45', 'sucesso'),
	(9, 9, '2025-03-12 23:58:45', 'sucesso'),
	(10, 10, '2025-03-12 23:58:45', 'sucesso'),
	(11, 11, '2025-03-12 23:58:45', 'sucesso'),
	(12, 12, '2025-03-12 23:58:45', 'sucesso'),
	(13, 13, '2025-03-12 23:58:45', 'sucesso'),
	(14, 13, '2025-03-12 23:58:45', 'sucesso'),
	(15, 13, '2025-03-12 23:58:45', 'sucesso'),
	(16, 3, '2025-03-12 23:58:45', 'sucesso'),
	(17, 3, '2025-03-12 23:58:45', 'sucesso'),
	(18, 3, '2025-03-12 23:58:45', 'sucesso'),
	(19, 3, '2025-03-12 23:58:45', 'sucesso'),
	(20, 3, '2025-03-12 23:58:45', 'sucesso');

-- Copiando estrutura para tabela labbd2.notificacoes
CREATE TABLE IF NOT EXISTS `notificacoes` (
  `notificacao_id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `mensagem` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `data_envio` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `lida` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`notificacao_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `notificacoes_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.notificacoes: ~0 rows (aproximadamente)
DELETE FROM `notificacoes`;
INSERT INTO `notificacoes` (`notificacao_id`, `usuario_id`, `mensagem`, `data_envio`, `lida`) VALUES
	(1, 1, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(2, 2, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(3, 3, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(4, 4, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(5, 5, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(6, 6, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(7, 7, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(8, 8, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(9, 9, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(10, 10, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(11, 11, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(12, 12, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(13, 13, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(14, 12, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(15, 11, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(16, 10, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(17, 9, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(18, 8, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(19, 7, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0),
	(20, 6, 'Seu pedido foi enviado.', '2025-03-12 23:58:45', 0);

-- Copiando estrutura para tabela labbd2.pedidos
CREATE TABLE IF NOT EXISTS `pedidos` (
  `ped_id` int NOT NULL AUTO_INCREMENT,
  `id_user_ped` int NOT NULL,
  `status_ped` enum('em analise','aprovado','separado','enviado','entregue') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'em analise',
  `forma_pagamento` enum('credito','debito','pix') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `data_pedido` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `cod_rast` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`ped_id`),
  KEY `id_user_ped` (`id_user_ped`),
  CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`id_user_ped`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.pedidos: ~0 rows (aproximadamente)
DELETE FROM `pedidos`;
INSERT INTO `pedidos` (`ped_id`, `id_user_ped`, `status_ped`, `forma_pagamento`, `data_pedido`, `cod_rast`) VALUES
	(1, 1, 'enviado', 'credito', '2025-03-12 23:53:36', 'ABC123'),
	(2, 2, 'enviado', 'debito', '2025-03-12 23:53:36', 'DEF456'),
	(3, 3, 'enviado', 'pix', '2025-03-12 23:53:36', 'GHI789'),
	(4, 4, 'enviado', 'credito', '2025-03-12 23:53:36', 'JKL012'),
	(5, 5, 'enviado', 'debito', '2025-03-12 23:53:36', 'MNO345'),
	(6, 6, 'enviado', 'pix', '2025-03-12 23:53:36', 'PQR678'),
	(7, 7, 'enviado', 'credito', '2025-03-12 23:53:36', 'STU901'),
	(8, 8, 'enviado', 'debito', '2025-03-12 23:53:36', 'VWX234'),
	(9, 9, 'enviado', 'pix', '2025-03-12 23:53:36', 'YZA567'),
	(10, 10, 'enviado', 'credito', '2025-03-12 23:53:36', 'BCD890'),
	(11, 11, 'enviado', 'debito', '2025-03-12 23:53:36', 'EFG123'),
	(12, 12, 'enviado', 'pix', '2025-03-12 23:53:36', 'HIJ456'),
	(13, 13, 'enviado', 'credito', '2025-03-12 23:53:36', 'KLM789'),
	(14, 12, 'enviado', 'debito', '2025-03-12 23:53:36', 'NOP012'),
	(15, 11, 'enviado', 'pix', '2025-03-12 23:53:36', 'QRS345'),
	(16, 10, 'enviado', 'credito', '2025-03-12 23:53:36', 'TUV678'),
	(17, 9, 'enviado', 'debito', '2025-03-12 23:53:36', 'WXY901'),
	(18, 8, 'enviado', 'pix', '2025-03-12 23:53:36', 'ZAB234'),
	(19, 7, 'enviado', 'credito', '2025-03-12 23:53:36', 'CDE567'),
	(20, 6, 'enviado', 'debito', '2025-03-12 23:53:36', 'FGH890');

-- Copiando estrutura para tabela labbd2.pedido_produto
CREATE TABLE IF NOT EXISTS `pedido_produto` (
  `ped_prod_id` int NOT NULL AUTO_INCREMENT,
  `ped_id` int NOT NULL,
  `prod_id` int NOT NULL,
  `quantidade` int NOT NULL,
  `preco_unitario` decimal(10,2) NOT NULL,
  PRIMARY KEY (`ped_prod_id`),
  KEY `ped_id` (`ped_id`),
  KEY `prod_id` (`prod_id`),
  CONSTRAINT `pedido_produto_ibfk_1` FOREIGN KEY (`ped_id`) REFERENCES `pedidos` (`ped_id`),
  CONSTRAINT `pedido_produto_ibfk_2` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`),
  CONSTRAINT `pedido_produto_chk_1` CHECK ((`quantidade` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.pedido_produto: ~0 rows (aproximadamente)
DELETE FROM `pedido_produto`;
INSERT INTO `pedido_produto` (`ped_prod_id`, `ped_id`, `prod_id`, `quantidade`, `preco_unitario`) VALUES
	(41, 1, 1, 1, 199.99),
	(42, 2, 2, 1, 149.99),
	(43, 3, 3, 1, 179.99),
	(44, 4, 4, 1, 169.99),
	(45, 5, 5, 1, 189.99),
	(46, 6, 6, 1, 129.99),
	(47, 7, 7, 1, 159.99),
	(48, 8, 8, 1, 139.99),
	(49, 9, 9, 1, 99.99),
	(50, 10, 10, 1, 249.99),
	(51, 11, 11, 1, 499.99),
	(52, 12, 12, 1, 299.99),
	(53, 13, 13, 1, 349.99),
	(54, 12, 14, 1, 129.99),
	(55, 11, 15, 1, 199.99),
	(56, 10, 16, 1, 249.99),
	(57, 9, 17, 1, 149.99),
	(58, 8, 18, 1, 99.99),
	(59, 7, 19, 1, 399.99),
	(60, 6, 20, 1, 89.99);

-- Copiando estrutura para tabela labbd2.permissoes_funcionarios
CREATE TABLE IF NOT EXISTS `permissoes_funcionarios` (
  `perm_id` int NOT NULL AUTO_INCREMENT,
  `func_id` int NOT NULL,
  `pode_editar_usuario` tinyint(1) DEFAULT '1',
  `pode_editar_pedido` tinyint(1) DEFAULT '1',
  `pode_ver_pagamento` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`perm_id`),
  KEY `FK_permissoes_funcionarios_usuarios` (`func_id`),
  CONSTRAINT `FK_permissoes_funcionarios_usuarios` FOREIGN KEY (`func_id`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.permissoes_funcionarios: ~0 rows (aproximadamente)
DELETE FROM `permissoes_funcionarios`;
INSERT INTO `permissoes_funcionarios` (`perm_id`, `func_id`, `pode_editar_usuario`, `pode_editar_pedido`, `pode_ver_pagamento`) VALUES
	(1, 2, 1, 1, 0),
	(2, 2, 1, 1, 0),
	(3, 2, 1, 1, 0),
	(4, 2, 1, 1, 0),
	(5, 2, 1, 1, 0),
	(6, 2, 1, 1, 0),
	(7, 2, 1, 1, 0),
	(8, 2, 1, 1, 0),
	(9, 2, 1, 1, 0),
	(10, 2, 1, 1, 0),
	(11, 2, 1, 1, 0),
	(12, 2, 1, 1, 0),
	(13, 2, 1, 1, 0),
	(14, 2, 1, 1, 0),
	(15, 2, 1, 1, 0),
	(16, 2, 1, 1, 0),
	(17, 2, 1, 1, 0),
	(18, 2, 1, 1, 0),
	(19, 2, 1, 1, 0),
	(20, 2, 1, 1, 0);

-- Copiando estrutura para tabela labbd2.produtos
CREATE TABLE IF NOT EXISTS `produtos` (
  `prod_id` int NOT NULL AUTO_INCREMENT,
  `nome_prod` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `qtd` int DEFAULT NULL,
  `preco` decimal(10,2) DEFAULT NULL,
  `cat_id` int NOT NULL,
  `editora_id` int DEFAULT NULL,
  `tempo_de_jogo` int DEFAULT NULL,
  `numero_jogadores` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `itens_inclusos` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `descri` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `clas_ind` enum('L','10','12','14','16','18') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `autor` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `categoria` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`prod_id`),
  KEY `cat_id` (`cat_id`),
  KEY `editora_id` (`editora_id`),
  CONSTRAINT `produtos_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `categorias` (`cat_id`),
  CONSTRAINT `produtos_ibfk_2` FOREIGN KEY (`editora_id`) REFERENCES `editoras` (`editora_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.produtos: ~0 rows (aproximadamente)
DELETE FROM `produtos`;
INSERT INTO `produtos` (`prod_id`, `nome_prod`, `qtd`, `preco`, `cat_id`, `editora_id`, `tempo_de_jogo`, `numero_jogadores`, `itens_inclusos`, `descri`, `clas_ind`, `autor`, `categoria`) VALUES
	(1, 'Catan', 15, 199.99, 1, 1, 60, '3-4', 'Tabuleiro, peças de madeira, cartas de recurso, dados', 'Um clássico jogo de estratégia e negociação.', NULL, 'Klaus Teuber', 'Estratégia'),
	(2, 'Carcassonne', 8, 149.99, 1, 2, 45, '2-5', 'Tabuleiro modular, meeples, cartas de terreno', 'Jogo de colocação de peças e controle de áreas.', NULL, 'Klaus-Jürgen Wrede', 'Estratégia'),
	(3, 'Pandemic', 25, 179.99, 2, 3, 45, '2-4', 'Tabuleiro, cartas de cidade, cartas de evento, marcadores de doença', 'Jogo cooperativo onde os jogadores combatem doenças globais.', NULL, 'Matt Leacock', 'Cooperativo'),
	(4, 'Ticket to Ride', 10, 169.99, 1, 4, 60, '2-5', 'Tabuleiro, cartas de trem, peças de trem, cartas de destino', 'Jogo de construção de rotas ferroviárias.', NULL, 'Alan R. Moon', 'Estratégia'),
	(5, '7 Wonders', 40, 189.99, 1, 5, 30, '2-7', 'Cartas de maravilha, cartas de recurso, moedas', 'Jogo de construção de civilizações e maravilhas.', NULL, 'Antoine Bauza', 'Estratégia'),
	(6, 'Dixit', 20, 129.99, 3, 6, 30, '3-6', 'Cartas ilustradas, marcadores de votação, tabuleiro de pontuação', 'Jogo de criatividade e adivinhação.', NULL, 'Jean-Louis Roubira', 'Party Game'),
	(7, 'Splendor', 5, 159.99, 1, 7, 30, '2-4', 'Fichas de gemas, cartas de desenvolvimento, cartas de nobre', 'Jogo de coleta de gemas e desenvolvimento econômico.', NULL, 'Marc André', 'Estratégia'),
	(8, 'Azul', 3, 139.99, 1, 8, 45, '2-4', 'Peças de azulejo, tabuleiros individuais, marcadores de pontuação', 'Jogo de colocação de azulejos e criação de padrões.', NULL, 'Michael Kiesling', 'Estratégia'),
	(9, 'Codenames', 50, 99.99, 3, 9, 15, '2-8', 'Cartas de palavras, cartas de agente, cartas de dica', 'Jogo de palavras e dedução em equipes.', NULL, 'Vlaada Chvátil', 'Party Game'),
	(10, 'Wingspan', 100, 249.99, 1, 10, 60, '1-5', 'Cartas de pássaros, dados de comida, tabuleiros individuais', 'Jogo de estratégia e coleção de pássaros.', NULL, 'Elizabeth Hargrave', 'Estratégia'),
	(11, 'Gloomhaven', 12, 499.99, 7, 11, 120, '1-4', 'Tabuleiro, cartas, miniaturas, marcadores', 'Jogo de RPG tático com campanha cooperativa.', NULL, 'Isaac Childres', 'Jogos de Aventura'),
	(12, 'Terraforming Mars', 18, 299.99, 1, 12, 120, '1-5', 'Tabuleiro, cartas, marcadores, cubos', 'Jogo de estratégia onde os jogadores transformam Marte.', NULL, 'Jacob Fryxelius', 'Estratégia'),
	(13, 'Scythe', 10, 349.99, 1, 13, 115, '1-5', 'Tabuleiro, miniaturas, cartas, marcadores', 'Jogo de estratégia em um mundo alternativo dos anos 1920.', NULL, 'Jamey Stegmaier', 'Estratégia'),
	(14, 'Gizmos', 22, 129.99, 1, 14, 45, '2-4', 'Cartas, marcadores, esferas de energia', 'Jogo de construção de máquinas e combinações.', NULL, 'Phil Walker-Harding', 'Estratégia'),
	(15, 'Root', 15, 199.99, 1, 15, 90, '2-4', 'Tabuleiro, miniaturas, cartas, marcadores', 'Jogo de estratégia assimétrica com animais antropomórficos.', NULL, 'Cole Wehrle', 'Estratégia'),
	(16, 'Everdell', 20, 249.99, 1, 16, 80, '1-4', 'Tabuleiro, cartas, marcadores, miniaturas', 'Jogo de construção de cidades em um mundo de animais.', NULL, 'James A. Wilson', 'Estratégia'),
	(17, 'Wingspan: Oceania', 30, 149.99, 1, 10, 60, '1-5', 'Cartas de pássaros, dados de comida, tabuleiros individuais', 'Expansão de Wingspan com pássaros da Oceania.', NULL, 'Elizabeth Hargrave', 'Estratégia'),
	(18, 'Catan: Extensão 5-6 Jogadores', 25, 99.99, 1, 1, 90, '3-6', 'Tabuleiro, peças de madeira, cartas de recurso, dados', 'Extensão para jogar Catan com mais jogadores.', NULL, 'Klaus Teuber', 'Estratégia'),
	(19, 'Pandemic: Legado', 10, 399.99, 2, 3, 60, '2-4', 'Tabuleiro, cartas, marcadores, adesivos', 'Jogo cooperativo com campanha e mudanças permanentes.', NULL, 'Matt Leacock', 'Cooperativo'),
	(20, 'Codenames: Pictures', 35, 89.99, 3, 9, 15, '2-8', 'Cartas de imagens, cartas de agente, cartas de dica', 'Versão de Codenames com imagens.', NULL, 'Vlaada Chvátil', 'Party Game');

-- Copiando estrutura para tabela labbd2.produtos_historico_navegacao
CREATE TABLE IF NOT EXISTS `produtos_historico_navegacao` (
  `prod_hist_id` int NOT NULL AUTO_INCREMENT,
  `prod_id` int NOT NULL,
  `hist_id` int NOT NULL,
  PRIMARY KEY (`prod_hist_id`),
  KEY `prod_id` (`prod_id`),
  KEY `hist_id` (`hist_id`),
  CONSTRAINT `produtos_historico_navegacao_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`),
  CONSTRAINT `produtos_historico_navegacao_ibfk_2` FOREIGN KEY (`hist_id`) REFERENCES `historico_navegacao` (`id_hist`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.produtos_historico_navegacao: ~0 rows (aproximadamente)
DELETE FROM `produtos_historico_navegacao`;
INSERT INTO `produtos_historico_navegacao` (`prod_hist_id`, `prod_id`, `hist_id`) VALUES
	(21, 1, 1),
	(22, 2, 2),
	(23, 3, 3),
	(24, 4, 4),
	(25, 5, 5),
	(26, 6, 6),
	(27, 7, 7),
	(28, 8, 8),
	(29, 9, 9),
	(30, 10, 10),
	(31, 11, 11),
	(32, 12, 12),
	(33, 13, 13),
	(34, 14, 14),
	(35, 15, 15),
	(36, 16, 16),
	(37, 17, 17),
	(38, 18, 18),
	(39, 19, 19),
	(40, 20, 20);

-- Copiando estrutura para tabela labbd2.produtos_lista_desejos
CREATE TABLE IF NOT EXISTS `produtos_lista_desejos` (
  `prod_lista_id` int NOT NULL AUTO_INCREMENT,
  `prod_id` int NOT NULL,
  `lista_id` int NOT NULL,
  PRIMARY KEY (`prod_lista_id`),
  KEY `prod_id` (`prod_id`),
  KEY `lista_id` (`lista_id`),
  CONSTRAINT `produtos_lista_desejos_ibfk_1` FOREIGN KEY (`prod_id`) REFERENCES `produtos` (`prod_id`),
  CONSTRAINT `produtos_lista_desejos_ibfk_2` FOREIGN KEY (`lista_id`) REFERENCES `lista_desejos` (`id_des`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.produtos_lista_desejos: ~0 rows (aproximadamente)
DELETE FROM `produtos_lista_desejos`;
INSERT INTO `produtos_lista_desejos` (`prod_lista_id`, `prod_id`, `lista_id`) VALUES
	(41, 1, 1),
	(42, 2, 2),
	(43, 3, 3),
	(44, 4, 4),
	(45, 5, 5),
	(46, 6, 6),
	(47, 7, 7),
	(48, 8, 8),
	(49, 9, 9),
	(50, 10, 10),
	(51, 11, 11),
	(52, 12, 12),
	(53, 13, 13),
	(54, 14, 14),
	(55, 15, 15),
	(56, 16, 16),
	(57, 17, 17),
	(58, 18, 18),
	(59, 19, 19),
	(60, 20, 20);

-- Copiando estrutura para tabela labbd2.promocoes
CREATE TABLE IF NOT EXISTS `promocoes` (
  `promocao_id` int NOT NULL AUTO_INCREMENT,
  `nome_promocao` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `desconto` decimal(5,2) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  `data_fim` date DEFAULT NULL,
  PRIMARY KEY (`promocao_id`),
  CONSTRAINT `promocoes_chk_1` CHECK (((`desconto` > 0) and (`desconto` <= 100)))
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.promocoes: ~0 rows (aproximadamente)
DELETE FROM `promocoes`;
INSERT INTO `promocoes` (`promocao_id`, `nome_promocao`, `desconto`, `data_inicio`, `data_fim`) VALUES
	(1, 'Promoção de Estratégia', 20.00, '2023-12-01', '2023-12-31'),
	(2, 'Promoção de Cooperativos', 15.00, '2023-12-01', '2023-12-31'),
	(3, 'Promoção de Party Games', 25.00, '2023-12-01', '2023-12-31'),
	(4, 'Promoção de Eurogames', 30.00, '2023-12-01', '2023-12-31'),
	(5, 'Promoção de Jogos de Cartas', 10.00, '2023-12-01', '2023-12-31'),
	(6, 'Promoção de Jogos de Miniaturas', 35.00, '2023-12-01', '2023-12-31'),
	(7, 'Promoção de Jogos de Dedução', 40.00, '2023-12-01', '2023-12-31'),
	(8, 'Promoção de Jogos de Aventura', 50.00, '2023-12-01', '2023-12-31'),
	(9, 'Promoção de Jogos de Construção', 45.00, '2023-12-01', '2023-12-31'),
	(10, 'Promoção de Jogos de Guerra', 60.00, '2023-12-01', '2023-12-31'),
	(11, 'Promoção de Jogos de Tabuleiro', 20.00, '2023-12-01', '2023-12-31'),
	(12, 'Promoção de Jogos de Cartas Colecionáveis', 15.00, '2023-12-01', '2023-12-31'),
	(13, 'Promoção de Jogos de RPG', 25.00, '2023-12-01', '2023-12-31'),
	(14, 'Promoção de Jogos de Quebra-Cabeça', 30.00, '2023-12-01', '2023-12-31'),
	(15, 'Promoção de Jogos de Memória', 10.00, '2023-12-01', '2023-12-31'),
	(16, 'Promoção de Jogos de Azar', 35.00, '2023-12-01', '2023-12-31'),
	(17, 'Promoção de Jogos de Palavras', 40.00, '2023-12-01', '2023-12-31'),
	(18, 'Promoção de Jogos de Lógica', 50.00, '2023-12-01', '2023-12-31'),
	(19, 'Promoção de Jogos de Simulação', 45.00, '2023-12-01', '2023-12-31'),
	(20, 'Promoção de Jogos de Terror', 60.00, '2023-12-01', '2023-12-31');

-- Copiando estrutura para tabela labbd2.reclamacoes_suporte
CREATE TABLE IF NOT EXISTS `reclamacoes_suporte` (
  `reclamacao_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `assunto` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `descricao` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status` enum('aberta','em andamento','resolvida') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'aberta',
  `data_abertura` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `user_respondeu_id` int DEFAULT NULL,
  `resposta` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`reclamacao_id`),
  KEY `user_id` (`user_id`),
  KEY `User Resposta` (`user_respondeu_id`),
  CONSTRAINT `reclamacoes_suporte_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `usuarios` (`user_id`),
  CONSTRAINT `User Resposta` FOREIGN KEY (`user_respondeu_id`) REFERENCES `usuarios` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.reclamacoes_suporte: ~0 rows (aproximadamente)
DELETE FROM `reclamacoes_suporte`;
INSERT INTO `reclamacoes_suporte` (`reclamacao_id`, `user_id`, `assunto`, `descricao`, `status`, `data_abertura`, `user_respondeu_id`, `resposta`) VALUES
	(21, 1, 'Peças faltando', 'Comprei Catan e faltam peças de madeira.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(22, 2, 'Tabuleiro danificado', 'O tabuleiro de Carcassonne veio quebrado.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.'),
	(23, 3, 'Cartas rasgadas', 'As cartas de Pandemic estão rasgadas.', 'aberta', '2025-03-13 00:04:27', 1, 'Estamos verificando sua reclamação.'),
	(24, 4, 'Peças de trem faltando', 'Faltam peças de trem no Ticket to Ride.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(25, 5, 'Cartas de maravilha danificadas', 'As cartas de 7 Wonders estão danificadas.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.'),
	(26, 6, 'Cartas de votação faltando', 'Faltam cartas de votação no Dixit.', 'aberta', '2025-03-13 00:04:27', 1, 'Estamos verificando sua reclamação.'),
	(27, 7, 'Fichas de gemas danificadas', 'As fichas de Splendor estão quebradas.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(28, 8, 'Azulejos quebrados', 'Os azulejos de Azul estão quebrados.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.'),
	(29, 9, 'Cartas de palavras faltando', 'Faltam cartas de palavras no Codenames.', 'aberta', '2025-03-13 00:04:27', 1, 'Estamos verificando sua reclamação.'),
	(30, 10, 'Cartas de pássaros danificadas', 'As cartas de pássaros de Wingspan estão danificadas.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(31, 11, 'Miniaturas quebradas', 'As miniaturas de Gloomhaven estão quebradas.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.'),
	(32, 12, 'Cartas danificadas', 'As cartas de Terraforming Mars estão danificadas.', 'aberta', '2025-03-13 00:04:27', 1, 'Estamos verificando sua reclamação.'),
	(33, 13, 'Tabuleiro riscado', 'O tabuleiro de Scythe está riscado.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(34, 12, 'Esferas de energia faltando', 'Faltam esferas de energia no Gizmos.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.'),
	(35, 11, 'Miniaturas faltando', 'Faltam miniaturas no Root.', 'aberta', '2025-03-13 00:04:27', 1, 'Estamos verificando sua reclamação.'),
	(36, 10, 'Cartas danificadas', 'As cartas de Everdell estão danificadas.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(37, 9, 'Cartas de pássaros faltando', 'Faltam cartas de pássaros no Wingspan: Oceania.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.'),
	(38, 8, 'Peças de madeira faltando', 'Faltam peças de madeira no Catan: Extensão 5-6 Jogadores.', 'aberta', '2025-03-13 00:04:27', 1, 'Estamos verificando sua reclamação.'),
	(39, 7, 'Adesivos faltando', 'Faltam adesivos no Pandemic: Legado.', 'aberta', '2025-03-13 00:04:27', 2, 'Estamos verificando sua reclamação.'),
	(40, 6, 'Cartas de imagens danificadas', 'As cartas de imagens do Codenames: Pictures estão danificadas.', 'aberta', '2025-03-13 00:04:27', 3, 'Estamos verificando sua reclamação.');

-- Copiando estrutura para tabela labbd2.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `cpf` varchar(14) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `dataNasc` timestamp NULL DEFAULT NULL,
  `telefone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `endereco` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `senha` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tipo` enum('cliente','funcionario','admin') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Copiando dados para a tabela labbd2.usuarios: ~0 rows (aproximadamente)
DELETE FROM `usuarios`;
INSERT INTO `usuarios` (`user_id`, `nome`, `cpf`, `dataNasc`, `telefone`, `endereco`, `email`, `senha`, `tipo`) VALUES
	(1, 'João Silva', '123.456.789-00', '1990-01-01 03:00:00', '(11) 99999-9999', 'Rua A, 123', 'joao.silva@example.com', 'senha123', 'cliente'),
	(2, 'Maria Oliveira', '987.654.321-00', '1985-05-15 03:00:00', '(11) 88888-8888', 'Rua B, 456', 'maria.oliveira@example.com', 'senha456', 'funcionario'),
	(3, 'Admin', '121.222.333-44', '1980-10-20 03:00:00', '(11) 77777-7777', 'Rua C, 789', 'admin@example.com', 'admin123', 'admin'),
	(4, 'Carlos Souza', '222.333.444-55', '1992-03-12 03:00:00', '(11) 99999-8888', 'Rua D, 789', 'carlos.souza@example.com', 'senha789', 'cliente'),
	(5, 'Ana Paula', '333.444.555-66', '1988-07-25 03:00:00', '(11) 88888-7777', 'Rua E, 101', 'ana.paula@example.com', 'senha101', 'cliente'),
	(6, 'Pedro Rocha', '444.555.666-77', '1995-11-30 03:00:00', '(11) 77777-6666', 'Rua F, 202', 'pedro.rocha@example.com', 'senha202', 'cliente'),
	(7, 'Fernanda Lima', '555.666.777-88', '1987-09-15 03:00:00', '(11) 66666-5555', 'Rua G, 303', 'fernanda.lima@example.com', 'senha303', 'cliente'),
	(8, 'Ricardo Santos', '666.777.888-99', '1991-04-20 03:00:00', '(11) 55555-4444', 'Rua H, 404', 'ricardo.santos@example.com', 'senha404', 'cliente'),
	(9, 'Juliana Costa', '777.888.999-00', '1989-12-05 03:00:00', '(11) 44444-3333', 'Rua I, 505', 'juliana.costa@example.com', 'senha505', 'cliente'),
	(10, 'Lucas Oliveira', '888.999.000-11', '1993-08-10 03:00:00', '(11) 33333-2222', 'Rua J, 606', 'lucas.oliveira@example.com', 'senha606', 'cliente'),
	(11, 'Mariana Silva', '999.000.111-22', '1994-06-18 03:00:00', '(11) 22222-1111', 'Rua K, 707', 'mariana.silva@example.com', 'senha707', 'cliente'),
	(12, 'Gustavo Pereira', '000.111.222-33', '1996-02-22 03:00:00', '(11) 11111-0000', 'Rua L, 808', 'gustavo.pereira@example.com', 'senha808', 'cliente'),
	(13, 'Camila Rocha', '111.222.333-44', '1997-01-30 03:00:00', '(11) 00000-9999', 'Rua M, 909', 'camila.rocha@example.com', 'senha909', 'cliente');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;