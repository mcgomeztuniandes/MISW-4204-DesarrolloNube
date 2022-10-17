from pydub import AudioSegment


class ConversorMP3:
    def convert_audio_to_mp3(self, filepath:str,output_file:str, format:str):
        try: 
            if format == '.ogg':
                sound = AudioSegment.from_ogg(filepath)
            if format == '.wav':
                sound = AudioSegment.from_wav(filepath)
        
            sound.export(output_file, format='mp3')
            print('Se proceso el archivo: ',output_file)
            return True
        except:
            print('Error al procesar el archivo: ',output_file)
            return False
        