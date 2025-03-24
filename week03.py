def duplicate_city(ls):
    result_city = set()

    s = set()

    for city in ls:
        l1 = len(s)

        s.add(city)

        l2 = len(s)

        if l1 == l2:
            result_city.add(city)

    return list(result_city)

cities = ["Suwan", "Hwasung", "Incheon", "Incheon", "Bucheon", "Incheon", "Seoul"]
cities.append("Seoul")
cities.append("Anyang")
cities.append("Incheon")

dups = duplicate_city(cities)

print(cities)
print(dups)