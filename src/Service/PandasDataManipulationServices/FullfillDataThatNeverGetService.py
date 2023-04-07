import pandas as pd
from datetime import datetime

class FullfillDataThatNeverGetService:
    def fullfill(self, filePathCsv):
        df = pd.read_csv(filePathCsv)
        
        df['Time'] = pd.to_datetime(df['Time'])

        df = df.set_index('Time')

        print(df)

        df = df.resample('1S').mean()

        #back data to original format
        df = df.reset_index()
        

        print(df)

        return df
