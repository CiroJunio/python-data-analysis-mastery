# Variáveis de atalho
DC = docker compose
SERVICE = fleet-lab

.PHONY: setup run test clean

setup: ## Constrói a imagem e prepara o ambiente
	$(DC) build
	@echo "✅ Ambiente pronto. Use 'make run' para iniciar."

run: ## Executa a orquestração principal (main.py)
	$(DC) run --rm $(SERVICE) python main.py

test: ## Executa o multímetro (sanity_check) para validar a vetorização
	$(DC) run --rm $(SERVICE) python -m tests.sanity_check

clean: ## Destrói containers, imagens e limpa cache do Python
	$(DC) down --rmi all --volumes --remove-orphans
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "🧹 Sistema limpo."