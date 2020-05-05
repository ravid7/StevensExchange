from yahoo_fin.options import *
import requests
import pandas as pd
import ftplib
import io
import re  

def force_float(elt):
    
    try:
        return float(elt)
    except:
        return elt

def get_top_crypto(count):
    
    '''Gets the top 100 Cryptocurrencies by Market Cap'''      

    session = HTMLSession()
    
    resp = session.get(f"https://finance.yahoo.com/cryptocurrencies?offset=0&count={count}")
    
    tables = pd.read_html(resp.html.raw_html)               
                    
    df = tables[0].copy()

    
    df["% Change"] = df["% Change"].map(lambda x: float(x.strip("%").\
                                                          strip("+").\
                                                          replace(",", "")))
    del df["52 Week Range"]
    del df["1 Day Chart"]
    
    fields_to_change = [x for x in df.columns.tolist() if "Volume" in x \
                        or x == "Market Cap" or x == "Circulating Supply"]
    
    for field in fields_to_change:
        
        if type(df[field][0]) == str:
            df[field] = df[field].str.strip("B").map(force_float)
            df[field] = df[field].map(lambda x: x if type(x) == str 
                                                else x * 1000000000)
            
            df[field] = df[field].map(lambda x: x if type(x) == float else
                                    force_float(x.strip("M")) * 1000000)
            
            
    session.close()        
                
    return df