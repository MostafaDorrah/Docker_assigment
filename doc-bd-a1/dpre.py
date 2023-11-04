import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def out_remove(col_name,df,cond,m):
    quartile1 = df[col_name].quantile(0.25)
    quartile3 = df[col_name].quantile(0.75)
    iqr = quartile3 - quartile1
    upper = quartile3 + m * iqr
    lower = quartile1 - m * iqr
    if(cond=='both'):
        new_df = df[(df[col_name] < upper) & (df[col_name] > lower)]
    elif(cond=='lower'):
        new_df = df[(df[col_name] > lower)]
    else:
        new_df = df[(df[col_name] < upper)]
    return new_df


def equal_width_discretization(df, column, bins):
    df[column] = pd.cut(df[column], bins=bins, labels=False, retbins=False)
    return df

def equal_frequency_discretization(df, column, quantiles):
    df[column] = pd.qcut(df[column], q=quantiles, labels=False, duplicates='drop')
    return df


def cleaning(df):
    
    #Data Cleaning & Data Reduction
    
    #Nulls
    df.iloc[:,:-1] = df.iloc[:,:-1].replace(0,np.nan)
    df = df.dropna()
    
    #Feature selection
    df = df.drop(['Insulin', 'Pregnancies'], axis=1)
    
    #Outliers
    df = out_remove('Glucose',df,'both',1.5)
    df = out_remove('BloodPressure',df,'lower',1.5)
    
    # Data Transformation
    
    X = df.drop('Outcome', axis=1)
    y = df['Outcome']
    
    # Z-score Normalization
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Min-Max Normalization
    min_max_scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_scaled)
    
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)
    df = pd.concat([X_scaled_df, y.reset_index(drop=True)], axis=1)
    
    # Data Discretization
    
    # equal width discretization
    df = equal_width_discretization(df, 'Glucose', 4)
    
    # equal frequency discretization
    df = equal_frequency_discretization(df, 'BloodPressure', 4)

    df.to_csv("res_dpre.csv")
    
    return df

