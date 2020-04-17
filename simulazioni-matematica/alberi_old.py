import numpy as np
import random as rn
import matplotlib.pyplot as plt
import useful
import os
import math 

os.system('cls')

maxday=int(input('inserire numero di giorni: '))
lbosco=int(input('inserire grandezza del bosco: '))
densita = int(input('inserire la densita di alberi in percentuale:' ))
print('----------------------------------------------------')
must_be_placed = math.floor((densita*lbosco**2)/100)
#newcommet
#set up della griglia
m = np.zeros((lbosco, lbosco))
print('Initializinig Grid Setup')
print('Alberi da piantare:', must_be_placed)
while must_be_placed > 0:
    for y in range(lbosco):
        for x in range(lbosco):
            if rn.randint(0,20) == 0:
                if m[y][x]==1:
                    pass
                else:
                    m[y][x] = 1
                    must_be_placed -=1
print(must_be_placed)

#print initial vaulues
init_count1 = useful.counter(1,m)
init_count0 = useful.counter(0,m)
print('giorno 0:')
print('numero di alberi iniziali: ', init_count1)
print('numero di vuoti iniziali: ', init_count0)
print('rapporto percentuale alberi/caselle: ', (init_count1*100)/(lbosco*lbosco) )

#set random starting point
startpoint_x = rn.randint(0,lbosco-1)
startpoint_y = rn.randint(0,lbosco-1)
starcoord = [startpoint_x,startpoint_y]
print(starcoord)
m[startpoint_y][startpoint_x] = 2

print(m)

#lista per trovare il giorno in cui tutto è 2
complete_days = []

for day in range(1,maxday+1):
    update_coord = []
    
    print('giorno numero:' , day)
    for y in range(lbosco):
        for x in range(lbosco):
            if m[y][x] == 1:
                try:
                    if y-1 < 0:
                        raise IndexError
                    if x-1 < 0:
                        raise IndexError
                    if y == lbosco-1:
                        raise IndexError
                    if x == lbosco-1:
                        raise IndexError
                    if m[y-1][x] == 2:
                        update_coord.append([y,x])
                    if m[y][x+1] == 2:
                        update_coord.append([y,x])
                    if m[y+1][x] == 2:
                        update_coord.append([y,x])
                    if m[y][x-1] == 2:
                        update_coord.append([y,x])
                    if m[y-1][x-1] == 2:
                        update_coord.append([y,x])
                    if m[y-1][x+1] == 2:
                        update_coord.append([y,x])
                    if m[y+1][x-1] == 2:
                        update_coord.append([y,x])
                    if m[y+1][x+1] == 2:
                        update_coord.append([y,x])
                except:
                    if y == 0:
                        if x == 0:
                            if m[y][x+1] == 2:
                                update_coord.append([y,x])
                            if m[y+1][x+1] == 2:
                                update_coord.append([y,x])
                            if m[y+1][x] == 2:
                                update_coord.append([y,x])
                        if x == lbosco-1:
                            if m[y][x-1] == 2:
                                update_coord.append([y,x])
                            if m[y+1][x] == 2:
                                update_coord.append([y,x])
                            if m[y+1][x-1] == 2:
                                update_coord.append([y,x])
                        else:
                            if m[y][x-1] == 2:
                                update_coord.append([y,x])
                            if m[y][x+1] == 2:
                                update_coord.append([y,x])
                            if m[y+1][x] == 2:
                                update_coord.append([y,x])
                            if m[y+1][x-1] ==2:
                                update_coord.append([y,x])
                            if m[y+1][x+1] ==2:
                                update_coord.append([y,x])
                    if x == 0:
                        if y>0:
                            if y == lbosco-1:
                                if m[y-1][x] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x+1] == 2:
                                    update_coord.append([y,x])
                                if m[y][x+1] == 2:
                                    update_coord.append([y,x])
                            else:
                                if m[y-1][x] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x+1] == 2:
                                    update_coord.append([y,x])
                                if m[y][x+1] ==2:
                                    update_coord.append([y,x])
                                if m[y+1][x+1] == 2:
                                    update_coord.append([y,x])
                                if m[y+1][x] == 2:
                                    update_coord.append([y,x])
                    if y == lbosco-1:
                        if x>0:
                            if x == lbosco-1:
                                if m[y-1][x] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x-1] ==2:
                                    update_coord.append([y,x])
                                if m[y][x-1] == 2:
                                    update_coord.append([y,x])
                            else:
                                if m[y][x-1] ==2:
                                    update_coord.append([y,x])
                                if m[y][x+1] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x-1] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x+1] == 2:
                                    update_coord.append([y,x])
                    if x == lbosco-1:
                        if x>0:
                            if y<lbosco-1:
                                if m[y-1][x] == 2:
                                    update_coord.append([y,x])
                                if m[y+1][x] == 2:
                                    update_coord.append([y,x])
                                if m[y][x-1] == 2:
                                    update_coord.append([y,x])
                                if m[y-1][x-1] == 2:
                                    update_coord.append([y,x])
                                if m[y+1][x-1] == 2:
                                    update_coord.append([y,x])

                            
    for i in range(len(update_coord)):
        m[update_coord[i][0], update_coord[i][1]] = 2


    #counter
    counter2 = useful.counter(2,m)
    counter1 = useful.counter(1,m)

    if counter2 == init_count1:
        complete_days.append(day)


    print('caselle con valore 2: ', counter2)
    print('caselle con valore 1: ', counter1)
    plt.plot(day,counter2, 'ro')
    plt.plot(day,counter1, 'bo')

print('---------------------------------')
print('this test is over, stats will be printed below')
try:
    print('Tutti gli alberi sono stati bruciati al giorno:', complete_days[0])        
except:
    print('Non tutti gli alberi si sono bruciati...')
    print('Alberi non bruciati', counter1)
print('percentuale di alberi non bruciati rispetto al totale di alberi: ',(counter1*100)/init_count1, '%')           
plt.show()

