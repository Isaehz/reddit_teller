from reddit import obtener_historias, guardar_historias

if __name__ == "__main__":
    subreddit_url = input("Ingrese la URL del subreddit: ")
    subreddit = subreddit_url.split("/")[-2] if "/r/" in subreddit_url else subreddit_url
    
    historias = obtener_historias(subreddit, 20)
    guardar_historias(historias, subreddit)

    for i, historia in enumerate(historias, 1):
        print(f"Historia {i}:\n{historia}\n{'-'*40}")
