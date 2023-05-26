years=int(input())

while True:
    years+=1
    years_str=str(years)
    set_value=set(years_str)
    len_set=len(set(years_str))
    if len(set(years_str))==len(years_str):
        break
print(years)