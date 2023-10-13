def badge_maker(name):
    return (f"Hello, my name is {name}.")

def batch_badge_creator(names):
    badges = []
    for name in names:
        badge = "Hello, my name is " + name + "."
        badges.append(badge)
    return badges

def assign_rooms(names):
    assigned_rooms = []
    room_number = 1
    for name in names :
        speaker_rooms = f"Hello, {name}! You'll be assigned to room {room_number}!"
        assigned_rooms.append(speaker_rooms)
        room_number += 1
        
    return assigned_rooms

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)

# Test the function with a list of names
names = ["Arel", "Carol"]
printer(names)

made_badge = badge_maker("Nat")
print(made_badge)

created_badges = batch_badge_creator(["Nat", "Mae"])
print(created_badges)

assigned_rooms = assign_rooms(["Nat", "Mae"])
print(assigned_rooms)

printer(["Nat", "Mae"])