import pandas as pd
import numpy as np
import datetime

def log_events(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} : {message}"

    with open("mylog.txt", 'a') as f:
        f.write(log_entry + '\n')

try:
    log_events("Loading data frames from CSV file")
    df = pd.read_csv('sales_data.csv')
    print(df)

    log_events("Displaying first 5 rows of the dataset:")
    print(df.head(5))

    log_events("Displaying last 5 rows of the dataset:")
    print(df.tail(5))

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    filename = f"updated_sales_report_{timestamp}.csv"
    df.to_csv(filename, index=False)
    log_events(f"Updated sales data saved to {filename}")

    log_events("Calculating total revenue")
    df['total_revenue'] = df['Price'] * df['QuantitySold']
    log_events("Total revenue calculated")

    log_events("Product with the highest total revenue:")
    max_revenue_product = df.loc[df['total_revenue'].idxmax()]
    log_events(str(max_revenue_product))

    log_events("Displaying items with the 'Electronics' category only:")
    electronics_df = df[df['Category'] == 'Electronics']
    print(electronics_df)
    log_events("Items with the 'Electronics' category displayed")

    log_events("Sorting total revenue in descending order:")
    sorted_df = df.sort_values(by='total_revenue', ascending=False)
    print(sorted_df)

except Exception as e:
    log_events(f"Error: {str(e)}")
