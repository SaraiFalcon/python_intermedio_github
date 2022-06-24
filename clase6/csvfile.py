#manipular archivos csv

with open('console_games.csv', 'r') as csv_file:
    print(csv_file.readline()) 

    for line in csv_file.readlines():
        print(line)
    
    #print(len(csv_file.readlines())) Solo sale cuando se comenta las 3 lineas de arriba