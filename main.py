
# %%

PlanszaDoGry = {'7':' ','8':' ','9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' '}

klawiszeGry = []

for key in PlanszaDoGry:
    klawiszeGry.append(key)

def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")

drukujPlansze(PlanszaDoGry)



# %%
PlanszaDoGry = {'7':' ','8':' ','9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' '}

klawiszeGry=[]

for key in PlanszaDoGry:
    klawiszeGry.append(key)

def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")

def gra():

    gracz='X'
    licznik=0

    for i in range(10):
        drukujPlansze(PlanszaDoGry)

        move=input(f'To jest, jest ruch, {gracz}. Wybierz gdzie chcesz postawić znak')
        if PlanszaDoGry[move] == ' ':
            PlanszaDoGry[move] = gracz
            licznik += 1
        else:
            print('Miejsce jest zajęte!!!\n Wybierz inne miejsce')
            continue

        if licznik >= 5:
            if PlanszaDoGry['7']==PlanszaDoGry['8']==PlanszaDoGry['9']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break
    
            elif PlanszaDoGry['4']==PlanszaDoGry['5']==PlanszaDoGry['6']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break

            elif PlanszaDoGry['1']==PlanszaDoGry['2']==PlanszaDoGry['3']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break
    
            elif PlanszaDoGry['7']==PlanszaDoGry['4']==PlanszaDoGry['1']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break
        
            elif PlanszaDoGry['8']==PlanszaDoGry['5'] == PlanszaDoGry['2']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break

            elif PlanszaDoGry['9'] == PlanszaDoGry['6'] == PlanszaDoGry['3']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break
        
            elif PlanszaDoGry['7']== PlanszaDoGry['5'] == PlanszaDoGry['3']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break

            elif PlanszaDoGry['9'] == PlanszaDoGry['5'] == PlanszaDoGry['1']!= ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKoniec gry\n')
                print(f'Wygrał Gracz: {gracz}')
                break
            if licznik == 9:
                print('\nKONIEC GRY!!!\n')
                print('\nJest Remis!!\n')

        if gracz == 'X':
            gracz = 'O'
        else:
            gracz = 'X'
    
    restart = input('Czy chcesz zagrać ponownie?/(t/n')
    if restart == 't' or restart == 'T':
        for key in klawiszeGry:
            PlanszaDoGry[key]=' '
        
        gra()

if __name__=='__main__':
    gra()





# %%
