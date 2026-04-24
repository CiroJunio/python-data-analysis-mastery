setup:
	docker compose build

run:
	docker compose up engine

# Monitora consumo de RAM e CPU em tempo real
profile:
	docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}\t{{.NetIO}}"

clean:
	docker compose down --rmi all --volumes
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.npy *.npz # Limpa arquivos binários [cite: 1349, 1357]