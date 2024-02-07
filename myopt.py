import pandas as pd
import numpy as np
import datetime

def log_event(message):
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry=f"{timestamp}: {message}"
    with open("log.txt", 'a') as f:
        mess=f.write(log_entry)

try:
  log_event(" <---- Starting reading of database  ---->")
  df=pd.read_csv("Students_data.csv")
  log_event(" <---- Displaing first five rows of database  ---->")
  f_df=df.head(5)
  log_event(" <---- Displaing last five rows of database  ---->")
  l_df=df.tail(5)
  
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
  new_filename = f"updated_csv_file_{timestamp}.csv"
  df.to_csv(new_filename)
  log_event("Updated new file")
  
  avg_score=df['Score'].mean()
  log_event(" <---- Displaing mean of database  ---->")
  avg_std=df['Score'].std()
  log_event(" <---- Displaing std of database  ---->")
  
  top_stu=df.sort_values(by='Score', ascending=False)
  log_event(" <---- Displaing our top students ---->")
  log_event(str(top_stu))
  
  df.loc[(df['Group']=='A')& (df['Score']>85)]
  name=df.sort_values(by='Name', ascending=True)
  log_event(" <---- Displaing Groups by name and score  ---->")

except Exception as e:
    # Log any errors or exceptions
    log_event(f"Error: {str(e)}")