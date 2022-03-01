#pip3 install pytube3
#python -m pip install git+https://github.com/nficano/pytube
#pip3 install pydub
#brew install ffmpeg


from pytube import YouTube
from pydub import AudioSegment
import os



def download_yt_mp4(link):
    yt = YouTube(link)
    print("This is the audio we downloading " + yt.title)
    ys = yt.streams.filter(only_audio=True)[0]
    ys.download()
    file = ys.default_filename
    mp4_to_wav(file)
    return file

def mp4_to_wav(file):
    audio = AudioSegment.from_file(file, format="mp4")
    file = file[:-4] + '.wav'
    audio.export(file, format="wav")
    pass

def delete(file):
    os.remove(file)
    pass

def panda():
    print('''
    
                                                       
                                                             -|-_
                                                              | _

                                                             <|/\
                                                              | |,

                                                             |-|-o
                                                             |<|.

                                              _,..._,m,      |,
                                           ,/'      '"";     | |,
                                          /             ".
                                        ,'mmmMMMMmm.      \  -|-_"
                                      _/-"^^^^^"""%#%mm,   ;  | _ o
                                ,m,_,'              "###)  ;,
                               (###%                 \#/  ;##mm.
                                ^#/  __        ___    ;  (######)
                                 ;  //.\\     //.\\   ;   \####/
                                _; (#\"//     \\"/#)  ;  ,/
                               @##\ \##/   =   `"=" ,;mm/
                               `\##>.____,...,____,<####@
                                                     ""'     m1a   
    ''')
    pass
panda()
print('panda downloader v1')
print('\n')
link = input("gimmie youtube link : ")
file = download_yt_mp4(link)
print('cleaning up my mess (finna delete the mp4)')
delete(file)
print('done :) now make a bop!!')








