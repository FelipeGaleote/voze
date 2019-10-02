from threading import Thread
from mover_para_esquerda import MoverParaEsquerda
from mover_para_direita import MoverParaDireita
from mover_para_baixo import MoverParaBaixo
from mover_para_cima import MoverParaCima
from clique import Clique
from controlador_de_velocidade import ControladorDeVelocidade
from acao_com_mouse import AcaoComMouse
import os
import speech_recognition as sr
from pocketsphinx import LiveSpeech, get_model_path
import time
import Xlib.threaded


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
    
def ehAcelerar(palavra):
    if ("aumentar" in palavra):
        return True
    else:
        return False
    
def ehDesacelerar(palavra):
    if ("reduzir" in palavra):
        return True
    else:
        return False

def processar_palavra(palavra):
    global acao
    if ehEsquerda(palavra):
        acao.cancelar()
        acao = MoverParaEsquerda(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehDireita(palavra):
        acao.cancelar()
        acao = MoverParaDireita(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehCima(palavra):
        acao.cancelar()
        acao = MoverParaCima(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehBaixo(palavra):
        acao.cancelar()
        acao = MoverParaBaixo(controlador_de_velocidade)
        iniciar_acao(acao)
    elif ehClique(palavra):
        acao.cancelar()
        acao = Clique(controlador_de_velocidade)
        acao.iniciar()
    elif ehDesacelerar(palavra):
        controlador_de_velocidade.desacelerar()
    elif ehAcelerar(palavra):
        controlador_de_velocidade.acelerar()

def ouvir_microfone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        while True:
            start_timestamp = time.time()
            print("Diga alguma coisa: ")
            audio = microfone.listen(source)
            try:
                print("Audio capturado " + str(time.time() - start_timestamp))
                palavra = microfone.recognize_sphinx(audio, 'en-US')
                print("Audio traduzido " + str(time.time() - start_timestamp))
                print("Você disse: " + palavra)
                processar_palavra(palavra)
            except:
                print("Não entendi")
                

def ouvir_microfone_br():
    model_path = get_model_path()
    print("Inicio")
    decoder = LiveSpeech(
            verbose=False,
            sampling_rate=8000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(model_path,'pt-br'),
            lm=os.path.join(model_path,'pt-br.lm'),
            dic=os.path.join(model_path,'cmudict-pt-br.dict')
            )
    decoder.set_kws('keyphrase',os.path.join(model_path, 'keyphrase.key'))
    decoder.set_search('keyphrase')
    for phrase in decoder:
        print(phrase)
        processar_palavra(str(phrase))
    
ouvir_microfone_br()
#ouvir_microfone()


