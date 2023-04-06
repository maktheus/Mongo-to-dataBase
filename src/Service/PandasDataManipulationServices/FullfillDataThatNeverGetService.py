import pandas as pd
import numpy as np

class FullfillDataThatNeverGetService:
    def fullfill(self, df):
        print("Fullfilling data that never get")
        df['Time'] = pd.to_datetime(df['Time'])
        df = df.set_index('Time')

        # Reamostrar DataFrame para frequência horária e preencher valores ausentes com NaN
        df = df.resample('S').asfreq()

        return df
