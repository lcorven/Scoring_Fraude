import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport
from pandasgui import show

df = pd.read_csv("./data/fraude_mobile_phone_ech_train_2021.csv")

#profile = df.profile_report(title="Scoring", minimal=True)
#profile.to_file("./exports/output.html")

#full_profile = df.profile_report(title="Scoring")
#full_profile.to_file("./exports/full_output.html")

# groupby.rolling.sum

df["datetime"] = pd.to_datetime(df['datetime'])
df["year"] = df["datetime"].dt.year
df["month"] = df["datetime"].dt.month

def make_amount_percent(x):
    # pour le code du dessous -> condition 0 ou pas 0
    pass

df["amountOldOrgPercent"] = df["amount"] / (df["oldbalanceOrg"] + 0.01)
df["amountOldDestPercent"] = df["amount"] / (df["oldbalanceDest"] + 0.01)
df["varBalanceOrg"] = (df["newbalanceOrig"] - df["oldbalanceOrg"]) / df["oldbalanceOrg"]
df["varBalanceDest"] = (df["newbalanceDest"] - df["oldbalanceDest"]) / df["oldbalanceDest"]
print(df.head())

print(df.groupby("isFraud")[["amount", "varBalanceOrg", "varBalanceDest"]].mean())
#show(df)