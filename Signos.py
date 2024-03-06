def verficador_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return 'Áries', 'Zuko', 'Grifinoria'
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return 'Touro', 'Toph', 'Lufa-Lufa'
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):  
        return 'Gêmeos', 'Aang', 'Corvinal'   
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return 'Câncer', 'Katara', 'Sonserina'
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return 'Leão', 'Azula', 'Grifinória'
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return 'Virgem', 'Sokka', 'Lufa-Lufa'
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return 'Libra', 'Mai', 'Corvinal'
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return 'Escorpião', 'Ty Lee', 'Sonserina'
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return 'Sagitário', 'Iroh', 'Grifinória'
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return 'Capricórnio', 'Ozai', 'Lufa-Lufa'
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return 'Aquário', 'Suki', 'Corvinal'
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return 'Peixes', 'Momo', 'Sonserina'
    else:   
        return 'Data de nascimento inválida', None, None

def main(): 
    dia = int(input('Digite sua data de nascimento (1-31):'))
    mes = int(input('Digite seu mês de nascimento (1-12):'))  
    signo, avatar, casa = verficador_signo(dia, mes)
    if signo != 'Data de nascimento inválida':  
        print("Seu signo do zodíaco é:", signo)
        print("Seu personagem em a Lenda de Aang é:", avatar)
        print("Sua casa em Hogwarts é:", casa)
    else:   
        print(signo) 

if __name__ == '__main__':    
    main()   
        
    