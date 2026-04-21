# 📄 LAB: TELEMETRY SANITIZER (Capítulo 03)

### 1. OVERVIEW
O objetivo deste laboratório foi construir um motor de processamento resiliente que limpa 10.000 linhas de telemetria ruidosa em tempo real, extraindo o pico de temperatura de cada sensor único através de uma arquitetura baseada em Geradores e estruturas de dados imutáveis.

### 2. TECHNICAL CONTEXT
* **Core Concept:** *Hashability* e o Protocolo Iterador. O projeto foca na distinção entre objetos mutáveis (Listas) e imutáveis (Tuplas) para garantir integridade em tabelas de dispersão (*Hash Maps*).
* **Tools Used:** Python 3.11 (Generators, Sets, Dicts), Docker & Docker Compose (Isolamento de ambiente), Makefile (Automação de tarefas de engenharia).

### 3. DEBUGGING & LEARNING
* **Issue:** O sistema apresentou um `TypeError: unhashable type: 'list'` ao tentar utilizar identificadores de sensores extraídos de um fatiamento de strings (`split`) como chaves de um dicionário e elementos de um conjunto.
* **Solution:** Foi implementada uma lógica de normalização de dados que converte as listas mutáveis resultantes do parser em **Tuplas imutáveis**, garantindo que o valor de *hash* do identificador seja constante durante o ciclo de vida do objeto.
* **Technical Learning:** Compreendi a "física" interna dos dicionários do Python; para que a busca em tempo constante $O(1)$ funcione, a chave deve ser obrigatoriamente imutável. Além disso, validei a importância do **Fail-Fast** ao criar exceções customizadas para barrar anomalias físicas nos dados (ex: 9999.9°C).



### 4. HOW TO REPRODUCE
1.  **Setup do Laboratório:**
    ```bash
    make setup
    ```
    *(Constrói o container e gera o log de 10k linhas ruidosas via bootstrap)*

2.  **Execução da Missão:**
    ```bash
    make run
    ```
    *(Processa o fluxo, limpa os dados e exibe o relatório final de picos de temperatura)*

3.  **Verificação de Sanidade (Tests):**
    ```bash
    make test
    ```
    *(Roda os asserts de prova de imutabilidade e valida se o sistema bloqueia anomalias corretamente)*

---
