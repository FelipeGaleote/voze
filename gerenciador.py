from threading import Thread
from mover_para_esquerda import MoverParaEsquerda
from mover_para_direita import MoverParaDireita
from mover_para_baixo import MoverParaBaixo
from mover_para_cima import MoverParaCima
from clique import Clique
from descer import Descer
from subir import Subir
from controlador_de_velocidade import ControladorDeVelocidade
from acao_com_mouse import AcaoComMouse
import os
import speech_recognition as sr
from pocketsphinx import LiveSpeech, get_model_path
import time
import shutil


linguagem = 'pt-BR'

controlador_de_velocidade = ControladorDeVelocidade()

acao = AcaoComMouse(controlador_de_velocidade)

def iniciar_acao(acao):
    thread_acao = Thread(target=acao.iniciar)
    thread_acao.setDaemon(True)
    thread_acao.start()

def ehEsquerda(palavra):
    if ("esquerda" in palavra):
        return True
    else:
        return False
    
def ehDireita(palavra):
    if ("direita" in palavra):
        return True
    else:
        return False
    
def ehCima(palavra):
    if ("cima" in palavra):
        return True
    else:
        return False
    
def ehBaixo(palavra):
    if ("baixo" in palavra):
        return True
    else:
        return False
    
def ehClique(palavra):
    if ("clique" in palavra):
        return True
    else:
        return False
    
def ehAumentar(palavra):
    if ("aumentar" in palavra):
        return True
    else:
        return False
    
def ehReduzir(palavra):
    if ("reduzir" in palavra):
        return True
    else:
        return False
    
def ehParar(palavra):
    if ("pausa" in palavra):
        return True
    else:
        return False
    
def ehDesce(palavra):
    if ("desce" in palavra):
        return True
    else:
        return False
    
def ehSobe(palavra):
    if ("sobe" in palavra):
        return True
    else:
        return False
    

def processar_palavra(palavra):
    global acao
    if ehReduzir(palavra):
        controlador_de_velocidade.desacelerar()
    elif ehAumentar(palavra):
        controlador_de_velocidade.acelerar()
    elif ehClique(palavra):
        acao.cancelar()
        acao = Clique(controlador_de_velocidade)
        acao.iniciar()
    elif ehEsquerda(palavra):
        acao.cancelar()
        acao = MoverParaEsquerda(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehDireita(palavra):
        acao.cancelar()
        acao = MoverParaDireita(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehBaixo(palavra):
        acao.cancelar()
        acao = MoverParaBaixo(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehSobe(palavra):
        acao.cancelar()
        acao = Subir(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehParar(palavra):
        acao.cancelar()
    elif ehDesce(palavra):
        acao.cancelar()
        acao = Descer(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehCima(palavra):
        acao.cancelar()
        acao = MoverParaCima(controlador_de_velocidade)
        iniciar_acao(acao)
    
    
    
def adicionar_modelos_ao_pocketsphinx(pocketsphinx_data_filepath):
    caminho_voze = os.path.dirname(os.path.realpath(__file__))
    print(os.path.join(caminho_voze, linguagem))
    print(os.path.join(pocketsphinx_data_filepath, linguagem))
    shutil.move(os.path.join(caminho_voze, linguagem), os.path.join(pocketsphinx_data_filepath, linguagem)) 


#Esse metodo funciona bem no Linux e no Windows
def ouvir_microfone():
    keywords = [("esquerda", 0.5), ("direita", 0.5), ("cima", 0.8), ("baixo", 1), ("clique", 0.9),
                ("aumentar", 0.5), ("reduzir", 0.5), ("pausa", 0.5)]
    
    while True:
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            start_timestamp = time.time()
            print("Diga alguma coisa: ")
            
            try:
                audio = microfone.listen(source, phrase_time_limit=2)
                print("Audio capturado " + str(time.time() - start_timestamp))
                palavra = microfone.recognize_sphinx(audio, linguagem, keywords)
                print("Audio traduzido " + str(time.time() - start_timestamp))
                print("Você disse: " + palavra)
                processar_palavra(palavra)
            except Exception as e: 
                if "missing" in str(e.args):
                    diretorio = str(e.args).split("directory: ")[1]
                    diretorio = diretorio.replace("\\\\", "\\")
                    diretorio = diretorio.replace(linguagem, "")
                    diretorio = diretorio.replace("\"", "").replace("'", "").replace(",", "").replace(")", "")
                    adicionar_modelos_ao_pocketsphinx(diretorio)
                else:
                    print(e.args)
                
                #print(e)
                print("Não entendi")
                

#Esse metodo funciona muito bem no Linux mas nao no Windows
def ouvir_microfone_br():
    print("Inicio")
    decoder = LiveSpeech(
            verbose=True,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm='pt-br',
            lm='pt-br.lm.bin',
            dic='cmudict-pt-br.dict'
            )
    decoder.set_kws('keyphrase', 'keyphrase.key')
    decoder.set_search('keyphrase')
    for phrase in decoder:
        print(phrase)
        processar_palavra(str(phrase))
    
#ouvir_microfone_br()
ouvir_microfone()


