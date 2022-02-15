###########################################################################################################
#Male_and_female
print('Inizio male_female')
# ---- Males ----
#scrivo un file per uomini con Name, sex e senza nomi "X X"
males = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\male_players.csv', 'r')
output_males = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\output_male_players.csv', 'w')

errori = ["Unknown", "", '??', 'X', 'Xxxxxxxx', 'Xxxxxxx']
nomi = [] # Lista in cui unisco nomi e cognomi 
for row in males.readlines():
    tokens = row.strip().split(',')
    # Leggo le righe di males e prendo solo i nomi (tokens[0]) e cognomi (tokens[1]) che non sono Unknown, vuoti, X o ??
    if (tokens[0] not in errori) and (tokens[1] not in errori):
        nomi.append(tokens[0]+ ' ' +tokens[1])  
    elif (tokens[0] not in errori) and (tokens[1] in errori):
        nomi.append(tokens[0])
    elif (tokens[0] in errori) and (tokens[1] not in errori):
        nomi.append(tokens[1])  
    
    
new_line = []
first = True
for nome in nomi:
    if first: #Scrivo l'header
        output_males.write('Name' + ',' + 'sex' + '\n')
        first = False
    else: #Scrivo sul file i nomi maschili insieme al sesso M in una nuova colonna
        new_line = nome + ',' + 'M' + '\n'
        output_males.write(new_line)

males.close()
output_males.close()


# ---- Females ----
#scrivo un file per le donne con Name,sex e senza nomi "X X"
females = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\female_players.csv', 'r')
output_females = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\output_female_players.csv', 'w')

nomi = []
for row in females.readlines():
    tokens = row.strip().split(',')
    # Leggo le righe di females e prendo solo i nomi (tokens[0]) e cognomi (tokens[1]) che non sono Unknown, vuoti, X o ??
    if (tokens[0] not in errori) and (tokens[1] not in errori):
        nomi.append(tokens[0]+ ' ' +tokens[1]) 
    elif (tokens[0] not in errori) and (tokens[1] in errori):
        nomi.append(tokens[0])
    elif (tokens[0] in errori) and (tokens[1] not in errori):
        nomi.append(tokens[1])  


new_line = []
first = True
for nome in nomi:
    if first: #scrivo l'header
        output_females.write('Name' + ',' + 'sex' + '\n')
        first = False
    else: #Scrivo sul file i nomi femminili insieme al sesso F in una nuova colonna
        new_line = nome + ',' + 'F' + '\n'
        output_females.write(new_line)

females.close()
output_females.close()

print('Fine male_female\n')



###########################################################################################################
#write_people
print('Inizio write_people')
tennis = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv')
males = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\output_male_players.csv')
females = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\output_female_players.csv')

players = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\people.csv', 'w')

# --- Ottengo le posizioni degli attributi in tennis --- 
tokens = []
for row in tennis.readlines():
    tokens = row.strip().split(',') #ottengo solo i nomi delle colonne di tennis
    break

tennis.close()

index = dict()
pos = 0    
for el in tokens:
    index[el] = pos #Creo un index con chiave il nome della colonna e come valore la posizione della stessa
    pos+=1

print(index) #tramite questo index posso accedere direttamente alla colonna senza cercare la sua posizione manualmente


people = dict() #dizionario in cui inserisco nome e relativo sex

# --- Scrivo i maschi senza duplicati ---
records1 = set()
maschi = set()
first = True
for row in males.readlines():
    if first: #salto l'header
        first = False
    else:
        tokens = row.strip().split(',')
        if tuple(tokens) not in records1: 
            records1.add(tuple(tokens))
            maschi.add(tokens[0]) #tokens[0] = nome
        
# --- Scrivo le femmine senza duplicati ---
records2 = set()
femmine = set()
first = True
for row in females.readlines():
    if first: #salto l'header
        first=False
    else:
        tokens = row.strip().split(',')
        if tuple(tokens) not in records2:
            records2.add(tuple(tokens))
            femmine.add(tokens[0]) #tokens[0] = nome
            
males.close()
females.close()


#Controllo persone che sono sia in maschi che femmine
common = maschi.intersection(femmine)


#Scrivo prima i maschi che non si trovano anche tra le femmine
first = True 
for item in (records1-common): 
    if first: #scrivo l'header
        players.write("name" + ',' + "sex" + '\n')
        first = False
    else: #scrivo tutti i males 
        new_line = item[0] + ',' + item[1] + '\n' #item[0] = name, item[1] = sex 
        players.write(new_line)
        people[item[0]] = item[1]
        
#Scrivo le femmine che non si trovano tra i maschi, a seguire 
for item in (records2-common):
    new_line = item[0] + ',' + item[1] + '\n'
    players.write(new_line)
    people[item[0]] = item[1]

#Per le persone sia in maschi che femmine, cerco il sex in base all'avversario, se presente
tennis = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv")

common_corretti = dict()
righe = tennis.readlines()
for name in common:
    for row in righe:
        tokens = row.strip().split(',')
        if (name == tokens[9]) and (tokens[16] not in common): #Prendo il sex del loser se non è presente in winner
            common_corretti[tokens[9]] = people[tokens[16]]
            break
        elif (name == tokens[16]) and (tokens[9] not in common): #Prendo il sex del winner se non è presente in loser
            common_corretti[tokens[16]] = people[tokens[9]]
            break

tennis.close()
players.close()

#Aggiungo i players corretti in coda al file
players = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\people.csv', 'a')
for key, value in common_corretti.items():
    players.write(key + ',' + value + '\n')
    
players.close()
print('Fine write_people\n')


###########################################################################################################
# Players_finale
print('Inizio write_players')
tennis = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv')

# --- Ottengo le posizioni degli attributi in tennis ---
tokens = []
for row in tennis.readlines():
    tokens = row.strip().split(',') #ottengo solo i nomi delle colonne di tennis
    break

tennis.close()

index = dict()
pos = 0    
for el in tokens:
    index[el] = pos #Creo un index con chiave il nome della colonna e come valore la posizione della stessa
    pos+=1

print(index) #tramite questo index posso accedere direttamente alla colonna senza cercare la sua posizione manualmente


# --- Prendo i valori per winners e losers separatamente ---
tennis = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv')
people = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\people.csv')

# colonne da selezionare, divise per winners e losers 
win_attr = ['winner_id', 'winner_ioc', 'winner_name', 'winner_hand', 'winner_ht', 'winner_age', 'tourney_date']
los_attr = ['loser_id', 'loser_ioc', 'loser_name', 'loser_hand', 'loser_ht', 'loser_age', 'tourney_date']


# Seleziono i dati salvandoli in delle liste per non rileggere tennis più volte
tennis = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv')
    
winners = [] 
losers = []
first = True
for row in tennis.readlines(): #leggo tennis riga per riga
    win_temp = []
    los_temp = []
    if first: #Salto l'header
        first = False
    else:
        tokens = row.strip().split(',')
        
        for attr in win_attr: #dai tokens prendo solo i valori delle colonne di winners
            win_temp.append(tokens[index[attr]]) #formo una riga fatta solo di valori riguardanti i winners
        winners.append(win_temp) #aggiungo la riga appena creata alla lista di righe riguardanti i winners
        
        for attr in los_attr: #dai tokens prendo solo i valori delle colonne di losers
            los_temp.append(tokens[index[attr]]) #formo una riga fatta solo di valori riguardanti i losers
        losers.append(los_temp) #aggiungo la riga appena creata alla lista di righe riguardanti i losers

    
# --- Creo un dizionario con i Nomi come chiavi e relativo Sex come valore, prendendo i valori da "people" ---
people_dict = dict()
first = True
for row in people.readlines(): #leggo people riga per riga
    if first: #salto l'header
        first = False
    else:
        tokens = row.strip().split(',')
        people_dict[tokens[0]] = tokens[1] #creo il dizionario per potere accedere al sesso relativo ad una persona 

    
# --- Scrivo il file Players --- 
players = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\players_finale.csv', 'w')

#scrivo l'header
header = 'player_id' + ',' + 'country_id' + ',' + 'name' + ',' + 'hand' + ',' + 'ht' + ',' + 'byear_of_birth' + ',' + 'sex' + '\n'
players.write(header)


# --- Scrivo prima i winners --- 
winners_visitati = set() 
for row in winners: 
    if row[0] not in winners_visitati: #tengo traccia dei winner che ho già incontrato nelle righe
        winners_visitati.add(row[0])
        
        new_line = '' 
        for el in row[:5]: #mi fermo all'attributo "ht", per poi aggiungere byear e sex manualmente 
            new_line += el + ','
          
        #Aggiungo anno di nascita
        try:
            new_line += str(int(row[6][:4]) - int(float(row[5][:2]))) + ',' #Aggiungo l'anno di nascita
        except:
            new_line += '' + ','
        
        #Aggiungo sex
        try:
            new_line += people_dict[row[2]] + ',' #Uso il dizionario delle persone per mettere il sex in base al name
        except:
            new_line += '' + ','
        
        new_line = new_line[:-1] + '\n'
        players.write(new_line) 
        

    


# --- Scrivo i losers che non sono mai stati winners (evito duplicati) ---
losers_visitati = set()
for row in losers:
    if row[0] not in losers_visitati: #tengo traccia dei losers già incontrati 
        losers_visitati.add(row[0])
        if row[0] not in winners_visitati: 
            new_line = ''
            for el in row[:5]: #mi fermo all'attributo "ht", per poi calcolare byear e sex a parte
                new_line += el + ','
            
            #Aggiungo anno di nascita
            try: #se l'età non è NULL
                new_line += str(int(row[6][:4]) - int(float(row[5][:2]))) + ','
            except: #se l'età è NULL, metto NULL come anno di nascita
                new_line += '' + ','
              
            #Aggiungo sex
            try: #se la persona è presente nel dizionario
                new_line += people_dict[row[2]] + ',' #Uso il dizionario delle persone per mettere il sex in base al name
            except: #se la persona non è presente del dizionario aggiungo NULL come sex
                new_line += '' + ','
                
            new_line = new_line[:-1] + '\n'
            players.write(new_line) 

 
tennis.close()
players.close()


# Correggo un errore in country_id in cui abbiamo ITF anzichè ITA per un giocatore italiano
import pandas as pd
players = pd.read_csv(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\players_finale.csv')

players['country_id'] = players['country_id'].replace("ITF", 'ITA')

players.to_csv(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\players_finale.csv', index = False, header = True)


print('Fine write_players\n')




















