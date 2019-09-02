from threading import Thread
from mover_para_esquerda import MoverParaEsquerda
from mover_para_direita import MoverParaDireita
from mover_para_baixo import MoverParaBaixo
from mover_para_cima import MoverParaCima
from clique import Clique
from controlador_de_velocidade import ControladorDeVelocidade
from acao_com_mouse import AcaoComMouse
import time
from pynput.keyboard import Key, Listener, _win32
import speech_recognition as sr


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
    if ("Click" in palavra or "Clique" in palavra):
        return True
    else:
        return False
    
def ehAcelerar(palavra):
    if ("acelerar" in palavra):
        return True
    else:
        return False
    
def ehDesacelerar(palavra):
    if ("desacelerar" in palavra):
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
            print("Diga alguma coisa: ")
            audio = microfone.listen(source)
            try:
                palavra = microfone.recognize_google(audio,language='pt-BR')
                print("Você disse: " + palavra)
                processar_palavra(palavra)
            except:
                print("Não entendi")

ouvir_microfone()


