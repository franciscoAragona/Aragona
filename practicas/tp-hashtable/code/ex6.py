def hashPostal(codigo):
    #yo creo que el m deberia de ser del tamaño de la suma de 4*num+grnde + 4*(caracter con mayor codigo)
    # Convertir el código postal a minúsculas para hacerlo insensible a mayúsculas
    codigo = codigo.lower()

    # Separar los caracteres y los dígitos del código postal
    #recorre el str y guarda los carecteres alfabeticos .isalpha() en una lista
    caracteres = [c for c in codigo if c.isalpha()]
    #recorre el str y guarda los carecteres nemericos .isdigit() en una lista
    digitos = [d for d in codigo if d.isdigit()]
    #suma el cdigo de cada letra
    k1=sum(ord(caracteres[i])-ord("a") for i in range(4))
    #suma cada numero
    k2=sum(int(digitos[i]) for i in range(4))
    return k1+k2
hashPostal("z9999zzz")