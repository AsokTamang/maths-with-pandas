import pandas as pd
import openpyxl

df_xl = pd.read_excel("C:/Users/ashok/Downloads/chapter4_assets/chapter4_assets/7_outlier_detection_using_iqr_boxplot/region_wise_sales.xlsx")
df_apac = df_xl[df_xl['Region'] == 'APAC']
df_euro = df_xl[df_xl['Region'] == 'Europe']
df_america = df_xl[df_xl['Region'] == 'Americas']
qap1,qap2,qap3 = df_apac.Sales.quantile([0.25,0.50,0.75])
IQRap= qap3-qap1
lower_limit = qap1 - (1.5 * IQRap)
upper_limit = qap3 + (1.5 * IQRap)
outliersap = df_apac[(df_apac['Sales']<lower_limit) | (df_apac['Sales']>upper_limit)]
print(outliersap)


qe1,qe2,qe3 = df_euro.Sales.quantile([0.25,0.50,0.75])
IQRe= qe3-qe1
lower_limit_e = qe1 - (1.5 * IQRe)
upper_limit_e = qe3 + (1.5 * IQRe)
outlierse = df_euro[(df_euro['Sales']<lower_limit_e) | (df_euro['Sales']>upper_limit_e)]
print(outlierse)

