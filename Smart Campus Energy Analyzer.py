readings=[]
n=int(input("Enter how many readings you have:"));

# Reading the Energy readings of different buildings
for i in range(n):
    readings.append(int(input(f"Enter Energy reading of building {i+1}:")))

# Categorization based on the values
categorized_data={}
categorized_data["efficient"]=[energy for energy in readings if 0<=energy<=50]
categorized_data["moderate"]=[energy for energy in readings if 51<=energy<=150]
categorized_data["high"]=[energy for energy in readings if energy>150]
categorized_data["invalid"]=[energy for energy in readings if energy<0]

# Total Energy Consumption

total_consumpt=0
for energy in readings:
    if energy>=0:
        total_consumpt=total_consumpt+energy

# Counts
efficient_count = len(categorized_data["efficient"])
moderate_count = len(categorized_data["moderate"])
high_count = len(categorized_data["high"])

# Summarizing the Statistics
if high_count>3:
    result="Overconsumption"

elif total_consumpt>600:
    result="Energy Waste Detected"

elif abs(efficient_count-moderate_count)<=1:
    result="Balanced Usage"

elif efficient_count>moderate_count:
    result="Efficient Campus"

else:
    result="Moderate Usage"

stats=(result,)

# Output

print("Categorized Readings:\n")
print(categorized_data,"\n")
print(f"Total Energy Consumption:{total_consumpt}\n")
print(f"Buildings Count:{len(readings)}\n")
print(f"Efficiency Result:{stats[0]}")