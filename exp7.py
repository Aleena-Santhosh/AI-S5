classes = {"CN": ["Agnus", "Bibin"],"TOC": ["Agnus", "Caren"],
    "AGA": ["Bibin", "Deb"],"ML": ["Caren", "Deb"],"ANN": ["Agnus", "Deb"]}
time_slots = ["9:00-10:00","10:00-11:00","11:00-12:00"]
rooms = ["A","B","C"]
room_availability = {
    "A": ["9:00-10:00","10:00-11:00","11:00-12:00"],
    "B": ["9:00-10:00","10:00-11:00","11:00-12:00"],
    "C": ["9:00-10:00","10:00-11:00","11:00-12:00"]}
domains = {}
for class_name in classes:
    domains[class_name] = []
    for time in time_slots:
        for room in rooms:
            if time in room_availability[room]:
                domains[class_name].append((time, room))
def is_valid(class_name, value, assignment):
    time, room = value
    for other_class, other_value in assignment.items():
        other_time, other_room = other_value
        if time == other_time and room == other_room:
            return False
        students1 = set(classes[class_name])
        students2 = set(classes[other_class])
        if time == other_time:
            if students1.intersection(students2):
                return False
    return True
def backtracking(assignment):
    if len(assignment) == len(classes):
        return assignment
    unassigned = [
        c for c in classes
        if c not in assignment
    ]
    class_name = unassigned[0]
    for value in domains[class_name]:
        if is_valid(class_name, value, assignment):
            assignment[class_name] = value
            result = backtracking(assignment)
            if result is not None:
                return result
            del assignment[class_name]
    return None
solution = backtracking({})
if solution:
    print("\nVALID TIMETABLE")
    print("=" * 55)
    for class_name, value in solution.items():
        time, room = value
        print(
            f"{class_name:<12} "
            f"Time: {time:<15} "
            f"Room: {room}"
        )
    print("=" * 55)
else:
    print("No valid timetable found.")