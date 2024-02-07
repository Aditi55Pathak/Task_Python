import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
import logging


def log_events(message):
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{message} : {time_stamp}"
    with open("MyPrac.txt", "a") as f:
        f.write(log_entry)


try:
    # Reading data from dataset
    log_events("Reading data")
    print("Printing data")
    df = pd.read_csv("sales_data.csv")
    log_events(str(df))
    print(df)
    # Displaying first few rows of data from dataset
    print("Displaying head")
    head_set = df.head()
    print(head_set)
    # Displaying and handling null values
    print("Displaying null values")
    miss_val = df.isnull().sum()
    print(miss_val)
    clean = df.dropna()
    print(clean)
    # convrting datetime into pandas datetime format
    print("Displaying values according to pandas date and time")
    df["Date"] = pd.to_datetime(df["Date"])
    print(df)
    # Create a new column 'Month' and populate it with the respective month
    log_events("Months")
    print("Displaying Month")
    df["Month"] = df["Date"].dt.month
    print(df)
    # Revenue creation
    print("Revenue creation")
    df["Revenue"] = df["Price"] * df["TotalAmount"]
    print(df)
    # Identifying top selling product based on quanity sold
    print("Top Selling Product Based On Quantity Sold")
    top_selling_products = (
        df.groupby("ProductName")["Quantity"].max().sort_values(ascending=False)
    )
    print(top_selling_products)
    # Group the data by 'Month' and calculate the total monthly revenue
    monthly_revenue = df.groupby("Month")["Revenue"].sum()
    # Create a line plot to visualize the trend of total monthly revenue
    print("Genertaing line plot for total revenue")
    plt.figure(figsize=(10, 6))
    plt.title("Line Plot For Total Monthly Revenue", fontweight="bold", fontsize=25)
    plt.xlabel("Month")
    plt.ylabel("Revenue Generated")
    plt.plot(monthly_revenue.index, monthly_revenue)
    plt.grid(True)
    plt.show()
    # Generate a bar chart to visualize the top-selling products.
    print("Generating Bar Chart For Top Selling Products")
    plt.figure(figsize=(10, 6))
    plt.barh(top_selling_products.index, top_selling_products, color="skyblue")
    plt.xlabel("Number Of Units Sold")
    plt.ylabel("Products Name")
    plt.title("Bar Chart For Top Selling Products", fontweight="bold", fontsize=25)
    plt.show()
    # Save the final DataFrame with added columns to a new CSV file
    df.to_csv("processed_sales_data.csv", index=False)
    # Create a summary report text file
    summary_report = """
    Analysis Summary:
    
    1. Total Revenue: ${:.2f}
    2. Top-Selling Products:
        - Product A: {}
        - Product B: {}
        - Product C: {}
    3. Monthly Trends:
        - Highest Revenue Month: {}
        - Lowest Revenue Month: {}
    """.format(
        df["Revenue"].sum(),
        df.groupby("ProductName")["Quantity"].sum().idxmax(),
        df.groupby("ProductName")["Quantity"].sum().idxmax(),
        df.groupby("ProductName")["Quantity"].sum().idxmax(),
        df.groupby("Month")["Revenue"].sum().idxmax(),
        df.groupby("Month")["Revenue"].sum().idxmin(),
    )

    with open("analysis_summary.txt", "w") as file:
        file.write(summary_report)

    print("Files saved successfully: processed_sales_data.csv, analysis_summary.txt")


except Exception as e:
    print("An exception occurred:", e)
    # Log the full exception traceback to the log file
    logging.exception("An exception occurred:")
