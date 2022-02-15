import csv

#colonne che devo selezionare da tennis
campi_tourn=['tourney_id','date_id','tourney_name','surface','draw_size','tourney_level','tourney_spectators','tourney_revenue']

tournament_open = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\tournament.csv','w', newline='')
tournament=csv.DictWriter(tournament_open, fieldnames=campi_tourn, delimiter=",") #creo tournament come dizionario
tournament.writeheader() #scrivo l'header di tournament


tennis_open=open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv','r')
tennis=csv.DictReader(tennis_open, delimiter=",") #apro tennis come dizionario 

for line in tennis: #leggo tennis
    if line["tourney_id"] != "": #scrivo la riga solo se l'id non è missing
        #scrivo la riga accedendo ai valori immagazzinati nel dizionario tennis
        #concateno il tourney_id con il livello e il nome del torneo (il nome lo inserisco tutto minuscolo per evitare problemi di case sensitivity)
        tournament.writerow({"tourney_id": line["tourney_id"]+ '/' + line["tourney_level"] + '/' + line['tourney_name'].lower(),
                             "date_id": line["tourney_date"],
                             "tourney_name": line["tourney_name"],
                             "surface": line["surface"],
                             "draw_size": line["draw_size"], 
                             "tourney_level": line["tourney_level"] , 
                             'tourney_spectators': line["tourney_spectators"],
                             'tourney_revenue': float(line["tourney_revenue"])})

tennis_open.close()
tournament_open.close()

# --- Eliminio righe duplicate ---
tournament = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\tournament.csv','r')
tournament_finale = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\tournament_finale.csv','w',newline='')

seen = set() 
for row in tournament.readlines(): #leggo tournament per controllare se ci sono id duplicati
    tokens = row.strip().split(',')
    if tokens[0] not in seen: #se ho già incontraro il tourney_id corrente salto la riga
        seen.add(tokens[0]) #tokens[0] è il tourney_id
        tournament_finale.write(row) 

tournament.close()
tournament_finale.close()

 


