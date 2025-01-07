star_name=('mercury', 'venus' , 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune')
start=input("type your star ")
for name in star_name:
    if name.startswith(start):
        print(name)
        break
