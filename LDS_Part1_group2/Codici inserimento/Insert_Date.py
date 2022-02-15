import pyodbc
import csv

# Credenziali di accesso per la stringa di connessione
server = 'tcp:131.114.72.230'
database = "Group_2_DB"
username = "Group_2"
password = "ROJQAAGH"

connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()

file = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle da inserire\date.csv", 'r')
csv_file = csv.DictReader(file, delimiter = ",")

# Query di inserimento
sql = "INSERT INTO Date(date_id,day,month,year,quarter) VALUES (?,?,?,?,?)"
i=1
for row in csv_file: # inserisco riga per riga
    val = (row["date_id"], row["day"], row["month"], row["year"], row["quarter"])
    cursor.execute(sql, val)
    print("Inserimento row %d" %i) # Tengo traccia di quale riga è stata inserita fin'ora
    i=i+1

file.close()
cnxn.commit()
cursor.close()
cnxn.close()

print("Connection closed.") 