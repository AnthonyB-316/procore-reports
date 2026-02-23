"""
Sample data that mimics real Procore API responses
Used for demo/testing without API credentials
"""

SAMPLE_RFIS = [
    {
        "id": 1,
        "number": "001",
        "subject": "Ceiling height clarification at Level 12",
        "status": "open",
        "ball_in_court": {"name": "HKS Architects"},
        "created_at": "2026-01-10T10:00:00Z",
        "due_date": "2026-01-17",
        "assignee": {"name": "Mike Chen"}
    },
    {
        "id": 2,
        "number": "002",
        "subject": "Door hardware specification for Suite 1420",
        "status": "open",
        "ball_in_court": {"name": "Owner's Rep"},
        "created_at": "2026-01-08T14:30:00Z",
        "due_date": "2026-01-15",
        "assignee": {"name": "Sarah Johnson"}
    },
    {
        "id": 3,
        "number": "003",
        "subject": "MEP coordination conflict at elevator lobby",
        "status": "closed",
        "ball_in_court": {"name": "GC"},
        "created_at": "2026-01-05T09:00:00Z",
        "due_date": "2026-01-12",
        "closed_at": "2026-01-11T16:00:00Z",
        "assignee": {"name": "Anthony Buonantuono"}
    },
    {
        "id": 4,
        "number": "004",
        "subject": "Millwork finish color confirmation",
        "status": "open",
        "ball_in_court": {"name": "Interior Designer"},
        "created_at": "2026-01-15T11:00:00Z",
        "due_date": "2026-01-22",
        "assignee": {"name": "Mike Chen"}
    },
    {
        "id": 5,
        "number": "005",
        "subject": "Fire rating for corridor partition",
        "status": "open",
        "ball_in_court": {"name": "HKS Architects"},
        "created_at": "2026-01-03T08:00:00Z",
        "due_date": "2026-01-10",
        "assignee": {"name": "Sarah Johnson"}
    },
    {
        "id": 6,
        "number": "006",
        "subject": "Acoustical ceiling grid layout",
        "status": "draft",
        "ball_in_court": {"name": "GC"},
        "created_at": "2026-01-20T10:00:00Z",
        "due_date": "2026-01-27",
        "assignee": {"name": "Anthony Buonantuono"}
    },
    {
        "id": 7,
        "number": "007",
        "subject": "Window sill detail at curtain wall",
        "status": "closed",
        "ball_in_court": {"name": "GC"},
        "created_at": "2026-01-02T09:00:00Z",
        "due_date": "2026-01-09",
        "closed_at": "2026-01-08T14:00:00Z",
        "assignee": {"name": "Mike Chen"}
    },
    {
        "id": 8,
        "number": "008",
        "subject": "Electrical panel relocation request",
        "status": "open",
        "ball_in_court": {"name": "MEP Engineer"},
        "created_at": "2026-01-18T13:00:00Z",
        "due_date": "2026-01-25",
        "assignee": {"name": "Sarah Johnson"}
    }
]

SAMPLE_SUBMITTALS = [
    {
        "id": 1,
        "number": "01.01",
        "title": "Door Hardware - Schlage",
        "spec_section": "08 71 00",
        "status": "approved",
        "submitted_by": {"name": "ABC Hardware Co"},
        "due_date": "2026-01-15",
        "submitted_date": "2026-01-10"
    },
    {
        "id": 2,
        "number": "01.02",
        "title": "Acoustical Ceiling Tiles - Armstrong",
        "spec_section": "09 51 00",
        "status": "pending",
        "submitted_by": {"name": "Ceiling Systems Inc"},
        "due_date": "2026-01-20",
        "submitted_date": "2026-01-12"
    },
    {
        "id": 3,
        "number": "01.03",
        "title": "Millwork Shop Drawings - Custom Cabinets",
        "spec_section": "06 41 00",
        "status": "revise_resubmit",
        "submitted_by": {"name": "Fine Woodworks LLC"},
        "due_date": "2026-01-18",
        "submitted_date": "2026-01-08"
    },
    {
        "id": 4,
        "number": "02.01",
        "title": "Paint Colors - Benjamin Moore",
        "spec_section": "09 91 00",
        "status": "approved",
        "submitted_by": {"name": "Pro Painters Inc"},
        "due_date": "2026-01-10",
        "submitted_date": "2026-01-05"
    },
    {
        "id": 5,
        "number": "02.02",
        "title": "Carpet Tile - Interface",
        "spec_section": "09 68 00",
        "status": "pending",
        "submitted_by": {"name": "Flooring Solutions"},
        "due_date": "2026-01-22",
        "submitted_date": "2026-01-14"
    },
    {
        "id": 6,
        "number": "03.01",
        "title": "Light Fixtures - Schedule A",
        "spec_section": "26 51 00",
        "status": "approved_as_noted",
        "submitted_by": {"name": "Electric Supply Co"},
        "due_date": "2026-01-12",
        "submitted_date": "2026-01-06"
    },
    {
        "id": 7,
        "number": "03.02",
        "title": "VAV Boxes - Trane",
        "spec_section": "23 36 00",
        "status": "pending",
        "submitted_by": {"name": "HVAC Distributors"},
        "due_date": "2026-01-25",
        "submitted_date": "2026-01-18"
    },
    {
        "id": 8,
        "number": "04.01",
        "title": "Fire Extinguisher Cabinets",
        "spec_section": "10 44 00",
        "status": "rejected",
        "submitted_by": {"name": "Safety Equipment Inc"},
        "due_date": "2026-01-08",
        "submitted_date": "2026-01-03"
    }
]

SAMPLE_DAILY_LOGS = [
    {
        "id": 1,
        "log_date": "2026-01-20",
        "weather": "Clear, 35°F",
        "weather_delay": False,
        "manpower": [
            {"trade": "Carpenters", "headcount": 12},
            {"trade": "Electricians", "headcount": 8},
            {"trade": "Plumbers", "headcount": 4},
            {"trade": "HVAC", "headcount": 6}
        ],
        "notes": "Framing continues on Level 14. MEP rough-in on Level 12.",
        "safety_incidents": []
    },
    {
        "id": 2,
        "log_date": "2026-01-21",
        "weather": "Snow, 28°F",
        "weather_delay": True,
        "manpower": [
            {"trade": "Carpenters", "headcount": 8},
            {"trade": "Electricians", "headcount": 6},
            {"trade": "Plumbers", "headcount": 2},
            {"trade": "HVAC", "headcount": 4}
        ],
        "notes": "Reduced crew due to weather. Interior work only.",
        "safety_incidents": []
    },
    {
        "id": 3,
        "log_date": "2026-01-22",
        "weather": "Cloudy, 32°F",
        "weather_delay": False,
        "manpower": [
            {"trade": "Carpenters", "headcount": 14},
            {"trade": "Electricians", "headcount": 10},
            {"trade": "Plumbers", "headcount": 5},
            {"trade": "HVAC", "headcount": 6},
            {"trade": "Drywall", "headcount": 8}
        ],
        "notes": "Drywall started on Level 11. Full crew back on site.",
        "safety_incidents": []
    },
    {
        "id": 4,
        "log_date": "2026-01-23",
        "weather": "Clear, 38°F",
        "weather_delay": False,
        "manpower": [
            {"trade": "Carpenters", "headcount": 14},
            {"trade": "Electricians", "headcount": 10},
            {"trade": "Plumbers", "headcount": 5},
            {"trade": "HVAC", "headcount": 6},
            {"trade": "Drywall", "headcount": 10}
        ],
        "notes": "Good progress on all fronts. Inspection scheduled for Friday.",
        "safety_incidents": []
    },
    {
        "id": 5,
        "log_date": "2026-01-24",
        "weather": "Clear, 42°F",
        "weather_delay": False,
        "manpower": [
            {"trade": "Carpenters", "headcount": 12},
            {"trade": "Electricians", "headcount": 8},
            {"trade": "Plumbers", "headcount": 4},
            {"trade": "HVAC", "headcount": 5},
            {"trade": "Drywall", "headcount": 10}
        ],
        "notes": "DOB inspection passed. Framing complete on Level 14.",
        "safety_incidents": []
    }
]
