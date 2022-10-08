import os
import tempfile
import subprocess
from IPython.display import Audio

def synthesize(score):
    with tempfile.TemporaryDirectory() as dir_name:
        midi_file = os.path.join(dir_name, 'temp.mid')
        out_file = os.path.join(dir_name, 'temp.wav')
        
        score.write('midi', fp=midi_file)

        popen = subprocess.Popen(
            ['fluidsynth', '-T', 'wav', '-F', out_file, '-ni', midi_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8"
        )

        stdout, stderr = popen.communicate()    
        if popen.returncode:
            raise Exception(stderr.strip())

        return Audio(out_file)

def show(score):
    display(synthesize(score))
    score.show()
