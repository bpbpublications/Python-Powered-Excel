import pandas as pd

df = pd.DataFrame({
    "region": ["East","West","East"],
    "value": [10,20,30]
})

df[df['region'] == 'East']          # works fine
df.query("region == 'East'")        # same result


df = pd.DataFrame({
    "region name": ["East","West","East"],
    "value": [10,20,30]
})

print(df[df["region name"]=="East"])          # works fine
print(df.query("region name == 'East'"))      # error (space in col name)
print(df.query("`region name` == 'East'"))    # works with backticks


# Both methods usually give the same result, 
# but .query() needs backticks for column names with 
# spaces or special characters, while Boolean masking always works.
