# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:54:21 2019

@author: Felipe
"""
class ControladorDeVelocidade:
    
    def __init__(self):
        self.DEMORA_BAIXA = 0.2
        self.DEMORA_NORMAL = 0.3
        self.DEMORA_ALTA = 1
        self.demoraAtual = self.DEMORA_NORMAL

    def acelerar(self):
        print("Aumentando velocidade! Demora atual: " + str(self.demoraAtual))
        if(self.demoraAtual == self.DEMORA_ALTA):
            self.demoraAtual = self.DEMORA_NORMAL
        elif (self.demoraAtual == self.DEMORA_NORMAL):
            self.demoraAtual = self.DEMORA_BAIXA
        print("Demora diminuida para: " + str(self.demoraAtual))

    def desacelerar(self):
        print("Diminuindo velocidade! Demora atual: " + str(self.demoraAtual))
        if(self.demoraAtual == self.DEMORA_BAIXA):
            self.demoraAtual = self.DEMORA_NORMAL
        elif (self.demoraAtual == self.DEMORA_NORMAL):
            self.demoraAtual = self.DEMORA_ALTA
        print("Demora aumentada para: " + str(self.demoraAtual))