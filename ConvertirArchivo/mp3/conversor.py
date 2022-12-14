from datetime import datetime
import sys
from pydub import AudioSegment
import datetime
import os

class ConversorMP3:
    def convert_audio_to_mp3(self, filepath:str, output_file:str, format:str):
        try: 
            if format == '.ogg':
                sound = AudioSegment.from_ogg(filepath)
            if format == '.wav':
                sound = AudioSegment.from_wav(filepath)
        
            sound.export(output_file, format='mp3')
            print('Se convirtio el archivo: ',output_file, 'hora: ', datetime.datetime.now(), 'archivo original:',filepath, 'tamanio:', str(round(os.path.getsize(filepath)/1024000, 2)) + ' MB')
            sys.stdout.flush()
            return True
        except:
            print('Error al procesar el archivo: ',output_file)
            return False
        