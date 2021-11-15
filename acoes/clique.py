from .acao_com_mouse import AcaoComMouse

class Clique(AcaoComMouse):
    
    def __init__(self, controlador_de_velocidade):
        AcaoComMouse.__init__(self, controlador_de_velocidade)
        self.ehAcaoContinua = False
            
    def executarAcao(self):
        print("Clicando")
        x, y = self.pyautogui.position()
        self.pyautogui.click(x, y)
