#colonne da selezionare da tennis
match_attributes = ['tourney_id', 'match_id', 'winner_id',
                    'loser_id','score', 'best_of', 
                    'round', 'minutes','w_ace', 
                    'w_df', 'w_svpt', 'w_1stIn', 
                    'w_1stWon', 'w_2ndWon', 'w_SvGms', 
                    'w_bpSaved', 'w_bpFaced', 'l_ace', 
                    'l_df', 'l_svpt', 'l_1stIn', 
                    'l_1stWon', 'l_2ndWon', 'l_SvGms', 
                    'l_bpSaved','l_bpFaced', 'winner_rank', 
                    'winner_rank_points', 'loser_rank', 'loser_rank_points', 
                    'winner_name', 'loser_name']

tennis = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv", 'r')
match_output = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\match.csv", 'w')

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


# --- Creo match ---
tennis = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv", 'r')

match_id = [] #lista in cui inserirò i match_id formati da match_num + tourney_id

tokens = []
concat = ''
first=True
for row in tennis.readlines():
    tokens = row.strip().split(',')
    if first: #salto l'header
        first=False
    else:
        concat = tokens[index['match_num']] + '/' + tokens[index['tourney_id']] #concateno match_num con il tourney_id corrispondente e aggiungo anche il level per rendere tourney_id univoco
        match_id.append(concat) 
    
tennis.close()

        
# Uso match_attributes per indicare da quale colonna prendere i valori 
tennis = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv", 'r')

first = True 
i=0 
for row in tennis.readlines():
    tokens = row.strip().split(',')
    if first: #scrivo l'header
        new_line = ''
        for attr in match_attributes:
            new_line += attr+','
        new_line = new_line[:-1] + '\n' #sostituisco l'ultima virgola con \n per terminare la riga
        match_output.write(new_line)
        first = False
    else: #scrivo i dati 
        new_line = ''
        for attr in match_attributes: #seleziono solo i tokens che mi interessano per formare la new_line da scrivere nel file
            if attr == "tourney_id": 
                new_line += tokens[index['tourney_id']] + '/' + tokens[index['tourney_level']] + '/' + tokens[index['tourney_name']].lower() + ',' #concateno tourney_id con il level e il nome del torneo corrispondente per rendere tourney_id univoco
            elif attr == "match_id":
                new_line += match_id[i] + ',' #itero nella lista match_id per aggiungerlo alla riga che sto creando
                i+=1
            else:
                new_line += tokens[index[attr]] + ','
        new_line = new_line[:-1] + '\n' #sostituisco l'ultima virgola con \n per terminare la riga
        match_output.write(new_line)

tennis.close()
match_output.close()
        
# --- Elimino le righe duplicate ---
match = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\match.csv','r')
match_finale = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\match_finale.csv','w',newline='')

seen = set() 
errori = set()
duplicati = set()
for row in match.readlines(): #leggo match per controllare se ci sono id duplicati
    tokens = row.strip().split(',') 
    if tokens[1] not in seen: #se ho già incontraro il match_id (tokens[1]) corrente salto la riga
        seen.add(tokens[1])
        duplicati.add(tuple(tokens)) #aggiungo tutta la riga per un controllo futuro
        match_finale.write(row)
    else:
        if tuple(tokens) not in duplicati: #se la riga è presente in "duplicati" vuol dire che è un duplicato identico di una riga già visitata
            errori.add(tuple(tokens)) #qui inserisco solo le righe che hanno match_id uguale ad una o più righe, ma con gli altri valori diversi

#print(len(errori))

match.close()
match_finale.close()

#Aggiungo i match con match_id duplicati ma valori della riga diversi
match_finale = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\match_finale.csv','a')

#Modifico il match_id aggiungendo un numero intero incrementale alla fine
count=0
for row in errori:
    new_line = ''
    for i in range(len(row)): #itero per ogni valore della riga, per modificare il match_id
        if i==1: #Se raggiungiamo la posizione di match_id
            new_line += row[1]+ '/' + str(count) + ',' #aggiungo un numero al vecchio match_id
            count+=1
        else:
            new_line += row[i] + ','
    new_line = new_line[:-1] + '\n'
    match_finale.write(new_line)

match_finale.close()



















