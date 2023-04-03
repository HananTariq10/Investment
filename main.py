Saving = 50000
total_saving = 0
savings_increase = 0.15
Return = 0.1
Dividend = 0.02
Capital = 0
i = 22

while i != 53:
    Capital = Capital + Saving
    Capital = Capital*1.10
    total_saving = total_saving + Saving
    Saving = Saving * 1.15
    i += 1

print(f"Capital = {round(Capital)}, Capital in inr = {round(Capital*81.97)}, Saving = {round(Saving)}, total saving = {round(total_saving*81.97)},"
      f"investment return = {round(Capital*81.97-total_saving*81.97)}, Age = {i}")
