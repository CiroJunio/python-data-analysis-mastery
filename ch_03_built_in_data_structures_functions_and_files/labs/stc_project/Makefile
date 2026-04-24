# Comandos de Automação
setup:
	docker compose build
	@echo "Ambiente forjado. Use 'make generate' para criar o caos."

generate:
	docker compose run --rm stc-engine python drivers/log_generator.py

run:
	docker compose run --rm stc-engine python run.py

profile:
	@echo "Monitorando Sinais Vitais (Pressione Ctrl+C para parar)..."
	docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}"

clean:
	docker compose down
	rm -rf data/*.txt
	find . -type d -name "__pycache__" -exec rm -rf {} +