number_of_pokemon=int(input("Enter how many pokemon are there :   "))
list_of_pockemonPower=[]
for count in range(number_of_pokemon):
    power_of_pokemon=int(input("Enter power of pokemon :   "))
    list_of_pockemonPower.append(power_of_pokemon)
minimum_power=min(list_of_pockemonPower)
maximum_power=max(list_of_pockemonPower)
print("\n\nMinimum power :  ",minimum_power)
print("Maximum power :  ",maximum_power)

left_power=number_of_pokemon-2
powerList=[]
i=1
for count2 in range(left_power):
    pair=[minimum_power,maximum_power-count2]
    powerList.insert(-i,pair)
    i=i+1
powerList.insert(0,[minimum_power,minimum_power])
powerList.insert(-1,[minimum_power,maximum_power])
print("List of power :   ",powerList)
for i in powerList:
    print(i[0],i[1])