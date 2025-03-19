import praw
import os
import random

def obtener_historias(subreddit, limite=10, min_caracteres=50):
    """Obtiene historias de un subreddit con un mínimo de caracteres."""
    reddit = praw.Reddit(
        client_id='EAhNUcnGpSMx9U4r_lz8yA',
        client_secret='gHbSkcy4tKIh-UyvCKReThSP2y8SAw',
        user_agent='story_teller'
    )
    
    historias = []
    for post in reddit.subreddit(subreddit).hot(limit=limite*10):  # Obtener más historias para tener una mejor selección aleatoria
        if len(post.selftext) >= min_caracteres:
            historia = {
                'title': post.title,
                'content': post.selftext
            }
            historias.append(historia)
    
    # Barajar las historias aleatoriamente
    random.shuffle(historias)
    
    # Devolver solo el número de historias solicitado
    return historias[:limite]

def guardar_historias(historias, subreddit):
    """Guarda las historias en un archivo de texto."""
    if not historias:
        print("No se encontraron historias que cumplan con la longitud mínima.")
        return

    carpeta_salida = "historias"
    os.makedirs(carpeta_salida, exist_ok=True)
    archivo_salida = os.path.join(carpeta_salida, f"{subreddit}.txt")
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for i, historia in enumerate(historias, 1):
            f.write(f"{historia['title']}:\n{historia['content']}\n{'-'*40}\n")
    
    print(f"Historias guardadas en {archivo_salida}")