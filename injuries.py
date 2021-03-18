# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import pandas as pd



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
df.to_csv('injuries.csv')
