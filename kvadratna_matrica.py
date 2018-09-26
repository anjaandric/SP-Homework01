n = int(input("Unesite red kvadratne matrice: "))
X = []

glavna_dijagonala = 0
sporedna_dijagonala = 0

prvi_element = 1

for i in range(n):

    X.append([])

    for j in range(n):
        X[i].append(prvi_element)

        if i == j:
            glavna_dijagonala += prvi_element


        if i+j == n-1:
            sporedna_dijagonala += prvi_element

        prvi_element += 1

for i in range(n):
    print(X[i])

print("Zbir elemenata u glavnoj dijagonali je: " + str(glavna_dijagonala))

print('Zbir elemenata u sporednoj dijagonali je: ' + str(sporedna_dijagonala))
