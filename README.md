# Projeto-Final-POO
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

# 🛒 Sistema de Loja Virtual Simplificada (CLI)

Projeto desenvolvido para a disciplina de **Programação Orientada a Objetos**, com o objetivo de simular uma loja virtual em ambiente de linha de comando (CLI), aplicando conceitos de **POO, regras de negócio, persistência de dados e testes automatizados**.

---

## 🎯 Objetivo do Projeto:
Desenvolver um sistema de loja virtual simplificado que permita:
- Cadastro e gerenciamento de produtos e clientes
- Criação de carrinho de compras
- Fechamento de pedidos
- Aplicação de cupons de desconto
- Cálculo de frete
- Registro de pagamentos
- Geração de relatórios
- Persistência de dados em JSON

---

## 🧱 Modelagem e Classes Principais:

### 📦 Produto
Classe base que representa um produto da loja.

**Atributos principais:**
- `sku` (único)
- `nome`
- `categoria`
- `preco`
- `estoque`
- `ativo`

**Conceitos aplicados:**
- Encapsulamento com `@property` para validação de preço (>0) e estoque (≥0)
- Métodos especiais: `__str__`, `__repr__`, `__eq__`, `__lt__`

### 📦 ProdutoFisico
Subclasse de `Produto`, utilizada para demonstrar **herança**.

**Atributo adicional:**
- `peso_kg`

---

### 👤 Cliente
Representa o cliente da loja.

**Atributos:**
- `id`
- `nome`
- `email`
- `cpf`
- `endereco`

**Regras:**
- Comparação de clientes por CPF ou e-mail (`__eq__`)

---

### 🏠 Endereco
Classe de valor que representa o endereço do cliente.

---

### 🛒 Carrinho / ItemCarrinho
Responsável por armazenar os itens antes da criação do pedido.

**Funcionalidades:**
- Adicionar e remover produtos
- Validar quantidade conforme estoque
- Calcular subtotal

**Métodos especiais:**
- `__len__`: retorna a quantidade total de itens no carrinho

---

### 📄 Pedido
Representa um pedido fechado a partir do carrinho.

**Atributos:**
- `id`
- `cliente`
- `itens`
- `frete`
- `cupom`
- `status`
- `total_pago`

**Estados possíveis:**
- `CRIADO`
- `PAGO`
- `ENVIADO`
- `ENTREGUE`
- `CANCELADO`

**Regras de negócio:**
- Transição controlada de estados
- Baixa de estoque ao pagamento
- Aplicação de cupom válido
- Cálculo do valor total

---

### 💳 Pagamento
Registra um pagamento realizado em um pedido.

---

### 🎟️ Cupom
Representa um cupom de desconto.

**Tipos:**
- `VALOR`
- `PERCENTUAL`

**Validações:**
- Data de validade
- Limite do desconto para não gerar total negativo

---

### 🚚 Frete
Responsável pelo cálculo do frete e prazo de entrega com base na UF do cliente, utilizando parâmetros definidos em `settings.json`.

---

## ⚙️ Persistência de Dados
A persistência é feita utilizando arquivos **JSON**, através do módulo `dados.py`.

Arquivos principais:
- `database.json`: armazena produtos, clientes, pedidos e cupons
- `seed.py`: cria dados iniciais para testes

---

## 🧠 Padrões e Conceitos Utilizados

- Programação Orientada a Objetos (POO)
- Encapsulamento com propriedades
- Herança
- Enum para estados do pedido
- Separação de responsabilidades (models, services, data)
- Métodos especiais (`__str__`, `__repr__`, `__eq__`, `__lt__`, `__len__`)
- Validações de regras de negócio

---

## 🖥️ Interface (CLI)
O sistema possui uma interface simples de linha de comando que permite:
- Listar produtos
- Criar pedidos
- Calcular frete
- Realizar pagamento

---

## ▶️ Como Executar

1. Instalar dependências:
```bash
pip install -r requirements.txt
```
2. (Opcional) Gerar dados iniciais:
```bash
python src/data/seed.py
```
## 🧪 Testes:
```bash
pytest
```
## 🗂️ Estrutura do projeto:
```bash
loja-virtual-cli/                 # Projeto principal da loja virtual em linha de comando
│
├── src/                          # Código-fonte da aplicação
│   ├── models/                   # Modelos (entidades) do sistema
│   │   ├── produto.py            # Classe Produto (nome, preço, estoque, etc.)
│   │   ├── cliente.py            # Classe Cliente (dados do cliente)
│   │   ├── endereco.py           # Classe Endereco (rua, cidade, CEP, etc.)
│   │   ├── cupom.py              # Classe Cupom (descontos e regras)
│   │   ├── carrinho.py           # Classe Carrinho (itens e valores)
│   │   ├── pedido.py             # Classe Pedido (resumo da compra)
│   │   ├── pagamento.py          # Classe Pagamento (forma e status do pagamento)
│   │   └── frete.py              # Classe Frete (cálculo de envio)
│   │
│   ├── data/                     # Camada de dados e persistência
│   │   ├── dados.py              # Funções para leitura e escrita de dados
│   │   ├── seed.py               # Dados iniciais para testes
│   │   └── database.json         # Banco de dados em formato JSON
│   │
│   ├── services/                 # Regras de negócio e serviços auxiliares
│   │   ├── estoque_service.py    # Lógica de controle de estoque
│   │   ├── relatorios.py         # Geração de relatórios
│   │   └── validacoes.py         # Validações de dados e regras
│   │
│   ├── cli.py                    # Interface de linha de comando (entrada do usuário)
│   └── settings.json             # Configurações gerais do sistema
│
├── tests/                        # Testes automatizados
│   ├── test_carrinho.py          # Testes do carrinho de compras
│   ├── test_pedido.py            # Testes dos pedidos
│   ├── test_cupom.py             # Testes dos cupons de desconto
│   └── test_frete.py             # Testes do cálculo de frete
│
├── README.md                     # Documentação do projeto
├── requirements.txt              # Dependências do projeto
└── .gitignore                    # Arquivos e pastas ignorados pelo Git
```
## 🔗 Diagrama:
<img width="826" height="841" alt="image" src="https://github.com/user-attachments/assets/79eb4f9b-319e-4e74-86b3-5867b9669942" />

