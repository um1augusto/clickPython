# Automação com PyAutoGUI

Este script utiliza a biblioteca **PyAutoGUI** para automatizar cliques em imagens específicas na tela.

## Como funciona

1. **Primeira Imagem**:
   - O script procura pela imagem `claim.png` na tela.
   - Se encontrada, clica no centro da imagem.

2. **Segunda Imagem**:
   - Após clicar na primeira imagem, espera 2 segundos.
   - Procura pela imagem `fechar.png` e clica no centro, caso encontrada.

3. **Terceira Imagem**:
   - Após a segunda imagem, espera mais 2 segundos.
   - Procura pela imagem `farmar.png` e clica no centro, caso encontrada.

4. **Repetição**:
   - O processo se repete continuamente enquanto a variável `procurar` estiver definida como `"sim"`.

## Dependências

- **Python 3.6+**
- Biblioteca **PyAutoGUI**

### Instalação do PyAutoGUI
Execute o comando abaixo para instalar a biblioteca:
```bash
pip install pyautogui
