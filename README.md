# 🎓 Gestão de Alunos (SqlitePython)

Uma aplicação para cadastro, visualização, cálculo de métricas e gerenciamento de alunos. O projeto inclui um backend/integração com **SQLite** via **Python**, uma interface gráfica web construída em **Streamlit**, além de uma prototipagem frontend interativa utilizando **HTML, CSS e JavaScript**.

---

## 📋 Sumário

- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar o Projeto](#-como-executar-o-projeto)
  - [1. Executando a Interface Streamlit (Python + SQLite)](#1-executando-a-interface-streamlit-python--sqlite)
  - [2. Visualizando a Interface Web (HTML/CSS/JS)](#2-visualizando-a-interface-web-htmlcssjs)
- [Mapeamento do Módulo de Banco de Dados (`banco.py`)](#-mapeamento-do-módulo-de-banco-de-dados-bancopy)
- [Melhorias Futuras](#-melhorias-futuras)
- [Licença](#-licença)

---

## 🚀 Visão Geral

O sistema permite gerenciar o cadastro acadêmico de alunos registrando **Nome**, **Idade** e **Curso**. 

O projeto conta com duas frentes de interface:
1. **Streamlit App (`interface.py`)**: Aplicação Python conectada diretamente ao banco de dados SQLite (`alunos.db`), permitindo persistência de dados em tempo real, adição de alunos, cálculo automático da média de idade e remoção de registros.
2. **Dashboard Web Frontend (`index.html`, `style.css`, `script.js`)**: Interface web estática e responsiva para demonstração de UI/UX com manipulação dinâmica do DOM e estatísticas instantâneas.

---

## ✨ Funcionalidades

- ➕ **Cadastro de Alunos**: Registro obrigatório de nome e curso, além de campo para idade.
- 📊 **Dashboard & Métricas**:
  - Total de alunos cadastrados.
  - Cálculo dinâmico da média de idade dos alunos.
  - Contagem de cursos distintos (na versão web).
- 📜 **Listagem Dinâmica**: Exibição dos alunos cadastrados em formato de tabela ou cards ordenados.
- 🗑️ **Remoção de Registros**: Exclusão simples de aluno por ID ou ação direta na interface.
- 🗄️ **Persistência de Dados**: Integração com SQLite para armazenamento durável na aplicação Python.

---

## 📁 Estrutura do Projeto

```text
SqlitePython/
├── alunos.db       # Banco de dados SQLite contendo a tabela 'alunos'
├── banco.py        # Módulo Python com funções CRUD para o SQLite
├── interface.py    # Aplicação interativa em Streamlit (interface principal Python)
├── index.html      # Estrutura HTML do dashboard web
├── style.css       # Estilização CSS moderna, responsiva e com temas
├── script.js       # Lógica JS do frontend estático (manipulação do DOM e métricas)
└── README.md       # Documentação do projeto