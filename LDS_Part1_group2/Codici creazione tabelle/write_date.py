columns=[5] #tourney_date
date = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\Tabelle assignment\date.csv','w')
tennis = open(r'C:\Users\Mario\Desktop\UniPi\2° anno\1° semestre\Lab\Progetto\Datasets\tennis.csv', 'r')

ymd=set() #set in cui inserire tutti i date_id, così da eliminare i duplicati

first=True
for row in tennis.readlines(): #leggo tennis
    if first: #salto l'header
        first=False
    else:
        tokens = row.strip().split(',')
        ymd.add(tokens[5]) #prendo solo il tourney_date


giorno = []
mese = []
anno = [] 
date_id = []

for el in ymd: #suddivido il tourney_date in giorno, mese, anno 
    date_id.append(el)
    anno.append(el[:4])
    mese.append(el[4:6])
    giorno.append(el[6:])
    #print(el)


quarter = []
for el in mese: #creo il quarter in base al mese 
    if el=="01" or el=="02" or el=="03":
        quarter.append("Quarter-1")
    if el=="04" or el=="05" or el=="06":
        quarter.append("Quarter-2")
    if el=="07" or el=="08" or el=="09":
        quarter.append("Quarter-3")
    if el=="10" or el=="11" or el=="12":
        quarter.append("Quarter-4")  


sep=","
data = list(zip(date_id, giorno, mese, anno, quarter)) #creo una lista di liste in cui ho tutti i date_id con relativi giorno, mese, anno
fine = len(data)
i=0
first = True
while i < fine: #itero per tutta la lista "data"
    newline=''
    if first: #scrivo l'header
        new_line = 'date_id' + sep + 'day' + sep + 'month' + sep + "year" + sep + "quarter" + '\n'
        first = False
    else: #scrivo date_id, giorno, mese, anno, quarter (in quest'ordine)
        new_line = data[i][0] + sep + data[i][1] + sep + data[i][2] + sep + data[i][3] + sep + data[i][4] + '\n'
        i+=1
    date.write(new_line)
    

tennis.close()
date.close()


