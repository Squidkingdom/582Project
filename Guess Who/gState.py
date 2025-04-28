# filler file, full comments in Nao and Player Turn response files

gState = [
	["1"] * 8,
	["1"] * 8,
	["1"] * 8
]

characterFeatures =[
[False, True, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, False, False, True, False, False, True], #Amy

[True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, True, True, False, True, False, False, True, False], #Al

[True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True], #Sam

[False,True, False, True, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False], #Sofia 

[False, True, True, False, False, False, False, False, True, False, False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, True], #Olivia

[True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, True, True, False], #Mike

[True, False, False, False, True, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, True, True, True, False], #David

[False, True, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, True, False], #Farah

[True, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, True], # Ben

[True, False, True, False, False, False, False, True, False, False, False, False, True, True, False, False, True, False, False, False, False, False, True, False, True, False], #Jordan

[False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, True, True, False], #Laura

[True, False, False, False, False, True, False, True, False, True, False, False, False, False, False, False, False, False, False, True, False, False, True, True, True, False], #Leo

[False, True, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, True, False, False, True, False, False, True, False, True], #Liz

[False, True, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True], #Mia

[True, False, False, False, True, False, False, True, False, False, False, True, False, False, False, False, True, False, False, False, False, False, True, False, False, True], #Nick

[False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, True, False, True, True, False], #Lily

[True, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, True, False, True, False, False, True, True, True, False], #Jo

[True, False, True, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False], #Gabe

[True, False, True, False, False, False, False, True, False, False, False, True, True, False, False, False, False, False, False, False, True, False, False, False, False, True], #Eric

[False, True, False, False, False, False, True, False, True, False, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, True], #Emma

[False, True, False, False, False, True, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, True, False, True], #Carmen

[True, False, False, False, False, False, True, False, True, True, False, True, False, False, True, False, False, False, True, True, False, True, False, False, False, True], #Daniel

[False, True, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, True, False, False, True, False, False, False, True, False], #Rachel

[False, True, False, False, True, False, False, False, True, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, False, True] #Caity

]

featureToInt = {
"male": 0,
"female": 1,
"black hair": 2,
"hair black": 2,
"brown hair": 3,
"hair brown": 3,
"hair blonde": 4,
"blonde hair": 4,
"white hair": 5,
"hair white": 5,
"orange hair": 6,
"hair orange": 6,
"short hair": 7,
"hair short": 7,
"hair long": 8,
"long hair": 8,
"facial hair": 9,
"bald": 10,
"freckles": 11,
"dyed hair": 12,
"hair dyed": 12,
"braided hair": 13,
"hair braided": 13,
"ponytail": 14,
"headwear": 15,
"earrings": 16,
"glasses": 17,
"beard": 18,
"mustache": 19,
"blue eyes": 20,
"eyes blue": 20,
"green": 21,
"eyes brown": 22,
"brown eyes": 22,
"teeth": 23,
"left": 24,
"right": 25
}

features = [
    'male',          # 0
    'female',        # 1
    'black hair',    # 2
    'brown hair',    # 3
    'hair blonde',   # 4
    'white hair',    # 5
    'orange hair',   # 6
    'short hair',    # 7
    'hair long',     # 8
    'facial hair',   # 9
    'bald',          # 10
    'freckles',      # 11
    'dyed hair',     # 12
    'braided hair',  # 13
    'ponytail',      # 14
    'headwear',      # 15
    'earrings',      # 16
    'glasses',       # 17
    'beard',         # 18
    'mustache',      # 19
    'blue eyes',     # 20
    'green',         # 21
    'eyes brown',    # 22
    'teeth',         # 23
    'left',          # 24
    'right'          # 25
]

name = ["Amy", "Al", "Sam", "Sofia", "Olivia", "Mike", "David", "Farah", "Ben", "Jordan", "Laura", "Leo", "Liz", "Mia", "Nick", "Lily", "Joe", "Gabe", "Eric", "Emma", "Carmen", "Daniel", "Rachel", "Katie"]

def elim(feat: str, ans: bool):
    feat_idx = featureToInt[feat]  # Get the feature index from string

    for i, person in enumerate(characterFeatures):
        if person[feat_idx] != ans:
            row = i // 8/
            col = i % 8
            gState[row][col] = "0"



# for i, character in enumerate(characterFeatures):
# 	print("\n" + name[i] + ":")
# 	for j in range(len(features)):
# 		print(f'{features[j]}={character[j]}')

elim("male", False)

for i, row in enumerate(gState):
    for j, cell in enumerate(row):
        if cell == "0":
            index = i * 8 + j
            print(f"{name[index]} has been eliminated.")


