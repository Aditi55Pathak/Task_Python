import pandas as pd
import numpy as np
import seaborn as sns
import datetime
from matplotlib import pyplot as plt
import schedule
import time

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    log_entry = f"{timestamp}:{message}\n"
    with open("tempLogs.csv", "a") as f:
        f.write(log_entry)


try:
    log_event("Reading the CSV file here")
    df = pd.read_csv("temp.csv")
    log_event(str(df))
    print(df)
    log_event("Displaying heads and tails")
    head_set = df.head(5)
    tail_set = df.tail(3)
    print(head_set)
    print(tail_set)
    log_event(str(head_set))
    log_event(str(tail_set))
    log_event("Making a new column named ComfortZone")
    df["ComfortZone"] = "Normal"  # Default value
    log_event("Adding values to ComfortZone")
    for index, row in df.iterrows():
        if row["Temperature"] > 25 and row["Humidity"] < 65:
            df.at[index, "ComfortZone"] = "Comfortable"
        elif row["Temperature"] < 20:
            df.at[index, "ComfortZone"] = "Cold"
    log_event(str(df))
    print(df)
    log_event(
        "Grouping DataFrame by month and calculate the average temperature and humidity for each month"
    )
    group_here = df.groupby("Date")
    df['avgTempByMonth'] = group_here["Temperature"].mean()
    print(group_here)
    log_event(str(group_here))
    log_event("Adding new column Average and putting vales of avgTempByMonth into it")
    log_event(str(df))
    print(df)

    log_event("Dat with highest temp")
    # Identify and display the day with the highest temperature
    max_temp_day = df["Temperature"].idxmax()
    max_temp_value = df["Temperature"].max()
    log_event(str(max_temp_day))
    log_event(str(max_temp_value))
    print(f"Day with the highest temperature: {max_temp_day} ({max_temp_value} °C)")

    # Identify and display the day with the lowest temperature
    log_event("Dat with lowest temp")
    min_temp_day = df["Temperature"].idxmin()
    min_temp_value = df["Temperature"].min()
    log_event(str(max_temp_day))
    log_event(str(max_temp_value))
    print(f"Day with the lowest temperature: {min_temp_day} ({min_temp_value} °C)")

    # creating a plot
    
    log_event("Creating a line chart showing Temperature vs Date")
    temp = df["Temperature"]
    month = df["Date"]
    print(
        "Create a line plot to visualize the trend of temperature and humidity over the month."
    )
    plt.figure(figsize=(14, 7))
    plt.title("Temp Data")
    plt.xlabel("Temperature")
    plt.ylabel("Month")
    plt.plot(temp, month)
    plt.grid(True)
    plt.show()

    def generate_heatMap():

      print("Generating a heat map")
      log_event("Generating a heat map using sea born")
      correlation_matrix = df[["Temperature", "Humidity"]].corr()
      sns.heatmap(
          correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5
      )
      plt.title("Correlation Heatmap: Temperature vs Humidity")
      plt.show()

    # generate_heatMap()

except Exception as e:
    print("This is an exception : ", e)
    log_event("This is Error message", e)


# Define the specific time to run the task (replace 'HH:MM' with your desired time)
scheduled_time = "13:37"

# Schedule the task to run at the specified time each day
schedule.every().day.at(scheduled_time).do(generate_heatMap)

# Keep the script running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
