import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv("./data/fraude_mobile_phone_ech_train_2021.csv")

profile = df.profile_report(title="Scoring", minimal=True)
profile.to_file("./exports/output.html")