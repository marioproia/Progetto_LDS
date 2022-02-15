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
while count < 15: # Eseguo il commit un chunk alla volta
    file = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle da inserire\tab da inserire\chunk_players\players_' + str(count) + '.csv', 'r')
    csv_file = csv.DictReader(file, delimiter = ",")
    
    # Query di inserimento
    sql = "INSERT INTO Players(player_id, country_id, name, hand, ht, byear_of_birth, sex) VALUES (?,?,?,?,?,?,?)"
    i=1
    print('--- Inizio scrittura file ', count, ' ---')
    for row in csv_file:
        val = (row["player_id"], row["country_id"], row["name"], row["hand"], row["ht"], row["byear_of_birth"], row["sex"])
        cursor.execute(sql, val)
        print('Inserimento row ', i) # Tengo traccia di quale riga è stata inserita fin'ora
        i=i+1
    
    file.close()
    cnxn.commit()
    print('Commit file ', count, '\n')
    count += 1
    
cursor.close()
cnxn.close()
print("Connection closed.")
