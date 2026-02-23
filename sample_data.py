"""
Sample data that mimics real Procore API responses
~500 data points spanning 2024-2026
"""

import random
from datetime import datetime, timedelta

# Seed for reproducibility
random.seed(42)

# Helper data
ARCHITECTS = ["HKS Architects", "Gensler", "SOM", "Perkins&Will"]
ENGINEERS = ["MEP Engineer", "Structural Engineer", "Fire Protection", "AV Consultant"]
CONTRACTORS = ["R&J Construction", "Owner's Rep", "GC", "Interior Designer"]
BALL_IN_COURT = ARCHITECTS + ENGINEERS + CONTRACTORS

TEAM_MEMBERS = [
    "Anthony Buonantuono", "Mike Chen", "Sarah Johnson", "David Park",
    "Lisa Martinez", "James Wilson", "Emily Brown", "Robert Taylor",
    "Jennifer Lee", "Michael Garcia", "Amanda White", "Chris Anderson"
]

LOCATIONS = [
    "Level 11 - Open Office", "Level 11 - Conference A", "Level 11 - Corridor",
    "Level 12 - Core", "Level 12 - Elevator Lobby", "Level 12 - Restrooms", "Level 12 - Perimeter",
    "Level 13 - Executive Suite", "Level 13 - Board Room", "Level 13 - Kitchen",
    "Level 14 - Suite 1420", "Level 14 - Reception", "Level 14 - Electrical Room",
    "Level 15 - Penthouse", "Level 15 - Terrace", "Stair A - All Levels", "Stair B - All Levels",
    "Lobby - Main", "Lobby - Service", "Basement - MEP Room"
]

RFI_SUBJECTS = [
    "Ceiling height clarification", "Door hardware specification", "MEP coordination conflict",
    "Millwork finish confirmation", "Fire rating for partition", "Acoustical ceiling layout",
    "Window sill detail", "Electrical panel relocation", "Sprinkler head placement",
    "ADA clearance at entry", "HVAC diffuser locations", "Stair handrail finish",
    "Glass partition framing", "Light fixture mounting", "Floor transition detail",
    "Column enclosure dimension", "Duct routing conflict", "Cable tray path",
    "Smoke detector placement", "Access panel location", "Furniture power location",
    "Signage mounting height", "Reveal detail at door", "Base detail at glass",
    "Grille finish selection", "Outlet height confirmation", "Switch plate layout",
    "Thermostat location", "Fire alarm device placement", "Emergency lighting",
    "Exit sign location", "Drinking fountain spec", "Toilet partition type",
    "Mirror mounting detail", "Grab bar locations", "Paper towel dispenser",
    "Soap dispenser type", "Ceiling access panel", "Diffuser neck size"
]

SUBMITTAL_TITLES = [
    ("Door Hardware", "08 71 00"), ("Acoustical Ceiling Tiles", "09 51 00"),
    ("Millwork Shop Drawings", "06 41 00"), ("Paint Colors", "09 91 00"),
    ("Carpet Tile", "09 68 00"), ("Light Fixtures", "26 51 00"),
    ("VAV Boxes", "23 36 00"), ("Fire Extinguisher Cabinets", "10 44 00"),
    ("Exit Signs", "10 14 00"), ("Drywall Partition Details", "09 21 16"),
    ("Glass Partition System", "08 88 00"), ("Plumbing Fixtures", "22 40 00"),
    ("Diffusers and Grilles", "23 37 00"), ("Electrical Panels", "26 24 00"),
    ("Fire Alarm Devices", "28 31 00"), ("Security Cameras", "28 23 00"),
    ("Access Control Hardware", "08 71 13"), ("Elevator Cab Finishes", "14 21 00"),
    ("Stair Railings", "05 52 00"), ("Window Film", "08 87 00"),
    ("Ceramic Tile", "09 30 00"), ("Solid Surface Counters", "12 36 00"),
    ("Wood Flooring", "09 64 00"), ("Rubber Base", "09 65 00"),
    ("Tackable Wall Panels", "09 84 00"), ("Fabric Wrapped Panels", "09 83 00"),
    ("Blinds and Shades", "12 24 00"), ("Projection Screens", "11 52 00"),
    ("Toilet Accessories", "10 28 00"), ("Lockers", "10 51 00"),
    ("Metal Panels", "07 42 00"), ("Aluminum Framing", "08 44 00")
]

SUBMITTAL_TYPES = ["Product Data", "Shop Drawing", "Sample", "Test Report", "Warranty"]
SUBMITTAL_STATUSES = ["approved", "pending", "revise_resubmit", "approved_as_noted", "rejected"]

SUBCONTRACTORS = [
    ("R&J Construction", "Carpenters"), ("Ace Electric", "Electricians"),
    ("AAA Plumbing", "Plumbers"), ("Metro HVAC", "HVAC"),
    ("Drywall Pros", "Drywall"), ("Pro Painters Inc", "Painters"),
    ("Ceiling Systems Inc", "Ceiling"), ("Flooring Solutions", "Flooring"),
    ("Glass Solutions NYC", "Glaziers"), ("Fire Protection Co", "Sprinkler Fitters"),
    ("Steel Works Inc", "Iron Workers"), ("Tile Masters", "Tile Setters")
]

WORK_ACTIVITIES = [
    "Framing continues", "MEP rough-in", "Drywall installation", "Taping and finishing",
    "Painting in progress", "Ceiling grid installation", "Tile installation",
    "Flooring installation", "Millwork installation", "Door and hardware install",
    "Light fixture installation", "Device trim-out", "Punch list work",
    "Final cleaning", "Inspection prep", "Touch-up and repairs"
]

DELIVERY_ITEMS = [
    "Drywall (40 sheets)", "Electrical conduit", "Light fixtures", "Door frames",
    "Doors (12)", "Hardware sets", "Ceiling grid", "Ceiling tiles", "Paint",
    "Carpet tile", "Ceramic tile", "Plumbing fixtures", "HVAC diffusers",
    "VAV boxes", "Millwork components", "Glass panels", "Aluminum framing"
]

VISITOR_TYPES = [
    "Owner's Rep - site walk", "Architect - RFI review", "MEP Engineer - coordination",
    "DOB Inspector", "Fire Marshal - inspection", "Interior Designer - review",
    "Client - progress tour", "Safety consultant", "Commissioning agent"
]

WEATHER_CONDITIONS = [
    ("Clear", 30, 85), ("Partly Cloudy", 35, 80), ("Cloudy", 32, 75),
    ("Rain", 40, 70), ("Snow", 20, 35), ("Overcast", 35, 65)
]

# Generate RFIs
def generate_rfis(count=150):
    rfis = []
    start_date = datetime(2024, 3, 1)

    for i in range(1, count + 1):
        created = start_date + timedelta(days=random.randint(0, 700))
        due = created + timedelta(days=random.randint(5, 14))
        status = random.choices(["open", "closed", "draft"], weights=[0.35, 0.55, 0.10])[0]

        rfi = {
            "id": i,
            "number": f"{i:03d}",
            "subject": f"{random.choice(RFI_SUBJECTS)} at {random.choice(LOCATIONS).split(' - ')[0]}",
            "status": status,
            "priority": random.choice(["High", "Normal", "Low"]),
            "cost_impact": random.choice(["None", "TBD", f"${random.randint(1,50)*500:,}"]),
            "schedule_impact": random.choice(["Yes", "No", "No", "No"]),
            "location": random.choice(LOCATIONS),
            "ball_in_court": {"name": random.choice(BALL_IN_COURT)},
            "created_by": {"name": random.choice(TEAM_MEMBERS)},
            "created_at": created.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "due_date": due.strftime("%Y-%m-%d"),
            "assignee": {"name": random.choice(TEAM_MEMBERS)}
        }

        if status == "closed":
            closed_date = due - timedelta(days=random.randint(0, 3))
            rfi["closed_at"] = closed_date.strftime("%Y-%m-%dT%H:%M:%SZ")

        rfis.append(rfi)

    return rfis

# Generate Submittals
def generate_submittals(count=150):
    submittals = []
    start_date = datetime(2024, 2, 1)

    for i in range(1, count + 1):
        title, spec = random.choice(SUBMITTAL_TITLES)
        submitted = start_date + timedelta(days=random.randint(0, 700))
        due = submitted + timedelta(days=random.randint(7, 21))
        status = random.choices(
            ["approved", "pending", "revise_resubmit", "approved_as_noted", "rejected"],
            weights=[0.45, 0.25, 0.15, 0.10, 0.05]
        )[0]

        division = (i // 10) + 1
        seq = (i % 10) + 1

        sub = {
            "id": i,
            "number": f"{division:02d}.{seq:02d}",
            "revision": str(random.choices([0, 1, 2], weights=[0.7, 0.25, 0.05])[0]),
            "title": f"{title} - {random.choice(['Type A', 'Type B', 'Schedule 1', 'Schedule 2', 'Option 1'])}",
            "spec_section": spec,
            "type": random.choice(SUBMITTAL_TYPES),
            "status": status,
            "submitted_by": {"name": random.choice([s[0] for s in SUBCONTRACTORS])},
            "responsible_contractor": random.choice([s[0] for s in SUBCONTRACTORS]),
            "approver": {"name": random.choice(ARCHITECTS + ENGINEERS)},
            "due_date": due.strftime("%Y-%m-%d"),
            "submitted_date": submitted.strftime("%Y-%m-%d"),
            "approved_date": (due - timedelta(days=random.randint(1, 5))).strftime("%Y-%m-%d") if status in ["approved", "approved_as_noted"] else "",
            "lead_time": f"{random.choice([2, 3, 4, 6, 8, 10, 12])} weeks"
        }

        submittals.append(sub)

    return submittals

# Generate Daily Logs
def generate_daily_logs(count=200):
    logs = []
    start_date = datetime(2024, 3, 4)  # Start on a Monday
    current_date = start_date

    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    log_id = 1
    while log_id <= count:
        # Skip weekends
        if current_date.weekday() < 5:
            # Determine weather
            month = current_date.month
            if month in [12, 1, 2]:
                weather_type, min_temp, max_temp = random.choice(WEATHER_CONDITIONS[:3] + [WEATHER_CONDITIONS[4]])
                temp = random.randint(min_temp, min(max_temp, 45))
            elif month in [6, 7, 8]:
                weather_type, min_temp, max_temp = random.choice(WEATHER_CONDITIONS[:3])
                temp = random.randint(max(min_temp, 65), max_temp)
            else:
                weather_type, min_temp, max_temp = random.choice(WEATHER_CONDITIONS[:4])
                temp = random.randint(min_temp, max_temp)

            weather_delay = weather_type in ["Snow", "Rain"] and random.random() < 0.3

            # Generate manpower
            base_trades = random.sample(SUBCONTRACTORS, random.randint(4, 8))
            manpower = []
            for company, trade in base_trades:
                headcount = random.randint(4, 16)
                if weather_delay:
                    headcount = max(2, headcount // 2)
                manpower.append({
                    "trade": trade,
                    "headcount": headcount,
                    "company": company
                })

            # Generate deliveries and visitors
            num_deliveries = random.randint(0, 4)
            num_visitors = random.randint(0, 2)

            log = {
                "id": log_id,
                "log_date": current_date.strftime("%Y-%m-%d"),
                "day": day_names[current_date.weekday()],
                "weather": f"{weather_type}, {temp}°F",
                "weather_delay": weather_delay,
                "work_hours": "7:00 AM - 3:30 PM" if not weather_delay else "7:00 AM - 2:00 PM",
                "manpower": manpower,
                "work_performed": f"{random.choice(WORK_ACTIVITIES)} on {random.choice(LOCATIONS).split(' - ')[0]}. {random.choice(WORK_ACTIVITIES)} on {random.choice(LOCATIONS).split(' - ')[0]}.",
                "deliveries": random.sample(DELIVERY_ITEMS, num_deliveries) if num_deliveries > 0 else [],
                "visitors": random.sample(VISITOR_TYPES, num_visitors) if num_visitors > 0 else [],
                "safety_incidents": [],
                "notes": random.choice([
                    "On schedule.", "Good progress.", "Ahead of schedule.",
                    "Minor delays resolved.", "Inspection passed.", "Coordination meeting held.",
                    "Punch list items addressed.", "Material delivery on time."
                ])
            }

            if weather_delay:
                log["notes"] = "Reduced crew due to weather. Interior work only."

            logs.append(log)
            log_id += 1

        current_date += timedelta(days=1)

    return logs

# Generate the data
SAMPLE_RFIS = generate_rfis(150)
SAMPLE_SUBMITTALS = generate_submittals(150)
SAMPLE_DAILY_LOGS = generate_daily_logs(200)
