import praw
import os


def obtener_historias(subreddit, limite=10):
    reddit = praw.Reddit(
        client_id='EAhNUcnGpSMx9U4r_lz8yA',
        client_secret='gHbSkcy4tKIh-UyvCKReThSP2y8SAw',
        user_agent='story_teller'
    )
    
    historias = []
    for post in reddit.subreddit(subreddit).hot(limit=limite):
        if not post.stickied:
            historias.append(post.title + '\n' + post.selftext)
    
    return historias

def guardar_historias(historias, subreddit):
    carpeta_salida = "historias"
    os.makedirs(carpeta_salida, exist_ok=True)
    archivo_salida = os.path.join(carpeta_salida, f"{subreddit}.txt")
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for i, historia in enumerate(historias, 1):
            f.write(f"Historia {i}:\n{historia}\n{'-'*40}\n")
    
    print(f"Historias guardadas en {archivo_salida}")
