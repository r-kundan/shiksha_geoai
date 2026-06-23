import pandas as pd

def load_data():
    data = {
        "School": ["A", "B", "C", "D", "E"],
        "District": ["Gurugram", "Sirsa", "Faridabad", "Bhiwani", "Panipat"],
        "Students": [1000, 300, 850, 250, 900],
        "Teachers": [20, 1, 10, 2, 12],
        "Vacancy": [2, 5, 3, 6, 1],
        "Growth": [15, 2, 12, 1, 10],
        "Accessibility": [90, 40, 85, 30, 75]
    }

    return pd.DataFrame(data)