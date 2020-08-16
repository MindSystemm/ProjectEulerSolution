sumofsquare = 0
squareofsum = 0
for x in range (1, 101):
    sumofsquare += x*x
    squareofsum+=x

squareofsum = squareofsum*squareofsum
print(sumofsquare)
print(squareofsum)
diff = squareofsum - sumofsquare
print(diff)
