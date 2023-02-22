def compact_columns(df, num_cols = 5, col_width = 25):
    cols = list(df.columns)
    row_string = ''
    for k, c in enumerate(cols):
        row_item = f"{c} {(col_width - len(c))*' '}"
        row_string = row_string + row_item
        
        if (k+1)%num_cols==0:
            print(row_string)
            row_string = ''
    print(row_string)                  
    return 

def clean_columns(df, suffix, inplace = False):
    column_list = list(df.columns.values)
    purge_list = [col for col in column_list if suffix in col]
    df = df.drop(columns = purge_list)
    return df