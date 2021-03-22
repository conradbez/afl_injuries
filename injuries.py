# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# !pip3 install dateparser
# !pip3 install lxml 


# %%
import requests
import pandas as pd
import dateparser
from datetime import datetime
from datetime import timedelta


# %%
r = requests.get('https://www.afl.com.au/news/564/afl-injury-list')
dfs = pd.read_html(r.text)


# %%
df = pd.DataFrame()
for df_part in dfs:
    updated_text = df_part.iloc[-1,0]
    df_part = df_part.iloc[:-1]
    date = updated_text[updated_text.find(':')+2:]
    df_part['Updated'] = date
    df = df.append(df_part)
df


# %%
df['DATE_BACK'] = df.apply(
    lambda x: 
    dateparser.parse(
        x['ESTIMATED RETURN'], 
        settings={
            'PREFER_DATES_FROM': 'future', 
            'PARSERS':['relative-time'], 
            'RELATIVE_BASE': dateparser.parse(x['Updated'])}, ), axis=1)


# %%
df['ESTIMATED RETURN'].unique()


# %%
df.loc[df['ESTIMATED RETURN'].isin([ 'Season', 'Indefinite']), 'DATE_BACK'] = datetime.strptime('01/01/24', '%d/%m/%y')

df.loc[df['ESTIMATED RETURN'].isin([ 'Test', 'TBC', 'TBA']), 'DATE_BACK'] = datetime.now().date()+timedelta(days=28)


# %%
df.to_csv('injuries.csv')


# %%



# %%



# %%



# %%



