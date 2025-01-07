star_name=('mercury', 'venus' , 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune')
star=input("pls type the strat of the name of the star")
for name in star_name:
    if name.startswith(star):
        print(name)
        found=True
        break
if not found:
    print("not found")