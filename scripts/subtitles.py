from moviepy import VideoFileClip, TextClip, CompositeVideoClip
import re
import whisper
import os

# Metodo para agregar subtítulos a un video
def add_subtitles_to_video(video_path, srt_path, output_path):
    def parse_srt(srt_path):
        with open(srt_path, 'r') as f:
            content = f.read()
        entries = re.findall(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)\n\n', content, re.DOTALL)
        
        def to_seconds(timestamp):
            h, m, s_ms = timestamp.split(':')
            s, ms = s_ms.split(',')
            return int(h)*3600 + int(m)*60 + int(s) + int(ms)/1000
        
        subtitles = []
        for _, start, end, text in entries:
            start_t = to_seconds(start)
            end_t = to_seconds(end)
            subtitles.append((start_t, end_t, text.replace('\n', ' ')))
        return subtitles

    video = VideoFileClip(video_path)
    subtitles = parse_srt(srt_path)
    subtitle_clips = []

    font_path = "/home/isael/proyecto_vid/fonts/Bebas_Neue/BebasNeue-Regular.ttf"

    for start_time, end_time, text in subtitles:
        duration = end_time - start_time
        txt_clip = (TextClip(font=font_path, filename="/home/isael/proyecto_vid/OUTPUTS/subs/scarystories.srt", font_size=48, color='white')
                    .with_position('center')
                    .with_start(start_time)
                    .with_duration(duration))
        subtitle_clips.append(txt_clip)

    final_video = CompositeVideoClip([video] + subtitle_clips)
    final_video.write_videofile(output_path, codec='libx264', fps=video.fps)

# Generador de subtítulos en formato SRT
class SRTGenerator:
    def __init__(self, audio_path):
        self.audio_path = audio_path

    def transcribe_with_whisper(self):
        model = whisper.load_model("base")  # Cambia a "small" o "medium" si quieres más precisión
        result = model.transcribe(self.audio_path)
        return result['segments']

    def generate_srt(self, output_srt_path):
        segments = self.transcribe_with_whisper()

        def format_timestamp(seconds):
            millisec = int((seconds - int(seconds)) * 1000)
            h = int(seconds // 3600)
            m = int((seconds % 3600) // 60)
            s = int(seconds % 60)
            return f"{h:02d}:{m:02d}:{s:02d},{millisec:03d}"

        with open(output_srt_path, 'w') as srt_file:
            for i, segment in enumerate(segments, start=1):
                start_time = format_timestamp(segment['start'])
                end_time = format_timestamp(segment['end'])
                text = segment['text'].strip()
                srt_file.write(f"{i}\n{start_time} --> {end_time}\n{text}\n\n")

# Agregar subtítulos a un video
if __name__ == "__main__":
    audio_path = "/home/isael/proyecto_vid/OUTPUTS/audios/scarystories.mp3"
    output_srt_path = "/home/isael/proyecto_vid/OUTPUTS/subs/scarystories.srt"

    srt_gen = SRTGenerator(audio_path)
    srt_gen.generate_srt(output_srt_path)
    print(f"Archivo SRT generado en: {output_srt_path}")

    video_path = "/home/isael/proyecto_vid/OUTPUTS/videos/RESULT_scarystories.mp4"
    srt_path = "/home/isael/proyecto_vid/OUTPUTS/subs/scarystories.srt"
    output_path = "/home/isael/proyecto_vid/OUTPUTS/videos/RESULT_scarystories_with_subtitles.mp4"

    add_subtitles_to_video(video_path, srt_path, output_path)
    print(f"Video generado con subtítulos en: {output_path}")
