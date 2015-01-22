import collections
population_dict = collections.defaultdict(int)
land_area_dict= collections.defaultdict(int)
density= collections.defaultdict(int)
with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[7] = float(line[7])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]
            land_area_dict[line[0]] += line[7]

for i in population_dict.iterkeys():
    density[i]=land_area_dict[i]/population_dict[i]
    
with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,density\n')

    for k, v in density.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
