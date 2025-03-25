from reddit import obtener_historias, guardar_historias
from voice import text_to_audio  
from video import create_video_with_narration  
from audio_mixer import mix_audio  
import os 

# Historias a obtener
LIMIT_HISTORIAS = 10

# Rutas de archivos
BACKGROUND_AUDIO_FILE = "/home/isael/proyecto_vid/background_audio/Initiation.mp3"  # Tu archivo de audio de fondo *Elegir el que se desee*
BACKGROUND_VIDEO_FILE = "/home/isael/proyecto_vid/background_videos/Backrooms_(Level 94).mp4"  # Ruta del video de fondo *Elegir el que se desee*
OUTPUT_VIDEO_DIR = "/home/isael/proyecto_vid/OUTPUTS/videos" #Ruta de salida del video

# Función para confirmar la continuación del proceso
def confirmar_continuacion(mensaje):
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == 's'

# Inicio del programa
if __name__ == "__main__":
    subreddit_url = input("Ingrese la URL del subreddit: ")
    if "/r/" in subreddit_url:
        subreddit_name = subreddit_url.split("/")[-2]
    
    # Obtener las historias del subreddit y guardar en un archivo de texto
    historias = obtener_historias(subreddit_name, LIMIT_HISTORIAS)
    guardar_historias(historias, subreddit_name)

    for i, historia in enumerate(historias, 1):
        titulo = historia.get('title', f'Historia {i}')
        contenido = historia.get('content', '')
        print(f"{titulo}:\n{contenido}\n{'-'*40}")

    if not confirmar_continuacion("¿Desea continuar con la generación del archivo de audio?"):
        print("Proceso terminado por el usuario.")
        exit()

    # Generar el archivo de audio con las historias guardadas
    archivo_historias = f"historias/{subreddit_name}.txt"
    generated_audio_file = text_to_audio(archivo_historias)  # Llamar a text_to_audio con el archivo de historias

    if not confirmar_continuacion("¿Desea continuar con la mezcla del audio?"):
        print("Proceso terminado por el usuario.")
        exit()

    # Mezclar el audio generado con el audio de fondo
    mixed_audio_file = mix_audio(generated_audio_file, BACKGROUND_AUDIO_FILE)

    if not confirmar_continuacion("¿Desea continuar con la creación del video?"):
        print("Proceso terminado por el usuario.")
        exit()

    # Definir las rutas de los archivos
    base_name = os.path.splitext(os.path.basename(archivo_historias))[0]
    output_file = os.path.join(OUTPUT_VIDEO_DIR, f"RESULT_{base_name}.mp4")  # El archivo de salida

    # Crear el video con narración
    create_video_with_narration(mixed_audio_file, BACKGROUND_VIDEO_FILE, output_file, start_minute=1)  # Llamar a create_video_with_narration con el audio mezclado
    print(f"El video ha sido guardado como {output_file}")