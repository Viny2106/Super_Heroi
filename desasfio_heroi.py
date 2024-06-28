
nivel_1 = "Radiante"
nivel_2 = "Imortal"
nivel_3 = "Ascedente"
nivel_4 = "Platina"
nivel_5 = "Ouro"
nivel_6 = "Prata"
nivel_7 = "Bronze"
nivel_8 = "Ferro"

heroi_1 = "Goku" 
heroi_2 = "Kuririn"
heroi_3 = "Tenshinhan"
heroi_4 = "Piccolo"
heroi_5 = "Gohan"
heroi_6 = "Vegeta"
heroi_7 = "Trunks"
heroi_8 = "Yamcha"
    
menu = """

========== SUPER HERÓIS ==========

[1] Goku 
[2] Kuririn 
[3] Tenshinhan 
[4] Piccolo 
[5] Gohan
[6] Vegeta
[7] Trunks
[8] Yamcha
[0] Sair 

==================================

Escolha uma Opção: """

while True:     
    opcao = input(menu)
      
    if opcao == "1":
        
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
        
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_1} está no nível {nivel_8}")
                
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_1} está no nível {nivel_7}")
                
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_1} está no nível {nivel_6}")
                
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_1} está no nível {nivel_5}")
                
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_1} está no nível {nivel_4}")
                
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_1} está no nível {nivel_3}")
                
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_1} está no nível {nivel_2}")
                
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_1} está no está no nível {nivel_1}")
                
            else: 
                print("XP não Catalogado!")    
                
    if opcao == "2": 
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if  1<= experiencia <= 1000: 
                print(f"O super Herói {heroi_2} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_2} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_2} está no nível {nivel_6}")
                    
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_2} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_2} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_2} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_2} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_2} está no está no nível {nivel_1}")
                     
            else: 
                print("XP não Catalogado!") 

    if opcao == "3":    
                
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_3} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_3} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_3} está no nível {nivel_6}")
                    
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_3} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_3} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_3} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_3} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_3} está no está no nível {nivel_1}") 
            else: 
                print("XP não Catalogado!") 
                
    if opcao == "4": 
                
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_4} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_4} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_4} está no nível {nivel_6}")
                    
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_4} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_4} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_4} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_4} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_4} está no está no nível {nivel_1}")
                    
            else: 
                print("XP não Catalogado!") 
            
    if opcao == "5":
                
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_5} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_5} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_5} está no nível {nivel_6}")
                    
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_5} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_5} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_5} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_5} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_5} está no está no nível {nivel_1}")
                    
            else: 
                print("XP não Catalogado!") 
                
    if opcao == "6":  
                
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_6} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_6} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_6} está no nível {nivel_6}")
                    
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_6} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_6} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_6} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_6} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_6} está no está no nível {nivel_1}")
                    
            else: 
                print("XP não Catalogado!") 

    if opcao == "7":
                
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_7} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_7} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_7} está no nível {nivel_6}")
                    
            elif 6001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_7} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_7} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_7} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_7} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_7} está no está no nível {nivel_1}")
                    
            else: 
                print("XP não Catalogado!") 
            
    if opcao == "8":
                
            experiencia = float(input("Informe a quantidade de XP tem o seu herói? "))
                
            if 1 <= experiencia <= 1000: 
                print(f"O super Herói {heroi_8} está no nível {nivel_8}")
                    
            elif  1001 <= experiencia <= 2000:
                print(f"O super Herói {heroi_8} está no nível {nivel_7}")
                    
            elif 2001 <= experiencia <= 5000:
                print(f"O super Herói {heroi_8} está no nível {nivel_6}")
                    
            elif 5001 <= experiencia <= 7000: 
                print(f"O super Herói {heroi_8} está no nível {nivel_5}")
                    
            elif 7001 <= experiencia <= 8000: 
                print(f"O super Herói {heroi_8} está no nível {nivel_4}")
                    
            elif 8001 <= experiencia <= 9000: 
                print(f"O super Herói {heroi_8} está no nível {nivel_3}")
                    
            elif 9001 <= experiencia <= 10000: 
                print(f"O super Herói {heroi_8} está no nível {nivel_2}")
                    
            elif experiencia >= 10001: 
                print(f"O super Herói {heroi_8} está no nível {nivel_1}")       
              
            else: 
                print("XP não Catalogado!") 
                    
    if opcao == "0": 
                print("Obrigao por compartilhar o XP do seu herói!")
                break 
                
        
                  

   
      
                



    
        
        
        
        

        






