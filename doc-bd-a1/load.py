import pandas as pd
import sys
from dpre import cleaning
from vis import visal
from model import model

def reading_df(patho):
    df = pd.read_csv(patho)
    return df

if len(sys.argv) > 1:
    path_to_csv = sys.argv[1]
    df = reading_df(path_to_csv)

    visal(df)
    
    df = cleaning(df)

    model(df)

