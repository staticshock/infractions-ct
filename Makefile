all:
	./scripts/parse.py --costs ./infractions.txt > costs.json
	./scripts/parse.py --descriptions ./infractions.txt > descriptions.json
