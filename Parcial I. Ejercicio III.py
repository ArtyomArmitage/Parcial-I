#Método con función lambda
def ordenar_diccionario_por_valor1(info):
    new_list=[]
    for key in info:
        value=[key,info[key]]
        new_list.append(value)
    new_list.sort(key=lambda x:x[1])
    return new_list
#Honestamente, no tenía ni idea que se podía utilizar una "key" para .sort
#Intenté resolver esto con otro método, pero no veo otra forma de hacerlo

def main():
    valores={"X":4,"B":2,"Z":5}
    resultado1=ordenar_diccionario_por_valor1(valores)
    print(resultado1)
main()