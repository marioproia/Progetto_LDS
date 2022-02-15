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
while count < 5: # Eseguo il commit un chunk alla volta
    file = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle da inserire\tab da inserire\chunk_tournament\tournament_' + str(count) +'.csv', 'r')
    csv_file = csv.DictReader(file, delimiter = ",")
    
    # Query di inserimento
    sql = "INSERT INTO Tournament(tourney_id, date_id, tourney_name, surface, draw_size, tourney_level, tourney_spectators, tourney_revenue) VALUES (?,?,?,?,?,?,?,?)"
    i=1
    print('--- Inizio file ', count, ' ---')
    for row in csv_file:
        val = (row["tourney_id"], row["date_id"], row["tourney_name"], 
               row["surface"], row["draw_size"], row["tourney_level"], 
               row["tourney_spectators"], row["tourney_revenue"])
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
