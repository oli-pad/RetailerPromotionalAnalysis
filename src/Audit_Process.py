import os
import pyodbc
import pandas as pd


def Audit_Process(Client_Code,Retailer_Code,Date_period_1,Date_period_2,SCC_alt):

    generate_arg=r'python C:\Users\python\Desktop\RetailerPromotionalAnalysis\src\Promo_reconciliation.py {} {} {} {} {}'


    os.system(generate_arg.format(Client_Code,Retailer_Code,Date_period_1,Date_period_2,SCC_alt))
    
