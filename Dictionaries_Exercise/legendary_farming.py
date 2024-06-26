special_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

special_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}

junk_materials = {}
is_crafted = False

while not is_crafted:
    data = input()
    materials = data.split()

    for idx in range(0, len(materials), 2):
        quantity = int(materials[idx])
        material = materials[idx + 1].lower()

        if material in special_materials:
            special_materials[material] += quantity
            if special_materials[material] >= 250:
                special_materials[material] -= 250
                is_crafted = True
                print(f"{special_items[material]} obtained!")
                break

        else:
            if material in junk_materials:
                junk_materials[material] += quantity
            else:
                junk_materials[material] = quantity

for material, count in special_materials.items():
    print(f"{material}: {count}")
for material, count in junk_materials.items():
    print(f"{material}: {count}")