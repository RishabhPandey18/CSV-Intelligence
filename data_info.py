import pandas as pd

def analyze_data(uploaded_file):
    # read csv
    df = pd.read_csv(uploaded_file)

    # calculate row and columns 
    row = df.shape[0]
    columns = df.shape[1]
#    row and columns, duplicate value, colummns name, missing values ,
  
# this return the names of columns
    col_name = df.columns.tolist()
#data tuype
    data_type = df.dtypes
    
# print duplicate values 
    duplicate = df.duplicated().sum()
    
    # missing values
    mis_val = df.isnull().sum()
    
    # unique values 
    uniq_val = df.nunique()
    
    # statics
    number = df.select_dtypes(include="number")
    stats_uniq = number.describe()
    
    
    return {
        "data" : df,
        "number of rows " : row,
        "Number of columns " : columns,
        "names of Columns " : col_name,
        "Types of data " : data_type,
        "Duplicate values " : duplicate,
        "Missing  Values " : mis_val,
        "Unique values" : uniq_val,
        "Some Statics information " : stats_uniq
           
    }
    
