import time
import datetime
import random
import plotter

app_file_name="app.apk"

tracked_data = {
    "12" : 0,
    "13" : 0,
    "14" : 0,
    "15" : 0,
    "16" : 0
}

def open_app():
    with open(app_file_name,"r") as myFile:
        start_time = time.time()

        data = myFile.readline()
        time.sleep(random.randint(1,5)) # sleep for any seconds between 1 to 5

        end_time = time.time()

        time_difference = int(end_time - start_time)

        # current_hour = str(datetime.datetime.now().hour)
        current_hour = str(random.randint(12,16))

        tracked_data[current_hour] = tracked_data.get(current_hour) + time_difference


for i in range(2):
    print(f"App Opened - {i} time")
    open_app()
    print(f"App Closed")

hours_list=[]
for hour_data in tracked_data:
    hours_list.append(hour_data + "pm")

print(f"Plotting Screen Time as Bar-Graph")
plotter.plot_bar_graph_v2(x_axis=hours_list,y_axis=list(tracked_data.values()))