import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

def visal(df):
    plt.figure(figsize=(8,4),dpi=110)
    sns.scatterplot(data=df, x='BMI', y='SkinThickness', color='darkblue');
    plt.plot([18, 47], [0, 55], 'red', linewidth=4)
    plt.xlim(20, 60)
    plt.ylim(4, 60)
    plt.savefig("vis.png") 
 