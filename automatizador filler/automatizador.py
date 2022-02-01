import pandas as pd
# abre o arquivo excel
df = pd.read_csv ('filler.csv')
print (df)
sql = ''
for row in df.itertuples(): # itertuples() retorna uma tupla com todas as linhas do dataframe
    sql += "INSERT INTO tabela (area_id, store_id, date, exposure, engagement, stopping_power) VALUES ('{}', '{}', '{}', '{}', '{}', '{}');\n".format(row.area_id, row.store_id, row.date, row.exposure, row.engagement, row.stopping_power)

#open ('caminho do arquivo', 'r').read(sql)
open ('caminho do arquivo', 'w').write(sql)





