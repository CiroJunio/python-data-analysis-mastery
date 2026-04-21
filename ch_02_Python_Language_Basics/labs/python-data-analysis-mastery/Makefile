DC = docker compose

.PHONY: setup run clean test

setup: ## Constrói e prepara o ambiente
	touch requirements.txt
	# Adicionando o básico para o capítulo 2: IPython 
	echo "ipython\npytest" > requirements.txt
	$(DC) build

run: ## Entra no IPython interativo
	$(DC) run --rm lab

run-main: ## Para execução de "mercado" (A Fábrica)
	$(DC) run --rm lab python main.py

test: ## Executa os testes de integridade de sinais
	$(DC) run --rm lab python -m pytest tests/

clean: ## Destrói a redoma e limpa o lixo
	$(DC) down --rmi all --volumes --remove-orphans
	find . -type d -name "__pycache__" -exec rm -rf {} +