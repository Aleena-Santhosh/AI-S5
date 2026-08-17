flights = [{"id": "F1", "origin": "A", "destination": "B", "duration": 2},
    {"id": "F2", "origin": "B", "destination": "C", "duration": 2},
    {"id": "F3", "origin": "A", "destination": "C", "duration": 2},
    {"id": "F4", "origin": "C", "destination": "A", "duration": 2}]
aircraft = ["AC1", "AC2"]
crew = ["CR1", "CR2"]
time_slots = [8, 10, 12, 14, 16]
airport_capacity = {"A": 1,"B": 1,"C": 1}
maintenance = {"AC1": [12],"AC2": [14]}
def is_valid(flight, aircraft_id, crew_id, time, schedule):
    if time in maintenance[aircraft_id]:
        return False
    for item in schedule:
        if item["aircraft"] == aircraft_id:
            if item["time"] == time:
                return False
    for item in schedule:
        if item["crew"] == crew_id:
            if item["time"] == time:
                return False
    departure_airport = flight["origin"]
    count = 0
    for item in schedule:
        if (
            item["flight"]["origin"] == departure_airport
            and item["time"] == time
        ):
            count += 1
    if count >= airport_capacity[departure_airport]:
        return False
    return True
def schedule_flights(index, schedule):
    if index == len(flights):
        return True
    flight = flights[index]
    for aircraft_id in aircraft:
        for crew_id in crew:
            for time in time_slots:
                if is_valid(flight,aircraft_id,crew_id,time,schedule):
                    assignment = {"flight": flight,"aircraft": aircraft_id,"crew": crew_id,"time": time}
                    schedule.append(assignment)
                    print(
                        f"Trying: {flight['id']} -> "
                        f"{aircraft_id}, {crew_id}, {time}:00")
                    if schedule_flights(index + 1, schedule):
                        return True
                    schedule.pop()
                    print(f"Backtracking: {flight['id']} "f"at {time}:00" )
    return False
schedule = []
print("========== AIRLINE SCHEDULING ==========\n")
if schedule_flights(0, schedule):
    print("\n========== FINAL SCHEDULE ==========\n")
    for item in schedule:
        flight = item["flight"]
        print( f"Flight {flight['id']}: " f"{flight['origin']} -> {flight['destination']} | "
            f"Aircraft: {item['aircraft']} | "f"Crew: {item['crew']} | "
            f"Departure: {item['time']}:00")
    print("\nAll flights scheduled successfully!")
else:
    print("\nNo valid schedule could be found.")