gen1 = (x for x in range(5))
gen2 = (x*2 for x in gen1)
gen3 = (x+1 for x in gen2)

print("Chained generator results")

for result in gen3:
    print(result)

    