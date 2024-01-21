
# %% 

import fundamentus
from pandasql import sqldf
import pandas as pd
import seaborn as sns

# %% 

df = fundamentus.get_resultado()

df.columns.name = None
df.index.name = None
df = df.reset_index()
df = df.rename(columns={"index" : "ticker"})


# %%
query = "SELECT * FROM df"
sqldf(query,globals())

# %%

query = f"""SELECT 
        ticker,cotacao,pl,pvp,dy,roe,liq2m,divbpatr,c5y 
    FROM 
        df 
    WHERE 
        pl BETWEEN 2.5 AND 10
    AND 
        pvp BETWEEN 0.5 AND 2
    AND 
        dy BETWEEN 0.07 AND 0.15
    AND 
        roe BETWEEN .10 AND 0.35
    AND 
        liq2m > 1000000 
    AND 
        divbpatr < 1.5
    AND 
        c5y > 0.10"""

sqldf(query,globals())
# sqldf(query, env=None)

# %%
df = fundamentus.get_resultado_raw()
df.head()