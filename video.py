from moviepy import VideoFileClip, AudioFileClip
import os

# Función para crear un video con la narración
def create_video_with_narration(audio_file, background_video, output_file, start_minute=10):
    try:
        # Cargar el video de fondo
        video = VideoFileClip(background_video)

        # Cargar el archivo de audio generado
        audio = AudioFileClip(audio_file)

        # Convertir el minuto de inicio a segundos
        start_time = start_minute * 60

        # Establecer la duración del video al tiempo del audio
        video_duration = audio.duration  # Duración del audio
        video = video.subclipped(start_time, start_time + video_duration)  # Recorta el video usando subclip

        # Asignar el audio al video
        video = video.with_audio(audio)  # Usar set_audio para asignar el audio

        # Escribir el video final
        video.write_videofile(output_file, codec="libx264", audio_codec="aac")
    except FileNotFoundError:
        print(f"El archivo {audio_file} o {background_video} no existe.")
    except KeyError as e:
        print(f"Error al leer el archivo de audio: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Prueba de la función
#if __name__ == "__main__":
#    output_file = "/home/isael/proyecto_vid/OUTPUTS/Result_nosleep.mp4"
#    audio_file = "/home/isael/proyecto_vid/OUTPUTS/mixed_audios/mixed_nosleep.mp3"
#    background_video = "/home/isael/proyecto_vid/background_videos/Rainy_drive_converted.mp4"
#    create_video_with_narration(audio_file, background_video, output_file, start_minute=0)
#    print(f"El video ha sido guardado como {output_file}")
