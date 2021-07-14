import pandas as pd
import numpy as np


class DataInfo:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_size(self):
        value = self.df.shape
        return value
    
    def get_no_datapoints(self):
        #value = self.df.shape
        print(f' There are {self.df.shape[0]} rows and {self.df.shape[1]} columns presnet in this data')
        return
 
    def get_column_names(self):
        print('Columns in the data are: ')
        return self.df.columns.tolist()
    
    def get_info(self):
        return self.df.info()
    
    def get_description(self):
        print('Descriptive statistics: ')
        return self.df.describe()
    
    def get_total_missing_values(self):
        missing = self.df.isnull().sum().sum()
        print(f'The number of missing value(s): {missing}')
        return
    
    def get_percentage_missing_values(self):
        total_cells = np.product(self.df.shape) # calculate total number of cells in dataframe
        total_missing_count = self.df.isnull().sum().sum() # calculate total number of missing values
        # calculate percentage missing
        print('There are', round(((total_missing_count/total_cells) * 100), 2), '%', 'missing values.')
        return
    
    def get_missing_columns(self):
        missing_columns = self.df.columns[self.df.isnull().any()]
        print(f'Columns having missing value(s): {missing_columns}')
        return
    
    def get_percentage_missing_columns(self):
        '''a function to check for missing values count and percentage missing'''
    
        count_missing = self.df.isnull().sum() # calculate total sum of missing data
        count_missing_percentage= round((self.df.isnull().sum()*100/len(self.df))) # multiply sum of missing data by 100 and divide by length of the whole data and round up 
        missing_column_name= self.df.columns 
        missing_df=pd.DataFrame(zip(count_missing,count_missing_percentage,missing_column_name),
                           columns=['Missing Count', '%Missing', 'ColumnName']) # create a dataframe 
        missing_df = missing_df.set_index('ColumnName') # set missing columns as index
        return missing_df
    
    def get_duplicates(self):
        return self.df[self.df.duplicated()]