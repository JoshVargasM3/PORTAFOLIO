def drawTree(number):
            #Para dibujar el arbol defines la funcion
        for x in range(number): # range(start, stop, step) 
            #Estableces un loop con 'for' e 'in'
            stars = "*" * x
            blankSpace = " " * (number - x)
            #Colocas las variables usando la logica
        
            print(blankSpace + stars + "*" + stars)
        print(blankSpace * number + "*")
        print(blankSpace * number + "*")
        print(blankSpace * (x) + "***")
        
(drawTree(8))




