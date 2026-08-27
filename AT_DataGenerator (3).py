
import random
import sys

# Auckland Western Line Stations (Hyper-Local Context)
WESTERN_LINE_STATIONS = [
    (101, "Britomart"),
    (102, "Newmarket"),
    (103, "Mt Eden"),
    (104, "Kingsland"),
    (105, "Morningside"),
    (106, "Baldwin Ave"),
    (107, "Mt Albert"),
    (108, "Avondale"),
    (109, "New Lynn"),
    (110, "Fruitvale Rd"),
    (111, "Glen Eden"),
    (112, "Sunnyvale"),
    (113, "Henderson"),
    (114, "Sturges Rd"),
    (115, "Ranui"),
    (116, "Swanson")
]

# Random name pools (Localized to NZ)
FIRST_NAMES = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Hemi", "Aroha", "Tane", "Wiremu", "Kiri", "Anahera", "Liam", "Charlotte", "Oliver", "Amelia", "Noah", "Isla"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Te Rangi", "Waititi", "Ihimaera", "Winiata", "Tupou", "Wong", "Singh", "Chen", "Patel", "Kumar"]
TICKET_TYPES = ["Standard", "Standard", "Standard", "Child", "Child", "Senior", "Gold AT HOP"]

def generate_data(student_id):
    # Seed the randomizer with the Student ID to ensure unique but reproducible datasets
    try:
        random.seed(int(student_id))
    except ValueError:
        random.seed(student_id)
    
    filename = f"AT_Data_{student_id}.txt"
    
    with open(filename, "w") as f:
        # 1. Generate Station Data for the Doubly Linked List and BST
        f.write("--- STATIONS ---\n")
        f.write("Format: STATION | StationID | StationName | BaseTraffic\n")
        for station_id, name in WESTERN_LINE_STATIONS:
            # Generate a base traffic capacity metric for the BST 
            base_traffic = random.randint(50, 500)
            f.write(f"STATION|{station_id}|{name}|{base_traffic}\n")
            
        f.write("\n--- MANIFEST ---\n")
        f.write("Format: EVENT_TYPE | Data...\n")
        # 2. Generate Passenger Manifest Events for the Queue and Stack
        num_events = random.randint(80, 150)
        
        for _ in range(num_events):
            event_chance = random.random()
            
            if event_chance < 0.75: 
                # 75% chance of a passenger boarding (Triggers the Ticketing Queue)
                fname = random.choice(FIRST_NAMES)
                lname = random.choice(LAST_NAMES)
                dest = random.choice(WESTERN_LINE_STATIONS)[0]
                ticket = random.choice(TICKET_TYPES)
                f.write(f"BOARD|{fname} {lname}|{dest}|{ticket}\n")
                
            elif event_chance < 0.90: 
                # 15% chance to process queue (Triggers integration: Queue -> Linked List -> BST)
                f.write("PROCESS_TRAIN\n")
                
            else: 
                # 10% chance of cancellation (Triggers the Stack logic for LIFO offboarding)
                f.write("CANCEL_LAST_TRAIN\n")

    print("\n" + "="*50)
    print(f"✅ Dataset successfully generated: {filename}")
    print("="*50)
    print("Please place this .txt file in the same directory as your Python scripts")
    print("and use it to feed data into your Data Structures for Assessment 1.")

    
    if student_id.strip():
        generate_data(student_id.strip())
    else:
        print("❌ Error: Student ID cannot be empty.")
