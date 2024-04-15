command = input()
players_by_side = {}
side_by_players = {}

while command != "Lumpawaroo":
    if " | " in command:
        force_side, force_user = command.split(" | ")

        if force_side not in players_by_side:
            players_by_side[force_side] = []

        if force_user not in side_by_players:
            side_by_players[force_user] = force_side
            players_by_side[force_side].append(force_user)

    else:
        force_user, force_side = command.split(" -> ")

        if force_side not in players_by_side:
            players_by_side[force_side] = []

        players_by_side[force_side].append(force_user)

        if force_user in side_by_players:
            old_side = side_by_players[force_user]
            players_by_side[old_side].remove(force_user)
            side_by_players[force_user] = force_side

        else:
            side_by_players[force_user] = force_side

        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, members in players_by_side.items():
    if len(members) >= 1:
        print(f"Side: {side}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")
