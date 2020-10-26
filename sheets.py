import pandas as pd

def read_google_sheet(key, sheet=None):
    url = 'https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv'.format(key)
    
    if sheet is not None:
        url = url + '&sheet={}'.format(sheet)
        
    return pd.read_csv(url)