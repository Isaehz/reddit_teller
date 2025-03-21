from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from pydub import AudioSegment, silence

class Subtitles:
    def __init__(self, video_path, subtitles_file):
        self.video_path = video_path
        self.subtitles_file = subtitles_file

    def detect_silences(self, audio_path, min_silence_len=500, silence_thresh=-30):
        audio = AudioSegment.from_file(audio_path)
        print(f"Duración del audio: {len(audio) / 1000} segundos")
        print(f"Rango de decibeles del audio: {audio.dBFS} dBFS")

        silences = silence.detect_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
        silences = [(start / 1000, end / 1000) for start, end in silences]  # Convertir ms a s

        print("Silencios detectados en detect_silences:")
        for start, end in silences:
            print(f"Inicio: {start}, Fin: {end}")

        return silences

    def parse_subtitles(self, silences):
        subtitles = []
        with open(self.subtitles_file, 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i < len(silences):
                    start_time, end_time = silences[i]
                    subtitles.append((start_time, end_time, line.strip()))
        return subtitles

    def add_subtitles(self, output_path):
        video = VideoFileClip(self.video_path)
        audio_path = self.video_path.replace('.mp4', '.mp3')
        video.audio.write_audiofile(audio_path)
        silences = self.detect_silences(audio_path)

        # Imprimir los silencios detectados para depuración
        print("Silencios detectados:")
        for start, end in silences:
            print(f"Inicio: {start}, Fin: {end}")

        subtitles = self.parse_subtitles(silences)
        subtitle_clips = []

        font_path = "/home/isael/proyecto_vid/fonts/Bebas_Neue/BebasNeue-Regular.ttf"  # Ruta completa a una fuente disponible

        # Imprimir los subtítulos procesados para depuración
        for start_time, end_time, text in subtitles:
         print(f"Subtítulo: {text}, Inicio: {start_time}, Fin: {end_time}")


        for start_time, end_time, text in subtitles:
            subtitle = TextClip(text=text, font=font_path, font_size=48, color='white', bg_color='black')  # Tamaño de fuente 240 (10 veces más grande)
            subtitle = subtitle.with_position('center').with_duration(end_time - start_time).with_start(start_time)  # Alineación al centro
            subtitle_clips.append(subtitle)

        final_video = CompositeVideoClip([video] + subtitle_clips)
        final_video.write_videofile(output_path, codec='libx264', fps=video.fps)

# Example usage
if __name__ == "__main__":
    video_path = "/home/isael/proyecto_vid/OUTPUTS/videos/RESULT_Glitch_in_the_Matrix.mp4"
    subtitles_file = "/home/isael/proyecto_vid/historias/Glitch_in_the_Matrix.txt"
    output_path = "/home/isael/proyecto_vid/OUTPUTS/videos/RESULT_Glitch_in_the_Matrix_with_subtitles.mp4"

    subtitle_adder = Subtitles(video_path, subtitles_file)
    subtitle_adder.add_subtitles(output_path)