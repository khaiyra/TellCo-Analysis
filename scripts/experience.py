import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, Normalizer, StandardScaler

class Data:
    def __init__(self, df: pd.DataFrame):
        self.df = df
     
    def fix_outlier(self, columns: list):
        for column in columns:
            self.df[column] = np.where(self.df[column] > self.df[column].quantile(
                    0.95), self.df[column].median(), self.df[column])
        return self.df
    
    def get_mode(self):
        mode = self.df.mode()
        actual_mode = mode.iloc[0, :]
        actual_mode.name = 'Mode'
        return actual_mode
    
    def get_min_max_of_column(self, col, range=1):
        sortedVal = np.sort(self.df[col].unique())
        top_df = pd.DataFrame(sortedVal[::-1][:range], columns=['Max Value/s'])
        bottom_df = pd.DataFrame(sortedVal[:range], columns=['Min Value/s'])
        info_df = pd.concat([top_df, bottom_df], axis=1)
        return info_df
    
    def standardize_column(self, column: str) -> pd.DataFrame:
        std_column_df = pd.DataFrame(self.df[column])
        std_column_values = std_column_df.values
        standardizer = StandardScaler()
        normalized_data = standardizer.fit_transform(std_column_values)
        self.df[column] = normalized_data

        return self.df