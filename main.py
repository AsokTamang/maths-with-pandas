#so for viewing data based on the specific threshold ,
#we must use the horizontal barchart if the number of categories are many or we can also use the vertical barchart

#but for viewing the continuous datas, we must use the line chart or line graph.

import pandas as pd
df = pd.read_csv("C:/Users/ashok/Downloads/chapter4_assets/chapter4_assets/4_shoe_sale_analysis/shoe_sales.csv")

print(df[df.sold_qty<12.25].shape)

df_new=df[df['sold_qty']>19.75].sort_values('sold_qty')
print(df_new)
print(df_new['sold_qty'].quantile(0.5))  #finding the 50th percentile value among the sold_qty dataset having higher value or equal to the 90th percentile value among total sold qty dataset


###NIKE ANALYSIS
df_nike=df[df['brand']=='Nike']
df_nike.fillna(0,inplace=True)
print(df_nike)
fiftyth_value=df_nike['sold_qty'].quantile(0.5).astype(int)
print(fiftyth_value)

df_nike2=df[df['brand']=='Nike']
df_nike2.isnull()

print(df_nike2[df_nike2['sold_qty'].isnull()])




