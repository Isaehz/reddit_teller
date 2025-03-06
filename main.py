from reddit import obtener_historias

if __name__ == "__main__":
    historias = obtener_historias("AskReddit", 3)
    for i, historia in enumerate(historias, 1):
        print(f"Historia {i}:\n{historia}\n{'-'*40}")
