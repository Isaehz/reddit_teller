from pydub import AudioSegment
import os

# Configurar pydub para usar ffmpeg
AudioSegment.converter = "/usr/bin/ffmpeg"  # Asegúrate de que esta ruta sea correcta

def mix_audio(generated_audio_file, background_audio_file):
    try:
        # Cargar los archivos de audio
        generated_audio = AudioSegment.from_file(generated_audio_file)
        background_audio = AudioSegment.from_file(background_audio_file)

        # Ajustar la duración del audio de fondo para que coincida con el audio generado
        background_audio = background_audio[:len(generated_audio)]

        # Ajustar el volumen del audio de fondo
        background_audio = background_audio   # Reducir el volumen del fondo

        # Mezclar los audios
        mixed_audio = background_audio.overlay(generated_audio)

        # Guardar el audio mezclado
        output_directory = "/home/isael/proyecto_vid/OUTPUTS/mixed_audios"
        os.makedirs(output_directory, exist_ok=True)
        output_mixed_audio_file = os.path.join(output_directory, f"mixed_{os.path.basename(generated_audio_file)}")
        mixed_audio.export(output_mixed_audio_file, format="mp3")

        print(f"El audio mezclado se ha guardado como {output_mixed_audio_file}")
        return output_mixed_audio_file
    except Exception as e:
        print(f"Ocurrió un error al mezclar los audios: {e}")
        return None