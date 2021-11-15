from .acao_com_mouse import AcaoComMouse
import time


class Subir(AcaoComMouse):
    
    def __init__(self, controlador_de_velocidade):
        AcaoComMouse.__init__(self, controlador_de_velocidade)
            
    def executarAcao(self):
        print("Subindo")
        self.pyautogui.scroll(1)
        time.sleep(0.01 * self._controlador_de_velocidade.demoraAtual)
