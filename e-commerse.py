import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import emoji
import math
df = pd.read_excel("C:\\Users\\DELL\\Downloads\\ecommerce_sales_dataset.xlsx")

#Data Cleaning:-

print(df.isnull().sum())
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Price"].fillna(df["Price"].median(), inplace=True)
df["Quantity"].fillna(df["Quantity"].median(),inplace=True)
df["City"]=df["City"].fillna("Unknown")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
df["Date"] = df["Date"].fillna(method="bfill")
df.loc[df["Quantity"]<0, "Quantity"] = df["Quantity"].median()
df.drop_duplicates(inplace=True)


#Functionalities:-


df["revenue"]=df["Price"]*df["Quantity"]
revenue=df.groupby("Product")["revenue"].sum()
top_revenue_product=revenue.idxmax()
low_revenue_product=revenue.idxmin()
print("\nProducts Revenue :\n")
print(revenue)
print("\nHighest Revenue Product:\n")
print(top_revenue_product)
print("\nLowest Revenue Product:\n")
print(low_revenue_product)
print("\nTotal Selled Products:\n ")
sell=df.groupby("Product")["Quantity"].sum()
print(sell)
print("\ncity-wise orders / quantity:\n ")
print(sell.idxmax())
city_order=df.groupby("City")["Quantity"].sum()
print(city_order)
print("\nCity-wise sales:\n")
city_sell=df.groupby("City")["revenue"].sum()
print(city_sell)

# Category-wise Sales trend
print("\nTotal Sell By Each Category:\n")
cate = df.groupby("Category")["Quantity"].sum()
print(cate)
print("\nTop Selling Category: \n")
top_cate=cate.idxmax()
print(top_cate)
print("\nLowest Selling Category: \n")
low_cate=cate.idxmin()
print(low_cate)

#nAOV = Total Revenue / Total Orders
print("------AOV(Avg. Order value)------\n")
total_revenue=df["revenue"].sum()
total_unique_order=df["OrderID"].nunique() # yha se unique ordwer d dekh li mene
aov=total_revenue/total_unique_order
print(f"\nAverage ek order pe customer {aov} spend kar raha hai.\n")

# Dashboard:-
total_products_sold=df["Quantity"].sum()
total_order=df["OrderID"].nunique()
print("------DASHBOARD------\n")
print(f"\nTotal-Revenue is: {total_revenue}")
print(f"Total Orders: {total_order}")
print(f"Total Sold Product is: {total_products_sold}\n")
print(f"Top Selling Product is: {sell.idxmax()}")
print(f"Lowest Selling Product is: {sell.idxmin()}\n")
print(f"Highest Revenue Product is: {top_revenue_product}")
print(f"Lowest Revenue Product is: {low_revenue_product}\n")
print(f"Top City With Most Revenue is: {city_sell.idxmax()}")
print(f"Top City With lowest revenue is: {city_sell.idxmin()}\n")
print(f"Top City With Most Demand is: {city_order.idxmax()}")
print(f"Top City With lowest Demand is: {city_order.idxmin()}")

# Visualization:-

plt.bar(sell.index,sell.values,color='r')
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.show()

plt.bar(city_sell.index,city_sell.values,color='b')
plt.title("Top Selling Products")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

cate_revenue=df.groupby("Category")["revenue"].sum()
plt.pie(cate_revenue.values,labels=cate_revenue.index,autopct="%1.1f%%")
plt.show()

revenuee=revenue.sort_values(ascending=False).head(5)
plt.barh(revenuee.index,revenuee.values,color='y')
plt.title("Highest Revenue Products")
plt.xlabel("Revenue")
plt.ylabel("Products")
plt.show()
















