import csv
import os
s = input("Jak masz na imie:  ")

st = open("st.txt", "w")
st.write(s)
st.close()

with open("sts.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["Top Gun", "Ocean's Eleven", "Raport mniejszości"])
    write.writerow(["Titanic", "Ostatni Jedi", "Incepcja"])
    write.writerow(["Pulp Fiction", "Czlowiek w ogniu", "Seksmisja"])

os.path.join("Users", "kagni", "Desktop", "rr.txt",)



siema = open("Users", "kagni", "rr.txt",)
print(siema.read())

