from src.Audit_Process import Audit_Process
from src.Audit_Process_ALL import Audit_Process_All

import pyodbc

import sys

script,client_code,retailer_code,date_period_1,date_period_2,SCC_alt=sys.argv

def main():
    if client_code == "All":
        Audit_Process_All()
    elif retailer_code == "All":
        Audit_Process_All()
    else:
        Audit_Process(get_client_list(client_code.upper()),get_retailer_list(retailer_code),date_period_1,date_period_2,SCC_alt)

def get_retailer_list(retailer_name):
    conn = pyodbc.connect('DRIVER=SQL Server;SERVER=UKSALAZSQL;DATABASE=Salitix_Master_Data;Trusted_Connection=Yes;UID=SALITIX\SQLSalitixAuditorUsers')
    cursor = conn.cursor()
    cursor.execute("SELECT salitix_customer_number FROM [Salitix_Master_Data].[dbo].[salitix_customer_numbers] WHERE [Active_Status] = 'Y' and Salitix_customer_short_name = '"+str(retailer_name)+"';")
    User_List=cursor.fetchall()
    retailer_names=[User_List[i][0] for i in range(len(User_List))]
    return retailer_names[0]

def get_client_list(client_name):
    conn = pyodbc.connect('DRIVER=SQL Server;SERVER=UKSALAZSQL;DATABASE=Salitix_Master_Data;Trusted_Connection=Yes;UID=SALITIX\SQLSalitixAuditorUsers')
    cursor = conn.cursor()
    cursor.execute("SELECT Salitix_client_number FROM [Salitix_Master_Data].[dbo].[salitix_client_numbers] WHERE [Active_Status] = 'Y' and Salitix_client_name = '"+str(client_name)+"';")
    User_List=cursor.fetchall()
    retailer_names=[User_List[i][0] for i in range(len(User_List))]
    return retailer_names[0]


if __name__ == "__main__":
    main()