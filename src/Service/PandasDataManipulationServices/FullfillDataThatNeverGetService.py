import pandas as pd
from datetime import datetime

class FullfillDataThatNeverGetService:
    def fullfill(self, df):
        print("Fullfilling data that never get")
        
        # Converte objetos bson.timestamp.Timestamp em objetos datetime
        df['Time'] = df['Time'].apply(lambda x: x.as_datetime() if isinstance(x, bson.timestamp.Timestamp) else x)
        
        df['Time'] = pd.to_datetime(df['Time'])
        df = df.set_index('Time')

        # Group data by the index, calculate the mean of the values within each group, and then resample the DataFrame
        df = df.groupby(df.index).mean().resample('S').asfreq()
        print(df)
        return df
