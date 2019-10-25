from SourceLauren import *
import pandas as pd

# pd.set_option('display.max_columns', 50)
# pd.set_option('display.width', 150)

path = qatmFile

###
# Column formatting

col = ['Inspection Lot', 'Material', 'Batch object', 'QATM', 'Short text', 'Result', 'Lower spec.', 'Upper spec.',
       'Sample Insp.Point', 'Insp.date Sample', 'Sample ID', 'Timestamp']

col_new = {'Inspection Lot':'Inspection_Lot', 'Batch object':'Batch', 'Short text':'Short_text', 'Lower spec.':'LSL', 'Upper spec.':'USL',
       'Sample Insp.Point':'Insp_Point', 'Insp.date Sample':'Insp_Date', 'Sample ID':'Sample_ID'}

###
# Collecting Data

df_og = pd.read_csv(path, sep='\t', skiprows=15, skip_blank_lines=True, encoding='windows-1252', usecols=col)
df = df_og.rename(col_new, axis=1)

###
#

print(df.head())