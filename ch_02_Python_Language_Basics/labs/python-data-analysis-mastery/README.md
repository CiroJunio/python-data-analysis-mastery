Aqui tens a versão final e consolidada do teu **README.md**, utilizando a metodologia **Minto Pyramid (BLUF)**. Este documento foi desenhado para destacar a tua evolução técnica, desde a resolução de erros de semântica até à implementação de testes de integridade.

---

# 📄 LAB: Telemetry Ingestion Mastery (Python Ch. 02)

## 1. OVERVIEW
**O objetivo deste laboratório foi desenvolver um motor de ingestão de dados resiliente para sensores de contêineres, capaz de normalizar múltiplos tipos de entrada (strings, listas e tuplas) com foco em eficiência de memória e integridade de tipos.** O resultado final é um pipeline robusto que processa sinais sujos, filtra metadados semânticos e valida limites de temperatura com latência inferior a 0.001s.

---

## 2. TECHNICAL CONTEXT
* **Core Concepts:** * **Semântica de Objetos:** Gestão de referências (*Binding*) e prova de identidade via `id()`.
    * **Imutabilidade:** Proteção de metadados críticos utilizando Tuplas para garantir que IDs de sensores não sejam alterados.
    * **Duck Typing:** Implementação do protocolo de iteração (`iter()`) para polimorfismo funcional sem uso de `isinstance` para coleções.
* **Ferramentas:** Docker (Python 3.11-slim), Docker Compose, Makefile (Interface de Abstração), IPython (Introspeção Ativa) e Pytest (Validação de Unidade).

---

## 3. DEBUGGING & LEARNING

* **Problema 1: O Erro de Atributo em Listas.** * *Cenário:* Ao utilizar `.split(';')` numa string, o Python retornava uma lista. Tentar executar um novo `.split(':')` diretamente no resultado causava um `AttributeError`.
    * *Solução:* Implementação de indexação direta `` após o primeiro split, garantindo que o objeto voltasse a ser uma string antes da segunda operação de fatiamento.
* **Problema 2: Ruído de Metadados (Citações).**
    * *Cenário:* A presença de etiquetas de referência técnica (`cite`) no código causou um `NameError`, interrompendo o pipeline de produção.
    * *Solução:* Limpeza cirúrgica do código para separar documentação teórica de lógica executável.
* **Aprendizagem Técnica:** Reforcei a compreensão de que, em Python, **atribuição é binding, não cópia**. O uso de *list comprehensions* no ingestor provou ser a forma ideal de criar novos objetos mutáveis a partir de fontes imutáveis sem corromper os dados originais.

---

## 4. HOW TO REPRODUCE

O projeto utiliza um **Makefile** para simplificar o ciclo de vida do desenvolvimento.

1.  **Configuração do Ambiente:**
    ```bash
    make setup
    ```
2.  **Execução em "Modo Fábrica" (Produção):**
    ```bash
    make run-main
    ```
3.  **Execução em "Modo Laboratório" (Exploração IPython):**
    ```bash
    make run
    # Dentro do IPython: %run src/main.py
    ```
4.  **Validação de Integridade (Testes):**
    ```bash
    make test
    ```
5.  **Limpeza e Descontaminação:**
    ```bash
    make clean
    ```

---
