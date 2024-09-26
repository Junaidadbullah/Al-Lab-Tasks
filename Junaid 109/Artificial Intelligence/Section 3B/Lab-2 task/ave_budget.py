
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

total_budget = 0 
for name,budget in movies:
    total_budget += budget 

average_budget=total_budget/len(movies)
print(f'average budget: (average_budget)')

for name, budget in movies:
    if budget > average_budget:
        print(f"{name} has a higher budget and {int(budget - average_budget)} higher than the average.")

