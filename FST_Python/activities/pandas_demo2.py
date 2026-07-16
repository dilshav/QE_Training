import pandas as pd

#read the csv file
df=pd.read_csv("employees.csv")

print(df)
print(df.sort_values("Name", ascending=False))

#write to a csv

data={
    "Vehicle type":["car","car","bike"],
    "Manufacturer":["Maruthi","Toyota","Enfield"],
    "Model":["Swift","Corolla","Thunderbird"]
}

df=pd.Dataframe(data)
df.to_csv("vehicles.csv")
