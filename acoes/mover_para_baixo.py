from .acao_com_mouse import AcaoComMouse

class MoverParaBaixo(AcaoComMouse):
    
    def __init__(self, controlador_de_velocidade):
        AcaoComMouse.__init__(self, controlador_de_velocidade)
            
    def executarAcao(self):
        print("Movendo para baixo")
        self.pyautogui.moveRel(0, self.DISTANCIA_PADRAO_DE_MOVIMENTO, self._controlador_de_velocidade.demoraAtual)
