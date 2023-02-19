import os

# Dicionário que mapeia cada palavra correta a uma lista de palavras incorretas que podem ser corrigidas para a palavra correta
corrections = {}

# Dicionário que mapeia cada palavra correta já corrigida
correct_words = {}


# Função para limpar a tela do terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para adicionar uma correção ao dicionário 'corrections'
def add_correction(correct_word, wrong_word):
    if correct_word not in corrections:
        corrections[correct_word] = [wrong_word]
    else:
        corrections[correct_word] += [wrong_word]

# Função que verifica se a palavra 'error' pode ser corrigida e retorna a palavra correta, caso exista
def correct_error(error):
    for correct_word, wrong_words in corrections.items():
        if error in wrong_words:
            return correct_word


# Esta função carrega um banco de palavras a partir de um arquivo txt
def load_word_database(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                correct_word, wrong_words_str = line.split(':')
                wrong_words = [w.strip() for w in wrong_words_str.split(',')]
                for wrong_word in wrong_words:
                    add_correction(correct_word, wrong_word)


# Carrega as correções do banco de dados de palavras
load_word_database('word_database.txt')

# Loop principal
while True:
    print('-' * 20)
    print('''
[1] Para adicionar mais erros à palavras corretas
[2] Corrigir uma frase que contenha erros
[3] Verificar a escrita de algo
[4] Limpar tela
[5] Sair
''')
    
    # Lê a opção escolhida pelo usuário
    menu_option = input('Selecione uma opção: ').lower()

    # Limpa a tela do terminal
    if menu_option == "4":
        clear_screen()

    # Adiciona uma correção ao dicionário 'corrections'
    if '1' in menu_option:
        print('-' * 20)
        print(' ' * 20)
        correct_word = input('Diga a palavra correta: ').lower()
        wrong_word = input('Diga a palavra errada: ').lower()
        add_correction(correct_word, wrong_word)
        print(corrections)
        print(' ' * 20)
    
    # Corrige uma frase que contém erros
    if '2' in menu_option:
        print('-' * 20)
        print(' ' * 20)
        frase = input('Digite sua frase: ').lower()
        words = frase.split()
        corrected_words = []
        for word in words:
            if word not in correct_words:
                if len(word) >= 2:
                    corrected_word = correct_error(word)
                    if corrected_word:
                        corrected_words.append(corrected_word)
                    else:
                        corrected_words.append(word)
                else:
                    corrected_words.append(word)
            else:
                corrected_words.append(word)
        print(' ' * 20)
        print(f"Correção: {' '.join(corrected_words)}")
        print(' ' * 20)

    # Verifica se uma palavra pode ser corrigida e imprime a correção, se existir
    if '3' in menu_option:
        print('-' * 20)
        print(' ' * 20)
        word_verify = input('Digite a palavra que deseja verificar: ').lower()
        correct_word = correct_error(word_verify)
        if correct_word:
            print(f'A frase corrreta é: {correct_word}')
        print(' ' * 20)
    
    # Sai do loop principal
    if '5' in menu_option:
        print(' ' * 20)
        print('Até logo!')
        print(' ' * 20)
        break
