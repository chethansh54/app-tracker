import plotter
import random

tracked_data = {
    "Bangalore" : 0,
    "Hyderabad" : 0,
    "Chennai" : 0,
    "Noida" : 0,
    "Patna" : 0,
}

def vote(city_name,votes):
    tracked_data[city_name] = tracked_data.get(city_name, 0) + votes
    print(f"Voting for : {city_name} => {votes} votes.")

for i in range(10):
    random_city_name = random.choice(list(tracked_data.keys()))
    random_votes = random.randint(0,100)

    vote(city_name=random_city_name, votes=random_votes)

print(f"Plotting City-Wise Votes as Bar-Graph...")
plotter.plot_bar_graph_v2(x_axis=list(tracked_data.keys()),y_axis=list(tracked_data.values()))