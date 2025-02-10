def next_higher_temp(temperaturas):
    days=[]
    for i in range(len(temperaturas)-1):
        position=1
        while position<len(temperaturas)-1:
            if temperaturas[i]<temperaturas[i+position]:
                days.append(position)
                break
            position+=1
    days.append(0)
    print(days)

def main():
    temperaturas=[30,40,35,50]
    result=next_higher_temp(temperaturas)
    return result
main()