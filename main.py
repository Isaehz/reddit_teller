from reddit import obtener_historias, guardar_historias
from voice import text_to_audio  # Importar la función text_to_audio
from video import create_video_with_narration  # Importar la función create_video_with_narration
from audio_mixer import mix_audio  # Importar la función mix_audio
import os 

LIMIT_HISTORIAS = 1

def confirmar_continuacion(mensaje):
    respuesta = input(f"{mensaje} (s/n): ").strip().lower()
    return respuesta == 's'

if __name__ == "__main__":
    subreddit_url = input("Ingrese la URL del subreddit: ")
    if "/r/" in subreddit_url:
        subreddit_name = subreddit_url.split("/")[-2]
    
<<<<<<< HEAD
=======
    # Obtener las historias del subreddit y guardar en un archivo de texto
>>>>>>> 1e4cabe (Initial commit)
    historias = obtener_historias(subreddit_name, LIMIT_HISTORIAS)
    guardar_historias(historias, subreddit_name)

    for i, historia in enumerate(historias, 1):
        titulo = historia.get('title', f'Historia {i}')
        contenido = historia.get('content', '')
<<<<<<< HEAD
        print(f"{titulo}:\n{contenido}\n{'-'*40}")
=======
        print(f"{titulo}:\n{contenido}\n{'-'*40}")

    if not confirmar_continuacion("¿Desea continuar con la generación del archivo de audio?"):
        print("Proceso terminado por el usuario.")
        exit()

    # Generar el archivo de texto con las historias guardadas
    archivo_historias = f"historias/{subreddit_name}.txt"
    generated_audio_file = text_to_audio(archivo_historias)  # Llamar a text_to_audio con el archivo de historias

    if generated_audio_file:
        if not confirmar_continuacion("¿Desea continuar con la mezcla del audio?"):
            print("Proceso terminado por el usuario.")
            exit()

        # Mezclar el audio generado con el audio de fondo
        background_audio_file = "/home/isael/proyecto_vid/background_audio/Initiation.mp3"
        mixed_audio_file = mix_audio(generated_audio_file, background_audio_file)

        if mixed_audio_file:
            if not confirmar_continuacion("¿Desea continuar con la creación del video?"):
                print("Proceso terminado por el usuario.")
                exit()

            # Definir las rutas de los archivos
            base_name = os.path.splitext(os.path.basename(archivo_historias))[0]
            output_file = os.path.join("/home/isael/proyecto_vid/OUTPUTS/videos", f"RESULT_{base_name}.mp4")  # El archivo de salida

            background_video = "/home/isael/proyecto_vid/background_videos/Night_city.mp4"  # Tu video de fondo *Elegir el que se desee*

            # Crear el video con narración
            create_video_with_narration(mixed_audio_file, background_video, output_file, start_minute=10)  # Llamar a create_video_with_narration con el audio mezclado
            print(f"El video ha sido guardado como {output_file}")
>>>>>>> 1e4cabe (Initial commit)
