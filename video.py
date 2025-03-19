from moviepy import VideoFileClip, AudioFileClip
import os

# Función para crear un video con la narración
def create_video_with_narration(audio_file, background_video, output_file):
    # Cargar el video de fondo
    video = VideoFileClip(background_video)

    # Cargar el archivo de audio generado
    audio = AudioFileClip(audio_file)

    # Establecer la duración del video al tiempo del audio
    video_duration = audio.duration  # Duración del audio
    video = video.subclipped(0, video_duration)  # Recorta el video usando subclip

    # Asignar el audio al video
    video = video.with_audio(audio)  # Usar set_audio para asignar el audio

    # Escribir el video final
    video.write_videofile(output_file, codec="libx264", audio_codec="aac")


# Definir las rutas de los archivos
txt_file = "/home/isael/proyecto_vid/historias/HistoriasDeReddit.txt"  # El archivo de texto con la narración

base_name = os.path.splitext(os.path.basename(txt_file))[0]
audio_file = os.path.join("/home/isael/proyecto_vid/OUTPUTS/audios", f"{base_name}.mp3")  # El archivo de audio generado previamente
output_file = os.path.join("/home/isael/proyecto_vid/OUTPUTS/videos", f"RESULT_{base_name}.mp4")  # El archivo de salida

background_video = "/home/isael/proyecto_vid/background_videos/Rainy_drive_converted.mp4"  # Tu video de fondo *Elegir el que se desee*

# Crear el video con narración
create_video_with_narration(audio_file, background_video, output_file)