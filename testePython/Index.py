import pyautogui
import time

procurar = "sim"

while procurar == "sim":
    try:
        time.sleep(5)
        img1 = pyautogui.locateCenterOnScreen('claim.png', confidence=0.7)
        
        if img1 is not None:
            pyautogui.click(img1.x, img1.y)
            print("Primeira imagem encontrada e clicada.")

            time.sleep(2)

            img2 = pyautogui.locateCenterOnScreen('fechar.png', confidence=0.5)

            if img2 is not None:
                pyautogui.click(img2.x, img2.y)
                print("Segunda imagem encontrada e clicada.")
            else:
                print("Segunda imagem não encontrada.")
            
            time.sleep(2)

            img3 = pyautogui.locateCenterOnScreen('farmar.png', confidence=0.4)

            if img3 is not None:
                pyautogui.click(img3.x, img3.y)  
                print("Terceira imagem encontrada e clicada.")
            else:
                print("Terceira imagem não encontrada.")
        else:
            print("Primeira imagem não encontrada.")

        time.sleep(2)

    except Exception as e:
       
        print(f"Ocorreu um erro: {e}")
        time.sleep(1)
