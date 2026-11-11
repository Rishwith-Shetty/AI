def goal_based_vacuum(position):
    if Room[position] == "Dirty":
        return "Clean the room"
    elif Room["A"] == "Clean" and Room["B"] == "Clean":
        return "Stop"
    else:
        if position == 'A':
            return "move to B"
        else:
            return "move to A"


Room = {'A': 'Dirty', 'B': 'Dirty'}
position = 'A'

action = goal_based_vacuum(position)

while True:
    if action == "Clean the room":
        Room[position] = "Clean"

    elif action == "Stop":
        break

    elif action == "move to A":
        position = 'A'

    elif action == "move to B":
        position = 'B'

    action = goal_based_vacuum(position)

print(f"Room A: {Room['A']}")
print(f"Room B: {Room['B']}")
