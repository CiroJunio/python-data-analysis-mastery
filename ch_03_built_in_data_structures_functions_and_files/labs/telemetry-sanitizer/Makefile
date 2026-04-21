# Variáveis
DC = docker compose
EXEC = $(DC) run --rm lab-sanitizer

.PHONY: setup run test clean bootstrap

setup: ## Constrói o ambiente e gera os dados de teste
	$(DC) build
	$(MAKE) bootstrap

bootstrap: ## Gera o arquivo de log com 10k linhas sujas
	$(EXEC) python bootstrap_data.py

run: ## Executa a missão principal (main.py)
	$(EXEC) python main.py

test: ## Executa o Verificador de Sanidade (Asserts)
	$(EXEC) python -m tests.sanity_check

clean: ## Destrói o container, imagens e limpa lixo do Python
	$(DC) down --rmi all --volumes --remove-orphans
	rm -rf **/__pycache__ .pytest_cache data/telemetry.log