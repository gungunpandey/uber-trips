#To read the dataset
import pandas as pd

#For visualization
import matplotlib.pyplot as plt

#Read the data
uber_df = pd.read_csv("C:/Users/GUNGUN PANDEY/OneDrive/Desktop/DS Projects/Python-Projects-Uber-Trips-Analysis/Data/uber-raw-data-sep14.csv")

#Display first 5 records
print(uber_df.head(5))
#Display last 5 records
print(uber_df.tail())

#Display the shape os dataset
print(uber_df.shape)

#Understand the properties of dataset
print(uber_df.info())

#Lets change the "Date/Time" column's datatype from string to datetime
uber_df['Date/Time'] = pd.to_datetime(uber_df['Date/Time'])

uber_df["Day"] = uber_df["Date/Time"].apply(lambda x: x.day)
uber_df["Hour"] = uber_df["Date/Time"].apply(lambda x: x.hour)
uber_df["Weekday"] = uber_df["Date/Time"].apply(lambda x: x.weekday())
print(uber_df.head(5))

#Visualize the density of rides per day of month
fig,ax = plt.subplots(figsize = (14,10))
plt.hist(uber_df.Day, width = 0.6, bins = 30)
plt.title("Density of trips per day", fontsize = 20)
plt.xlabel("Day", fontsize = 14)
plt.ylabel("Density of rides", fontsize = 14)

#Visualize the density of rides per Weekday
fig,ax = plt.subplots(figsize = (14,10))
plt.hist(uber_df.Weekday, width = 0.6, range = (0,6.5), bins = 7, color="green")
plt.title("Density of trips per Weekday", fontsize = 20)
plt.xlabel("Weekday", fontsize = 14)
plt.ylabel("Density of rides", fontsize = 14)