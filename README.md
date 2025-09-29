# Atividade 2

# Projeto de Gerenciamento de Pedidos com Python e MySQL

Este projeto é uma atividade prática para demonstrar a integração entre Python e um banco de dados MySQL, utilizando a biblioteca `mysql-connector-python` (ou `SQLAlchemy`).

## 🎯 Objetivo

Adaptar um script Python capaz de realizar as quatro operações básicas de um banco de dados (CRUD) em um sistema simples de gerenciamento de pedidos.

## ✨ Funcionalidades

-   **Criação (Create):** Inserção de um novo pedido com múltiplos itens.
-   **Leitura (Read):** Listagem de todos os pedidos e seus respectivos itens.
-   **Atualização (Update):** Alteração de informações de um pedido existente.
-   **Deleção (Delete):** Remoção de um pedido e seus itens associados do banco de dados.
-   **Integridade dos Dados:** Uso de transações (`COMMIT`/`ROLLBACK`) para garantir que um pedido e seus itens sejam salvos de forma atômica (ou seja, "tudo ou nada").

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python
-   **Banco de Dados:** MySQL
-   **Bibliotecas:**
    -   `mysql-connector-python`
    -   `SQLAlchemy`
