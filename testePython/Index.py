import pyautogui
import time

# Função para localizar e clicar em uma imagem
def localizar_e_clicar(imagem, confidence=0.7, descricao="Imagem"):
    try:
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=confidence)
        if posicao is not None:
            pyautogui.click(posicao.x, posicao.y)
            print(f"{descricao} encontrada e clicada.")
            return True
        else:
            print(f"{descricao} não encontrada.")
            return False
    except Exception as e:
        print(f"Erro ao localizar {descricao}: {e}")
        return False

# Loop principal
procurar = True

while procurar:
    try:
        # Espera antes de cada iteração
        time.sleep(50)

        # Tenta localizar e clicar nas imagens
        if localizar_e_clicar('claim.png', confidence=0.7, descricao="Primeira imagem (claim)"):
            time.sleep(1)
            localizar_e_clicar('fechar.png', confidence=0.6, descricao="Segunda imagem (fechar)")
            time.sleep(2)
            localizar_e_clicar('farmar.png', confidence=0.7, descricao="Terceira imagem (farmar)")

        # Espera antes da próxima iteração
        time.sleep(30)

    except KeyboardInterrupt:
        # Permite sair do loop pressionando Ctrl+C
        print("Execução interrompida pelo usuário.")
        procurar = False
    except Exception as e:
        # Lida com outros erros
        print(f"Ocorreu um erro inesperado: {e}")
        time.sleep(1)
