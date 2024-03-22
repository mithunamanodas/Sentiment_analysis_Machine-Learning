import pickle as pkl
import pandas as pd
with open("countVect_imdb.pkl", "rb") as f:
    file = pkl.load(f)
     
df = pd.DataFrame([file])
df.to_csv(r'filename.csv')
