import pandas as pd

df=pd.read_excel("c:\\Users\\jeetv\\OneDrive\\Desktop\\data analyst projects\\Ola ride project\\Bookings-20000-Rows (1).xlsx")
print(df)


df.info()

df1=df.isnull().sum()
print(df1)


df1=df["V_TAT"].fillna(df["V_TAT"].mean(),inplace=True)
print(df1)

print(df["V_TAT"])

df1=df.isnull().sum()
print(df1)

df1=df["C_TAT"].fillna(df["C_TAT"].mean(),inplace=True)
print(df1)

print(df["C_TAT"])

df1=df.isnull().sum()
print(df1)

df1=df["Canceled_Rides_by_Customer"].fillna("Driver's Behaviour Is Not Good",inplace=True)
print(df1)

print(df["Canceled_Rides_by_Customer"])

df1=df.isnull().sum()
print(df1)

df1=df["Canceled_Rides_by_Driver"].fillna("Customer's Behaviour Is Not Good",inplace=True)
print(df1)


print(df["Canceled_Rides_by_Driver"])

df1=df.isnull().sum()
print(df1)

df1=df["Incomplete_Rides"].fillna("No",inplace=True)
print(df1)

df1=df["Incomplete_Rides_Reason"].fillna("Vehicle Issue",inplace=True)
print(df1)

print(df["Incomplete_Rides"])
print(df["Incomplete_Rides_Reason"])

df1=df.isnull().sum()
print(df1)


df1=df["Payment_Method"].fillna("Credit Card",inplace=True)
print(df1)

df1=df["Driver_Ratings"].fillna(df["Driver_Ratings"].mean(),inplace=True)
print(df1)

df1=df["Customer_Rating"].fillna(df["Customer_Rating"].mean(),inplace=True)
print(df1)

print(df["Payment_Method"])
print(df["Driver_Ratings"])
print(df["Customer_Rating"])

df1=df.isnull().sum()
print(df1)

#Total Booking Value
df1=df["Booking_Value"].sum()
print(df1)

#Which payment method is used most
df1=df["Payment_Method"].value_counts()
print(df1)

#which customer has the highest rating
df1=df.groupby("Customer_ID")["Customer_Rating"].mean().sort_values(ascending=False).head(1)
print(df1)

#which Pickup point has the highest booking value
df1=df.groupby("Pickup_Location")["Booking_Value"].sum().sort_values(ascending=False).head(1)
print(df1)

#which drop point has the highest booking value
df1=df.groupby("Drop_Location")["Booking_Value"].sum().sort_values(ascending=False).head(1)
print(df1)

#Booking status count
df1=df["Booking_Status"].value_counts()
print(df1)


#Top 10 customers with the highest booking value
df1=df.groupby("Customer_ID")["Booking_Value"].sum().sort_values(ascending=False).head(10)
print(df1)

#vehicle type performance
df1=df.groupby("Vehicle_Type")["Booking_Value"].agg(["sum","mean","count"])
print(df1)

#cancelled rides by customer
df1=df["Canceled_Rides_by_Customer"].value_counts()
print(df1)

#cancelled rides by driver
df1=df["Canceled_Rides_by_Driver"].value_counts()


#Highest Revenue of Vehicle Type
df1=df.groupby("Vehicle_Type")["Booking_Value"].sum().sort_values(ascending=False)
print(df1)

#Average Driver Ratings by Vehicle Type
df1=df.groupby("Vehicle_Type")["Driver_Ratings"].mean().sort_values(ascending=False)
print(df1)

#Average Customer Ratings by Vehicle Type
df1=df.groupby("Vehicle_Type")["Customer_Rating"].mean().sort_values(ascending=False)
print(df1)

#revenue by payment method
df1=df.groupby("Payment_Method")["Booking_Value"].sum().sort_values(ascending=False)
print(df1)

df.to_excel("Ola_Bookings_Cleaned.xlsx",index=False)