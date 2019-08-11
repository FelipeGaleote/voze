import pyautogui

# Essa variavel define o intervalo entre os movimentos do mouse (pyautogui)
pyautogui.PAUSE = 0.1

DISTANCIA_PADRAO_DE_MOVIMENTO = 80

#Constantes que definem a demora para realizar um movimento
DEMORA_BAIXA = 0.3
DEMORA_NORMAL = 0.8
DEMORA_ALTA = 1.2

demoraAtual = DEMORA_NORMAL

def acelerar():
    global demoraAtual
    if(demoraAtual == DEMORA_ALTA):
        demoraAtual = DEMORA_NORMAL
    elif (demoraAtual == DEMORA_NORMAL):
        demoraAtual = DEMORA_BAIXA
        
def desacelerar():
    global demoraAtual
    if(demoraAtual == DEMORA_BAIXA):
        demoraAtual = DEMORA_NORMAL
    elif (demoraAtual == DEMORA_NORMAL):
        demoraAtual = DEMORA_ALTA

def mover_para_esquerda():
    pyautogui.moveRel(-DISTANCIA_PADRAO_DE_MOVIMENTO, 0, demoraAtual)
    
def mover_para_direita():
    pyautogui.moveRel(DISTANCIA_PADRAO_DE_MOVIMENTO, 0, demoraAtual)

def mover_para_cima():
    pyautogui.moveRel(0, -DISTANCIA_PADRAO_DE_MOVIMENTO, demoraAtual)
    
def mover_para_baixo():
    pyautogui.moveRel(0, DISTANCIA_PADRAO_DE_MOVIMENTO, demoraAtual)
    
def mover_para_o_centro():
    x, y = pyautogui.size()
    pyautogui.moveTo( x/2 , y/2 )


#Apenas para testes, simulando comandos que o usuario dara por voz
mover_para_o_centro()
for i in range(3):
    mover_para_esquerda()
    acelerar()
    
mover_para_o_centro()
for i in range(3):
    mover_para_direita()
    desacelerar()

    

    
    

