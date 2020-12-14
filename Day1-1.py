#lancement chronomètre
import time  
start_time = time.time()  

# définition de la liste de valeurs
expected = 2020
exit = False

#récupérer la liste 
with open('input.txt') as f:
    entries_list  = [int(x) for x in f.read().split()]

#récupérer les éléments de la liste 1 par 1 
for entry_1 in entries_list:
    for entry_2 in entries_list:
        result = entry_1 + entry_2
        if result == expected:
            print (entry_1," + ",entry_2)
            exit = True
            break
    if exit == True:
        break

final_result = entry_1*entry_2
print (final_result)


#résultat chronomètre
interval = time.time() - start_time  
print ('Total time in seconds:', round(interval,2))