# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# !pip3 install dateparser
# !pip3 install lxml 


# %%
import requests
import pandas as pd
import dateparser


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
df


# %%
df.to_csv('injuries.csv')


