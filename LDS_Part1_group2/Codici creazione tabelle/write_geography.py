################################################################################################################
# languages 
countries = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\country_list.csv", 'r')
lingue = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\lingue.csv", 'w')

for row in countries.readlines(): #leggo il file in cui è presente il language 
    tokens = row.strip().split(',')
    lingue.write((tokens[1] + ',' + tokens[4] + '\n')) #da countries prendo solo country_name (tokens[1]) e lang_name (tokens[4])
    
    
countries.close()
lingue.close()



################################################################################################################
# write_geography
'''
Geography  (country_ioc, continent, language)
'''

tennis = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv", 'r')
countries = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\countries.csv", 'r')
language = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\lingue.csv", "r")

geography = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\geography.csv', 'w')


lingue = dict()
first = True
for row in language.readlines():
    tokens = row.strip().split(',')
    if first: #salto l'header
        first=False
    else: #creo il dizionario con chiavi i country_name e valore la lingua
        lingue[tokens[0]] = tokens[1] 

language.close()  


first = True
for row in countries.readlines():
    tokens = row.strip().split(',') 
    if first: #Scrivo l'header    
    # tokens[0] -> country_ioc
    # tokens[1] -> country_name
    # tokens[2] -> continent
        geography.write(tokens[0] + ',' + tokens[2] + ',' + 'language' + '\n')
        first = False
    else: #Scrivo i dati correggendo le inconsistenze
        if tokens[1] == "Great Britain" or tokens[1] == "United States of America" or tokens[1] == "New Zeland" or tokens[1] == "Papua New Guinea" or tokens[1] == "Grenada" or tokens[1] == "Bahamas" or tokens[1] == "Mauritius" or tokens[1] == "Samoa" or tokens[1] == "Namibia" or tokens[1] == "Guam" or tokens[1] == "Barbados" or tokens[1] == "Canada":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'English' + '\n')
        elif tokens[1] == "Urugay" or tokens[1] == "Cuba" or tokens[1] == "Dominican Republic":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Spanish' + '\n')
        elif tokens[1] == "North Macedonia":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Macedonian' + '\n')
        elif tokens[1] == "Reunion" or tokens[1] == "Burundi" or tokens[1] == "Haiti" or tokens[1] == "Gabon" or tokens[1] == "Guadeloupe" or tokens[1] == "Cameroon" or tokens[1] == "Madagascar" or tokens[1] == "France":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'French' + '\n')
        elif tokens[1] == "Kosovo":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Serbian' + '\n')
        elif tokens[1] == "Unknown": #Il paese 'Unknown' è Pacific Oceania con codice POC
            geography.write(tokens[0] + ',' + 'Oceania' + ',' + 'Malesian' + '\n')
        elif tokens[1] == "Moldova":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Romenian' + '\n')
        elif tokens[1] == "Cyprus":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Turkish' + '\n')
        elif tokens[1] == "Andorra":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Catalan' + '\n')
        elif tokens[1] == "Russia":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Russian' + '\n')
        elif tokens[1] == "China":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'Chinese' + '\n')
        elif tokens[1] == "Germany":
            geography.write(tokens[0] + ',' + tokens[2] + ',' + 'German' + '\n')
        else:
            geography.write(tokens[0] + ',' + tokens[2] + ',' + lingue[tokens[1]] + '\n')
            
        
tennis.close()
countries.close()
geography.close()


# Prendo i country_codes che sono in players ma che non sono in geography
players = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\players_finale.csv", 'r')
players_ioc = set()
first = True
for row in players.readlines():
    if first: #salto l'header
        first=False
    else:
        tokens = row.strip().split(',')
        players_ioc.add(tokens[1]) #prendo solo il country_ioc del player ma senza duplicati

players.close()

geography = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\geography.csv", 'r')
geo_ioc = set()
first = True
for row in geography.readlines():
    if first:
        first=False
    else:
        tokens = row.strip().split(',')
        geo_ioc.add(tokens[0]) #prendo solo country_ioc ma senza duplicati
        
geography.close()         

sottrazione = players_ioc - geo_ioc #prendo i country_ioc presenti in players ma non presenti in geography

#Appendo manualmente solo i codici mancanti presi da players (ottengo continenti e linguaggi mancanti dal web) 
geography = open(r"C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\geography.csv", 'a')
for ioc in sottrazione: 
    if ioc == 'BEN' or ioc == 'TOG' or ioc == 'COD':
        geography.write(ioc + ',' + 'Africa' + ',' + 'French' + '\n')
        
    elif ioc == 'MRN':
        geography.write(ioc +','+'America'+','+'French'+'\n')
        
    elif ioc == 'LVA':
        geography.write(ioc +','+'Europe'+','+'Latvian'+'\n')
        
    elif ioc == 'ANT' or ioc == 'TTO' or ioc == 'VIN' or ioc== 'BER' or ioc == 'JAM':
        geography.write(ioc + ',' + 'America' + ',' + 'English' + '\n')
        
    elif ioc == 'BAN':
        geography.write(ioc + ',' + 'Asia' + ',' + 'Bangali' + '\n')
        
    elif ioc =='LBN' or ioc == 'SAU' or ioc == 'QAT' or ioc=='SYR' or ioc=='JOR' or ioc == 'UAE':
        geography.write(ioc + ',' + 'Asia' + ',' + 'Arabic' + '\n') 
        
    elif ioc == 'TKM':
        geography.write(ioc +','+'Asia'+','+'Turkmen'+'\n')
        
    elif ioc == 'GHA' or ioc == 'BOT' or ioc == 'ZAM':
        geography.write(ioc +','+'Africa'+','+'English'+'\n') 
        
    elif ioc == 'AZE':
        geography.write(ioc +','+'Asia'+','+'Azerbaijani'+'\n')
        
    elif ioc == 'SMR':
        geography.write(ioc +','+'Europe'+','+'Italian'+'\n')
        
    elif ioc == 'AHO':
        geography.write(ioc +','+'America'+','+'Dutch'+'\n')
        
    elif ioc == 'BRN':
        geography.write(ioc +','+'Asia'+','+'Malay'+'\n')
   
    elif ioc == 'LBA':
        geography.write(ioc +','+'Africa'+','+'Arabic'+'\n')
        
    elif ioc == 'CRI':
        geography.write(ioc +','+'America'+','+'Spanish'+'\n')
        
    elif ioc == 'ERI':
        geography.write(ioc +','+'Africa'+','+'Tigryna'+'\n')
        
    elif ioc == 'BGR':
        geography.write(ioc +','+'Europe'+','+'Bulgarian'+'\n')
        
geography.close()

