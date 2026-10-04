import pandas as pd

# Product data
data = {
    "Product Name": ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Price": [50000, 20000, 15000, 2000, 1500],
    "Quantity Sold": [10, 60, 30, 80, 55]
}

df = pd.DataFrame(data)

# Calculate total sales
df["Total Sales"] = df["Price"] * df["Quantity Sold"]

print("Product Sales Data:")
print(df)

# Product with highest sales
highest_sales = df.loc[df["Total Sales"].idxmax()]

print("\nProduct with Highest Sales:")
print(highest_sales)

# Average product price
print("\nAverage Product Price:", df["Price"].mean())

# Products where quantity sold is greater than 50
print("\nProducts with Quantity Sold greater than 50:")
print(df[df["Quantity Sold"] > 50])

# Sort products based on total sales
print("\nProducts sorted by Total Sales:")
print(df.sort_values("Total Sales", ascending=False))
