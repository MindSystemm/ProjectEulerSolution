palindrome = []
for i in range(100, 1000):
    for j in range(i, 1000):
        produit = i*j
        if str(produit) == str(produit)[::-1]:
            palindrome.append(produit)
palindrome.sort(reverse=True)
print(palindrome[0])
