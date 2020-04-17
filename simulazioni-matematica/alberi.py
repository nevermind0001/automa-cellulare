import numpy as np
import random as rn
import matplotlib.pyplot as plt
import useful
import os
import math 
from tqdm import tqdm

os.system('cls')

lbosco=int(input('inserire grandezza del bosco: '))
num_densita = int(input('quante densità vuoi testare: '))


densita = []
for i in range(num_densita):
    x = int(input('Inserire il numero: '))
    densita.append(x)

num_simulazioni = int(input('inserire il numero di simulazioni che si vuole effettuare: '))

input_flag = int(input('inserire 0 per una simulazione silenziosa, 1 per una con log dettagliato: '))
if input_flag == 0:
    verboseprint = lambda *a: None
else:  
    def verboseprint(*args):
        print(*args)


for index_dens in range(len(densita)):
    percentuali = []
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>TESTANDO DENSITA AL:', densita[index_dens], '% <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    for simulazione in tqdm(range(num_simulazioni)):
        #definisce il numero di alberi da piazzare
        must_be_placed = math.floor((densita[index_dens]*lbosco**2)/100)

        #set up della griglia
        m = np.zeros((lbosco, lbosco))
        verboseprint('*******************************************')
        verboseprint('Initializinig Grid Setup')
        verboseprint('Alberi da piantare:', must_be_placed)
        while must_be_placed > 0:
            for y in range(lbosco):
                for x in range(lbosco):
                    if rn.randint(0,20) == 0:
                        if m[y][x]==1:
                            pass
                        else:
                            m[y][x] = 1
                            must_be_placed -=1

        #print initial vaulues
        init_count1 = useful.counter(1,m)
        init_count0 = useful.counter(0,m)
        verboseprint('numero di alberi iniziali: ', init_count1)
        verboseprint('numero di vuoti iniziali: ', init_count0)
        verboseprint('rapporto percentuale alberi/caselle: ', (init_count1*100)/(lbosco*lbosco) )

        #set random starting point
        startpoint_x = rn.randint(0,lbosco-1)
        startpoint_y = rn.randint(0,lbosco-1)
        starcoord = [startpoint_x,startpoint_y]
        verboseprint(starcoord)
        m[startpoint_y][startpoint_x] = 2


        #lista per trovare il giorno in cui tutto è 2
        complete_days = []

        verboseprint('simulating fire :D')
        day = 0
        while True:
            day += 1
            update_coord = []
            
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

            #print('caselle con valore 2: ', counter2)
            #print('caselle con valore 1: ', counter1)

            if len(update_coord) == 0:
                break


        verboseprint('---------------------------------')
        verboseprint('this TEST IS OVER, stats will be printed below')
        try:
            verboseprint('Tutti gli alberi sono stati bruciati al giorno:', complete_days[0])        
        except:
            verboseprint('Non tutti gli alberi si sono bruciati...')
            verboseprint('Alberi non bruciati', counter1)
        verboseprint('percentuale di alberi non bruciati rispetto al totale di alberi: ',(counter1*100)/init_count1, '%')           

        percentuale_bruciati = (counter1*100)/init_count1
        percentuali.append(percentuale_bruciati)



    media = sum(percentuali)/len(percentuali)
    print('media delle percentuali: ',media, '%')
    plt.plot(densita[index_dens],media,'ro')
plt.show()