import pandas as pd
s2={'col1':[1,2,3,4],'col2':[8,9,6,7],'col3':[3,4,5,9]}
s1=pd.DataFrame(s2)
df2 = s1.iloc[:, 0]
print(df2)