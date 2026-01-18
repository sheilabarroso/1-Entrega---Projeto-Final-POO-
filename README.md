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
### 🛒 Sistema de Loja Virtual (CLI)
Este projeto é um simulador de e-commerce operando via linha de comando, desenvolvido com foco em Programação Orientada a Objetos (POO) e Persistência de Dados. O sistema gerencia desde a validação de estoque e aplicação de cupons até o faturamento com geração de Nota Fiscal.

## 🚀 Como Rodar
1. Certifique-se de ter o Python 3.8+ instalado.

2. Clone o repositório ou copie o código para um arquivo chamado main.py.

3. Execute o comando:
```bash
python main.py
```
O sistema criará automaticamente o diretório src/data/ e o arquivo database.json para armazenar os dados.

## 🏗️ Arquitetura e Classes
O projeto está dividido em responsabilidades claras:

- Modelagem (Entidades)
- Produto: Gerencia informações do item, preço e controle rigoroso de estoque via @property.
- Cliente / Endereco: Representam o comprador e o local de destino, essenciais para o cálculo de frete e emissão de nota.
- Cupom: Classe de regra de negócio que valida datas de expiração e tipos de desconto (Fixo ou Percentual).
- Pedido: O "coração" do sistema. Orquestra itens, calcula o total devido, gerencia a transação financeira e altera o estado do estoque.
- Persistência (Dados)
- GerenciadorDados: Centraliza a leitura e escrita no arquivo JSON.
- LojaEncoder: Um padrão de codificação customizado que ensina o Python a salvar objetos complexos (como datetime e Enum) em formato de texto.

## 🧠 Padrões e Conceitos de POO Aplicados
Para atender às exigências de um projeto de alta qualidade, foram utilizados:

- Encapsulamento: Uso de decoradores @property e .setter para garantir que o estoque nunca seja negativo e preços nunca sejam menores ou iguais a zero.
- Enumerações (Enum): Uso da classe StatusPedido para evitar "strings mágicas" e garantir que o pedido passe apenas por estados válidos (CRIADO, PAGO, CANCELADO).
- Composição: Um Pedido é composto por uma lista de ItemCarrinho, que por sua vez compõe um Produto.
- Tratamento de Exceções: Uso de try/except e raise ValueError para lidar com falhas de negócio (ex: tentar pagar um pedido já cancelado ou falta de estoque).

## 📊 Estrutura de Pastas Sugerida
Para organizar este código conforme os padrões de mercado, utilize:
```bash
Plaintext
loja-virtual/
├── src/
│   ├── data/
│   │   └── database.json    # Criado automaticamente
│   └── main.py              # Código principal
└── README.md
```

## 🔗 Diagrama:
<img width="913" height="685" alt="image" src="https://github.com/user-attachments/assets/6d79940b-796f-496d-b479-43a1007dcad9" />

## 🔗 Código integral:
```bash
import json
import uuid
from enum import Enum
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path
```
## PERSISTÊNCIA (dados.py integrado)
```bash
class LojaEncoder(json.JSONEncoder):
    """Garante que Datas e Enums sejam salvos corretamente no JSON."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Enum):
            return obj.value
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        return super().default(obj)

class GerenciadorDados:
    def __init__(self, arquivo_db="src/data/database.json"):
        self.caminho = Path(arquivo_db)
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        if not self.caminho.exists():
            self.salvar_dados({"produtos": [], "pedidos": []})

    def salvar_dados(self, dados: dict):
        with open(self.caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, cls=LojaEncoder, ensure_ascii=False)
```
## MODELAGEM (POO) 
```bash
class StatusPedido(Enum):
    CRIADO = "CRIADO"
    PAGO = "PAGO"
    CANCELADO = "CANCELADO"

class Endereco:
    def __init__(self, logradouro: str, cidade: str, uf: str, cep: str):
        self.logradouro = logradouro
        self.cidade = cidade
        self.uf = uf.upper()
        self.cep = cep

    def __str__(self):
        return f"{self.logradouro}, {self.cidade}-{self.uf}"

class Produto:
    def __init__(self, sku: str, nome: str, preco: float, estoque: int):
        self.sku = sku
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = True

    @property
    def preco(self): return self._preco
    @preco.setter
    def preco(self, v):
        if v <= 0: raise ValueError("Preço inválido")
        self._preco = v

    @property
    def estoque(self): return self._estoque
    @estoque.setter
    def estoque(self, v):
        if v < 0: raise ValueError("Estoque insuficiente")
        self._estoque = v

class Cupom:
    def __init__(self, codigo: str, tipo: str, valor: float, validade: str):
        self.codigo = codigo
        self.tipo = tipo.upper() # 'PERCENTUAL' ou 'VALOR'
        self.valor = valor
        self.validade = datetime.strptime(validade, "%Y-%m-%d")

    def esta_valido(self) -> bool:
        return datetime.now() <= self.validade

class ItemCarrinho:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = produto.preco * quantidade

class Pedido:
    def __init__(self, cliente_nome: str, endereco: Endereco, itens: List[ItemCarrinho], frete: float, cupom: Cupom = None):
        self.id = str(uuid.uuid4())[:8]
        self.cliente = cliente_nome
        self.endereco = endereco
        self.itens = itens
        self.status = StatusPedido.CRIADO
        self.valor_frete = frete
        self.cupom = cupom

    def calcular_desconto(self) -> float:
        if not self.cupom or not self.cupom.esta_valido():
            return 0.0
        subtotal = sum(i.subtotal for i in self.itens)
        if self.cupom.tipo == "PERCENTUAL":
            return subtotal * (self.cupom.valor / 100)
        return min(self.cupom.valor, subtotal)

    @property
    def total_devido(self):
        subtotal = sum(i.subtotal for i in self.itens)
        return max(subtotal + self.valor_frete - self.calcular_desconto(), 0.0)

    def pagar(self):
        if self.status != StatusPedido.CRIADO:
            raise ValueError("Pedido não pode ser pago.")
        for item in self.itens:
            item.produto.estoque -= item.quantidade
        self.status = StatusPedido.PAGO

    def gerar_nota(self):
        n = f"\n--- NOTA FISCAL #{self.id} ---\n"
        for i in self.itens:
            n += f"{i.produto.nome:.<20} x{i.quantidade}: R$ {i.subtotal:>8.2f}\n"
        n += f"Total Devido: R$ {self.total_devido:.2f}\n"
        n += f"Status: {self.status.value}\n"
        return n
```
## EXECUÇÃO
```bash
if __name__ == "__main__":
    db = GerenciadorDados()
    
    # Simulação
    p1 = Produto("SKU01", "Smartphone S25", 2500.0, 10)
    end = Endereco("Av. Beira Mar", "Fortaleza", "CE", "60000-000")
    cupom = Cupom("PROMO26", "VALOR", 50.0, "2026-12-31")
    
    item = ItemCarrinho(p1, 1)
    pedido = Pedido("Jayr Alencar", end, [item], 20.0, cupom)
    
    try:
        pedido.pagar()
        print(pedido.gerar_nota())
        
        # Salvando no JSON (Cumpre a exigência de persistência)
        db.salvar_dados({"pedidos": [pedido.__dict__]})
        print("Dados salvos com sucesso em database.json")
        
    except ValueError as e:
        print(f"Erro: {e}")

