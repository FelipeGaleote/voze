import os
import getpass
import urllib.request
import zipfile
import sys

USER_NAME = getpass.getuser()


def module_exists(module_name):
    try:
        if (module_name == "PyAudio"):
            __import__("pyaudio")
        elif (module_name == "SpeechRecognition"):
            __import__("speech_recognition")
        else:
            __import__(module_name)
    except ImportError:
        return False
    else:
        return True


def printOk(module_name):
    print("%s ja esta instalado" % module_name)
    

def instalarModulo(module_name):
    print("%s esta sendo instalado" % module_name)
    os.system("pip3 install %s" % module_name)
    

def instalarModuloPocketSphinx(module_name):
    print("%s esta sendo instalado" % module_name)
    urllib.request.urlretrieve("http://prdownloads.sourceforge.net/swig/swigwin-4.0.1.zip", "swig.zip")
    with zipfile.ZipFile("swig.zip", 'r') as zip_ref:
        swig_path = "C:\\Users\\%s\\AppData\\Roaming\\swigwin-4.0.1" % USER_NAME
        zip_ref.extractall(swig_path)
        new_path = "set PATH=%s;%s" % (os.environ['PATH'], swig_path)
        print(new_path)
        os.system(new_path)
    os.system("python -m pip install --upgrade pip setuptools wheel")
    os.system("pip3 install %s" % module_name)

def instalarModuloPyAudio(module_name):
    print("%s esta sendo instalado" % module_name)
    urllib.request.urlretrieve("https://download.lfd.uci.edu/pythonlibs/g5apjq5m/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl", "PyAudio-0.2.11-cp37-cp37m-win_amd64.whl")
    os.system("pip install %s" % "PyAudio-0.2.11-cp37-cp37m-win_amd64.whl")
    
    
def garantirImportDoModulo(module_name):    
    if( module_exists(module_name)):
        printOk(module_name)
    elif module_name == "pocketsphinx":
        instalarModuloPocketSphinx(module_name)
    elif module_name == "PyAudio":
        instalarModuloPyAudio(module_name)
    else:
        instalarModulo(module_name)

def adicionarAInicializacaoDoWindows():
    print("entrou")
    file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        print(bat_path)
        bat_file.write('python %s\iniciar.py \npause' % file_path)

garantirImportDoModulo("pyautogui")
garantirImportDoModulo("SpeechRecognition")
garantirImportDoModulo("pocketsphinx")
garantirImportDoModulo("PyAudio")
adicionarAInicializacaoDoWindows()
os.system('python %s\gerenciador.py' % os.path.dirname(os.path.realpath(__file__)))

