# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:04:04 2019

@author: Felipe
"""
from acao_com_mouse import AcaoComMouse

class MoverParaDireita(AcaoComMouse):
    
    def __init__(self, controlador_de_velocidade):
        AcaoComMouse.__init__(self, controlador_de_velocidade)
            
    def executarAcao(self):
        print("Movendo para a direita")
        self.pyautogui.moveRel(self.DISTANCIA_PADRAO_DE_MOVIMENTO, 0, self._controlador_de_velocidade.demoraAtual)