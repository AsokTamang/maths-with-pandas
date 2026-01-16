#so for viewing data based on the specific threshold ,
#we must use the horizontal barchart if the number of categories are many or we can also use the vertical barchart

#but for viewing the continuous datas, we must use the line chart or line graph.

import pandas as pd
df = pd.read_csv("C:/Users/ashok/Downloads/chapter4_assets/chapter4_assets/4_shoe_sale_analysis/shoe_sales.csv")

print(df[df.sold_qty<12.25].shape)

df_new=df[df['sold_qty']>19.75].sort_values('sold_qty')
print(df_new)