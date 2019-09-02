import pyautogui

# Essa variavel define o intervalo entre os movimentos do mouse (pyautogui)
pyautogui.PAUSE = 0.0

class AcaoComMouse:
    
    def __init__(self, controlador_de_velocidade):
        #Por padrao as acoes sao continuas, ou seja, sao executadas num loop e podem ser canceladas
        self.ehAcaoContinua = True
        self.DISTANCIA_PADRAO_DE_MOVIMENTO = 10
        self._controlador_de_velocidade = controlador_de_velocidade
        self.pyautogui = pyautogui
        self.deveSerCancelada = False
        
    def cancelar(self):
        self.deveSerCancelada = True
        
    def iniciar(self):
        self.deveSerCancelada = False
        if (self.ehAcaoContinua):
            while self.deveSerCancelada != True:
                self.executarAcao()
        else:
            self.executarAcao()
            
    def executarAcao(self):
        print("Acao nulla")
        
    

