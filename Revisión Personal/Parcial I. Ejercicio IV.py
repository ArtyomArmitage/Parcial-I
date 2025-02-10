#La versión que entregué para el parcial sólo funcionaba para el primer ejemplo, esta sí sirve para cualquier caso
#según las restricciones que dieron.
def next_higher_temp(temperaturas):
    days=[]
    for i in range(len(temperaturas)-1):
        position=1
        while position<=len(temperaturas)-1-i:
            if temperaturas[i]<temperaturas[i+position]:
                days.append(position)
                break
            position+=1
            if position==len(temperaturas)-i:
                days.append(0)
    days.append(0)
    return days

def main():
    temperaturas=[2]
    result=next_higher_temp(temperaturas)
    print(result)
main()