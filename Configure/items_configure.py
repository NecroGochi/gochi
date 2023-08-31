PATH_IMAGINES_ITEMS = "Images/Items/"


Book = {
    "Name": "Possessed book",
    "Shape": "Rect",
    "Distance_from_player": 150,
    "Quantity": 1,
    "Power": 20,
    "Speed": 0.02,
    "Bonus_level": {
            'power': 2,
            'speed': 0.02
        },
    "Images": [PATH_IMAGINES_ITEMS + "ksiazka.png"]
}

Card = {
    "Name": "Possessed card",
    "Shape": "Rect",
    "Distance_from_player": 300,
    "Quantity": 1,
    "Power": 20,
    "Speed": 2.0,
    "Bonus_level": {
            'power': 5,
            'speed': 0
        },
    "Images": [PATH_IMAGINES_ITEMS + "karta.png"]
}