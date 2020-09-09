import pandas as pd

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/03-05-2020.csv"
csv_0305 = pd.read_csv(url, index_col=0)
df.to_sql(table_name, conn, if_exists='append', index=False)


print(csv_0305.head())