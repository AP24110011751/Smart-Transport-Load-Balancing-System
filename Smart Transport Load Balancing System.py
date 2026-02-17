No_of_packages=int(input("Enter number of packages :"))
packages_list=[]
for i in range(No_of_packages):
 packages_list.append(int((input(f"Enter package weight{i+1} :"))))
print(packages_list)
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]
total_valid=0
for i in range(No_of_packages):
  if packages_list[i]<0:
   invalid_entries.append(packages_list[i])
  elif packages_list[i]>=0 and packages_list[i]<=5:
   very_light.append(packages_list[i])
   total_valid += 1
  elif packages_list[i]>=6 and packages_list[i]<=25:
   normal_load.append(packages_list[i])
   total_valid += 1
  elif packages_list[i]>=26 and packages_list[i]<60:
   heavy_load.append(packages_list[i])
   total_valid += 1
  else:
   overload.append(packages_list[i])
   total_valid += 1
full_name=(input("Enter full name :"))
l=len(full_name)-full_name.count(" ")
PLI=l%3
print("length of the name and PLI value",l,PLI)
affected_weight=0
if PLI==0:
   for i in overload:
    invalid_entries.append(i)
    affected_weight+=1
   overload=[]
elif PLI==1:
 for i in very_light:
  affected_weight += 1
 very_light=[]
elif PLI==2:
 for i in very_light:
  affected_weight += 1
 for i in overload:
  affected_weight += 1
 very_light=[]
 overload=[]
print("valid_weights",total_valid)
print("affected weights due to PLI",affected_weight)
print("\nvery_light weights",very_light,"\nnormal weights",normal_load,"\nheavy weights",heavy_load,"\nover weights",overload,"\ninvalid weights",invalid_entries)


