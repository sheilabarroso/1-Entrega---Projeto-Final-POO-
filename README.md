# 1-Entrega---Projeto-Final-POO-
##Projeto: TEMA 9 – SISTEMA DE LOJA VIRTUAL SIMPLIFICADA

## Integrantes da Equipe:

- Sheila Matias Barroso (2025014897) - Modelagem da estrutura e Herança.
- Rubens Lopes dos Santos (2025014805) - Armazenamento de dados e settings.
- Carlos Rodrigo Ferreira da Silva (2025014304) - Gestão de Produto e Cliente.
- Viviana Barros Gomes de Sousa (2025014912) - Lógica central do carrinho, pedido e estoque.
- Vitoria Cavalcante Souza (2025019481) - Cálculos, Pagamento, Frete e Transições.
- Samuelson da Silva Lima (2025014860) - Garantia de qualidade e usabilidade.

## Principais Class do Projeto:

Classe: Produto
Atributos: sku, nome, categoria, preço_unitário, estoque
Métodos: cadastrar(), atualizar(), consultar(), substituir(), excluir()

Classe: Cliente
Atributos: id, nome, email, CPF, endereços
Métodos: cadastrar, atualizar, consultar, excluir

Classe: Carrinho
Atributos: id_carrinho, cliente, lista_produtos, valor_total
Métodos: adicionar_produto(), remover_produto(), calcular_total(), limpar_carrinho(), exibir_carrinho()

Classe: Cupom
Atributos: codigo, tipo_desconto (percentual ou valor fixo), valor_desconto, validade, uso_maximo, categorias_elegiveis
Métodos: validar(), aplicar_desconto()

Classe: Pedido
Atributos: id_pedido, cliente, itens, valor_total, status
Métodos: gerar_pedido(), cancelar_pedido(), consultar_pedido()

Classe: Frete
Atributos: origem, destino (CEP, cidade, UF), valor_frete, prazo_entrega 
Métodos: calcular_frete(), calcular_prazo()

Classe: Pagamento
Atributos:id_pagamento, pedido, forma_pagamento (Pix, débito, crédito, boleto), valor_pago, data_pagamento
Métodos: registrar_pagamento(), validar_pagamento()

