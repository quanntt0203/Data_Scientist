import pandas as pd

def extract_code(val:str) -> str:
    if val[:1]=='0':
        return val[1:3]
    else:
        return val[:2]

def display_phone(val):
    cities = ['24', '28']
    new_val = val
    if val[:1]=='0':
        new_val = val[1:]

    city_code = new_val[:2]
    if city_code in cities:
        return '0{0} {1} {2}'.format(new_val[:2], new_val[2:6], new_val[6:])
    else:
        return '0{0} {1} {2}'.format(new_val[:2], new_val[2:5], new_val[5:])

##TODO:

file_to_load = "C:\\Users\\admin\\Downloads\\phone_number.txt"

some_values = ['90','91']

df = pd.read_csv(file_to_load, delimiter='\t', dtype=str)
#df['phone'] = pd.to_numeric(df['phone'])
#df.set_index(['phone','code'], drop=True)
#abc = df.filter(items= ['phone','code'])
print(df)

df['phone_len'] = df['phone'].apply(len)
df = df.loc[(df['phone_len']>=9) & (df['phone_len']<=11)]

df['code_2'] = df['phone'].apply(extract_code)
df['display_phone'] = df['phone'].apply(display_phone)

#print(df)
abc = df.loc[(df['code_2'].isin(some_values)) & (df['phone_len']>8) & (df['phone_len']<11)]
print(df)
