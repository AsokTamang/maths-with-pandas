import pandas as pd
import openpyxl

df_xl = pd.read_excel("C:/Users/ashok/Downloads/chapter4_assets/chapter4_assets/7_outlier_detection_using_iqr_boxplot/region_wise_sales.xlsx")

region_names = df_xl.Region.unique()
total_value = [df_xl[df_xl['Region'] == region].Sales for region in region_names]


df_apac = df_xl[df_xl['Region'] == 'APAC']
df_euro = df_xl[df_xl['Region'] == 'Europe']
df_america = df_xl[df_xl['Region'] == 'Americas']


def get_third_first_quartile(data):
    q1,q3 = data.Sales.quantile([0.25,0.75])
    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    return lower_limit, upper_limit



lower_limit,upper_limit = get_third_first_quartile(df_apac)
print(lower_limit,upper_limit)
outliersap = df_apac[(df_apac['Sales']<lower_limit) | (df_apac['Sales']>upper_limit)]
print(outliersap)



lower_limit_e , upper_limit_e = get_third_first_quartile(df_euro)
outlierse = df_euro[(df_euro['Sales']<lower_limit_e) | (df_euro['Sales']>upper_limit_e)]
print(outlierse)


