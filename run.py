from leap_year import find_leap_year

year = int(input("Digite um ano: "))
if find_leap_year(year):
    print("O ano {} é bissexto!".format(year))
else:
    print("O ano {} não é bissexto!".format(year))