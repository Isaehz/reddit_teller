import requests
import os

# Tu clave de API de ElevenLabs
api_key = "tu api key"  # Reemplaza con tu clave de API
# ID de la voz que deseas usar (puedes obtenerlo de la respuesta del endpoint de voces)
voice_id = "LgVKhF8NfPN1eYSzWQpW"  # Reemplaza con el voice_id correcto

# Función para convertir texto a audio
def text_to_audio(txt_file):
    try:
        # Leer el archivo de texto
        with open(txt_file, 'r') as file:
            text = file.read()

        # URL de la API de ElevenLabs con el voice_id
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        
        # Datos a enviar en la solicitud
        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2"  # Modelo de voz
        }

        # Cabeceras de la solicitud
        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }

        # Realizar la solicitud POST
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            # Generar el nombre del archivo de salida basado en el nombre del archivo de texto
            base_name = os.path.splitext(os.path.basename(txt_file))[0]
            output_directory = "/home/isael/proyecto_vid/OUTPUTS/audios"
            os.makedirs(output_directory, exist_ok=True)
            output_audio_file = os.path.join(output_directory, f"{base_name}.mp3")
                    
            # Guardar el archivo de audio
            with open(output_audio_file, 'wb') as audio_file:
                audio_file.write(response.content)
            
            print(f"El audio se ha guardado como {output_audio_file}")
            return output_audio_file
        else:
            print(f"Error al generar el audio: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    except FileNotFoundError:
        print(f"El archivo {txt_file} no existe.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None