import os
import csv


# tworzenie ścieżki dostępu do pliku

os.path.join("czesc.txt")

# tworzenie pliku i zapisywanie coś na nim

st = open("czesc.txt", "w")
st.write("czesc")
st.close()

# otwieranie pliku i jego zawartości

with open("czesc.txt", "r") as f:
    print(f.read())

# umieszanie zmian w koontenerze w celu otwierania pliku w programie

my_list = list()
with open("st.txt", "r") as f:
    my_list.append(f.read())

print(my_list)
print(my_list)

#pliki csv

with open("st.csv", "w", newline='') as v:
    write = csv.writer(v, delimiter=",")
    write.writerow(["jeden", "dwa", "trzy"])
    write.writerow(["cztery", "piec", "szesc"])

with open("st.csv", "r") as v:
    r = csv.reader(v, delimiter=",")
    for row in r:
        print(",".join(row))