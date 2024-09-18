color_to_feeling = {"red": "love", "white": "hate", "blue": "relax"}
s1 = {1,2}
print(type(s1))

print(len(color_to_feeling))
del color_to_feeling["red"]
print(color_to_feeling)
print(f"the color red represent {color_to_feeling['red']}")
#print(color_to_feeling["grey"])
color_to_feeling["grey"] = "koala"
print(color_to_feeling["grey"])
color_to_feeling["red"] = "heart"
print(color_to_feeling)

