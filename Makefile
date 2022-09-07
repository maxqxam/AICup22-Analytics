all:
	python3 $(SERVER_PATH)


DEBUG_DEBUG_M1:
	python3 $(SERVER_PATH) -p1 $(DEBUG_PATH) -p2 $(DEBUG_PATH)


SERVER_PATH="src/server.py"
DEBUG_PATH="Clients/main.py"

