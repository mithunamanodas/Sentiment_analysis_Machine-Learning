import pickle as pkl
import pandas as pd
with open("countVect_imdb.pkl", "rb") as f:
    object = pkl.load(f)
    
df = pd.DataFrame(list(object))
df.to_csv(r'imdb_data_file.csv')
