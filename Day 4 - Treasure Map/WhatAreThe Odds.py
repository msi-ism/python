import random

minutesinday = 24 * 60

possiblehours = [["01:"], ["02:"], ["03:"], ["04:"], ["05:"], ["06:"], ["07:"], ["08:"], ["09:"], ["10:"], ["11:"], ["12:"]]
possibleminute1 = ["0", "1", "2", "3", "4", "5"]
possibleminute2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

end_rangehour = len(possiblehours) - 1
randomhour = random.randint(0, end_rangehour)

end_rangemin1 = len(possibleminute1) - 1
randommin1 = random.randint(0, end_rangemin1)

end_rangemin2= len(possibleminute2) - 1
randommin2 = random.randint(0, end_rangemin2)

random_hour_true = (", ".join(possiblehours[randomhour]))

hour_check = possiblehours[randomhour][0][1]
minute_check = possibleminute2[randommin2]
middle_minute_check = possibleminute1[randommin1]

randomtime = str(randomhour) + str(randommin1) + str(randommin2)

print(f"{random_hour_true}{str(randommin1)}{str(randommin2)}")

if hour_check == minute_check:
    print("This is a synchronicity.")
elif hour_check == minute_check and hour_check == middle_minute_check:
    print("This is a true synchronicity.")
else:
    print("This is not a synchronicity.")
    
print(randommin1)
  