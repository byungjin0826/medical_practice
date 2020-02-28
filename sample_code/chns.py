import pandas as pd


df = pd.read_sas('./data/CHNS/biomarker_09.sas7bdat')


# Index(['IDind', 'UREA', 'UA', 'APO_A', 'LP_A', 'HS_CRP', 'CRE', 'HDL_C',
#        'LDL_C', 'APO_B', 'MG', 'FET', 'INS', 'HGB', 'WBC', 'RBC', 'PLT',
#        'Glu_field', 'Y48_2', 'Y48_3', 'Y48_4', 'Y48_5', 'Y48_6', 'HbA1c', 'TP',
#        'ALB', 'GLUCOSE', 'TG', 'TC', 'ALT', 'TRF', 'TRF_R', 'CRE_MG', 'UA_MG',
#        'UREA_MG', 'MG_MG', 'TC_MG', 'Y48_5MG', 'TG_MG', 'Y48_6MG', 'HDL_C_MG',
#        'LDL_C_MG', 'Glu_field_MG', 'GLUCOSE_MG', 'APO_A_MG', 'APO_B_MG',
#        'TRF_MG', 'Y46_1DL', 'wave'],
#       dtype='object')

a = df.loc[df.IDind == 211101003002, :]
