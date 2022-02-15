import pyodbc
import csv

# Credenziali di accesso per la stringa di connessione
server = 'tcp:131.114.72.230'
database="Group_2_DB"
username="Group_2"
password="ROJQAAGH"

connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString) 
cursor = cnxn.cursor()

count = 0
while count < 190: # Eseguo il commit un chunk alla volta
    file = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle da inserire\tab da inserire\chunk_match\match_'+ str(count) +'.csv', 'r')
    csv_file = csv.DictReader(file, delimiter = ",")
    
    # Query di inserimento
    sql = 'INSERT INTO Match(tourney_id, match_id, winner_id, loser_id, score, best_of, round, winner_rank, winner_rank_points, loser_rank, loser_rank_points) VALUES (?,?,?,?,?,?,?,?,?,?,?)'
    i=1
    print('--- Inizio file ', count, ' ---')
    for row in csv_file:
        val = (row["tourney_id"], row['match_id'], row['winner_id'],
               row['loser_id'], row['score'], row['best_of'], 
               row['round'], row['winner_rank'], row['winner_rank_points'], 
               row['loser_rank'], row['loser_rank_points']) 
        cursor.execute(sql, val)
        
        print("Inserimento row ", i) # Tengo traccia di quale riga è stata inserita fin'ora
        i=i+1
    
    file.close()
    cnxn.commit()
    print('Commit file ', count, '\n')
    count+=1

cursor.close()
cnxn.close()
print("Connection closed.")