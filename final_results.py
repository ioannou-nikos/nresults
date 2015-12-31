# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

if __name__ == "__main__":
    plt.rcParams['font.family'] = ['Arial'] #Set font family to arial so greek renders
    #Read the excel with the data in it
    df = pd.read_excel("FINALRESULTS.xlsx",parse_cols="A,C:E,H:N",index_col=[0,1,2,3])
    #Create the dataframes
    gDimoi = df.groupby(level=['PERIFEREIA','EKL_PERIF','DIMOS']).sum() #Συγκεντρωτικά Δήμων
    gEklPerif = df.groupby(level=['PERIFEREIA','EKL_PERIF']).sum() #Συγκεντρωτικά Εκλογικών Περιφερειών
    gPerif = df.groupby(level=['PERIFEREIA']).sum() #Συγκεντρωτικά Περιφερειών

    with PdfPages('All_final_results.pdf') as pdf:
        #Ανάλυση κατά Περιφέρεια ανά Εκλογική Περιφέρεια
        levels = gEklPerif.index.levels[0]
        for level in levels:
            gEklPerif.loc[level][['Meim','Mits','Tzi','Geor']].plot(kind='bar', figsize=(14,10), title=str(level))
            pdf.savefig()

        #Ανάλυση της Κεντρικής Μακεδονίας κατά Εκλογική Περιφέρεια ανά Δήμο
        pkm = gDimoi.query('PERIFEREIA == "PKM"')
        pkm = pkm.reset_index()
        pkm = pkm[['EKL_PERIF','DIMOS','Meim','Mits','Tzi','Geor']]
        pkm = pkm.set_index(['EKL_PERIF','DIMOS'])
        levels = pkm.index.levels[0]
        for level in levels:
            pkm.loc[level].plot(kind='bar',figsize=(14,10))
            pdf.savefig()