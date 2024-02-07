import pandas as pd
import numpy as np
import datetime

def log_events(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} : {message}"

    with open("purchase_analysis_log.txt", "a") as f:
        f.write(log_entry + '\n')

try:
    log_events("Reading files into dataset\n")
    df = pd.read_csv("customer_purchases.csv")
    print(df)

    log_events("Printing first and last ten rows from dataset\n")
    head_set = df.head(10)
    tail_set = df.tail(10)
    log_events(str(head_set))
    log_events(str(tail_set))

    log_events("Calculating total purchase for revenue generated\n")
    df['TotalRevenue'] = df["Price"] * df["QuantityPurchased"]
    print("Total revenue Generated\n")
    print(df['TotalRevenue'])
    log_events("Total revenue generated:\n")
    log_events(str(df['TotalRevenue']))

    log_events("Maximum revenue of the customer:\n")
    max_revenue = df.loc[df['TotalRevenue'].idxmax()]
    print(max_revenue)
    log_events(str(max_revenue))

    log_events("Purchases made only in last month\n")
    current_month = datetime.datetime.now().strftime("%Y-%m")
    last_month = df[df['PurchaseDate'].str.startswith(current_month)]
    print("Purchase made in last month:")
    print(last_month)
    log_events(str(last_month))

    log_events("New column TotalCost\n")
    df['TotalCost'] = df['Price'] * df['QuantityPurchased']
    print("My new column:")
    print(df)
    log_events(str(df))

except Exception as e:
    log_events(f"Error: {str(e)}")
