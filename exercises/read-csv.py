import csv  

with open('excercises/Customer.csv', 'r') as file_ptr:
    # dialect = csv.Sniffer().sniff("'Country','Capital City','Latitude','Longitude','Population','Capital Type'")
    # print(vars(dialect))

    data = csv.reader(file_ptr, delimiter = ",")

    columns = next(data)
    print(columns)
    country_index = columns.index("Country")
    population_index = columns.index("Population")

    print(country_index, population_index)

    line_dict = {}
    for line in data:
        line_dict[line[country_index]] = line[population_index]

