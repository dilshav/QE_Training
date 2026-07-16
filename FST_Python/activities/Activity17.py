import pandas as pd
import csv
data={
    "Usernames":["Admin","Charles","Deku"],
    "Passwords":["password","Charl13","AllMight"]
}

df=pd.DataFrame(data)
df.to_csv("loginInfo.csv", index=False)

#print usernames
# with open("loginInfo.csv", mode="r") as file:
#     reader=csv.reader()

df=pd.read_csv("loginInfo.csv")
print(df["Usernames"])
print(f"Username: {df["Usernames"][1]},Passwords: {df["Passwords"][1]}")
print(df.sort_values("Usernames", ascending=True))
print(df.sort_values("Passwords", ascending=False))