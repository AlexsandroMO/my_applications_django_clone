import numpy as np
import pandas as pd
import pandasql as ps
import sqlite3
from datetime import datetime
import xlrd
import excel

def DbDb():
    def read_sql_agency(): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM insurance_agency;
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_sql_prod(): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM insurance_product;
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    # def read_sql_secure(): #Information Tables Read
    #     conn = sqlite3.connect('db.sqlite3')
    #     sql_datas = f"""
    #                 SELECT * FROM insurance_secure;
    #     """

    #     read_db = pd.read_sql_query(sql_datas, conn)
    #     conn.close()
        
    #     return read_db


    def cria_cliente(prod_id_name, name, secure_id_name, cpf, cnpj, agency_id_name, policy, amount_paid,date_contract, tel1, cel1, tel2, cel2, comments, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO insurance_cliente(name,cpf,cnpj,conta,gerency,policy,amount_paid,tel1,tel2,cel1,cel2,email,comments,date_contract,update_at,create_at,agency_id,prod_id,secure_id)
                    VALUES ('{name}','{cpf}','{cnpj}','','','{policy}','{amount_paid}','{tel1}','{tel2}','{cel1}','{cel2}','','{comments}','{date_contract}','{date_today}','{date_today}','{agency_id_name}','{prod_id_name}','{secure_id_name}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    df = pd.read_excel('media/RENOVACAO.xlsx')
    df = df[['PRODUTO', 'NOME_CLIENTE', 'TIPO_SEGURO', 'CPF', 'AG', 'APOLICE', 'VALOR', 'DATA',
            'TEL1', 'CEL1', 'TEL2', 'CEL2','OBS']]

    body = ['PRODUTO', 'NOME_CLIENTE', 'TIPO_SEGURO', 'CPF', 'AG', 'APOLICE', 'VALOR', 'DATA',
            'TEL1', 'CEL1', 'TEL2', 'CEL2','OBS']

    header = ['prod_id_name', 'name', 'secure_id_name', 'cpf', 'agency_id_name','policy', 'amount_paid',
            'date_contract', 'tel1', 'cel1', 'tel2', 'cel2', 'comments', ]

    for i in range(len(body)):
        df.rename(columns={body[i]:header[i]}, inplace=True)

    df['cnpj'] = ''
    df['conta'] = ''
    df['gerency'] = ''
    df['email'] = ''

    df.fillna('', inplace=True)

    for a in range(len(df['cpf'])):
        if len(str(df['cpf'].loc[a])) > 11:
            df['cnpj'].loc[a] = str(df['cpf'].loc[a])
            df['cpf'].loc[a] = str(df['cpf'].loc[a])

            df['tel1'].loc[a] = str(df['tel1'].loc[a])[:len(str(df['tel1'].loc[a]))-2]
            df['tel2'].loc[a] = str(df['tel2'].loc[a])[:len(str(df['tel2'].loc[a]))-2]
            df['cel1'].loc[a] = str(df['cel1'].loc[a])[:len(str(df['cel1'].loc[a]))-2]
            df['cel2'].loc[a] = str(df['cel2'].loc[a])[:len(str(df['cel2'].loc[a]))-2]
        else:
            df['tel1'].loc[a] = str(df['tel1'].loc[a])[:len(str(df['tel1'].loc[a]))-2]
            df['tel2'].loc[a] = str(df['tel2'].loc[a])[:len(str(df['tel2'].loc[a]))-2]
            df['cel1'].loc[a] = str(df['cel1'].loc[a])[:len(str(df['cel1'].loc[a]))-2]
            df['cel2'].loc[a] = str(df['cel2'].loc[a])[:len(str(df['cel2'].loc[a]))-2]

    df['agency_id_name'] = df['agency_id_name'].astype(str)
    df['prod_id_name'] = df['prod_id_name'].astype(str)
    df['secure_id_name'] = df['secure_id_name'].astype(str)
    df['date_contract'] = df['date_contract'].astype(str)

    date_today = datetime.today()

    for a in range(len(df['name'])):
        name = df['name'].loc[a]
        cpf = df['cpf'].loc[a]
        cnpj = df['cnpj'].loc[a]
        policy = df['policy'].loc[a]
        amount_paid = df['amount_paid'].loc[a]
        tel1 = df['tel1'].loc[a]
        tel2 = df['tel2'].loc[a]
        cel1 = df['cel1'].loc[a]
        cel2 = df['cel2'].loc[a]
        #email = df['email'].loc[a]
        comments = df['comments'].loc[a]
        str_date = df['date_contract'].loc[a]
        date_contract = datetime.strptime(str_date, '%Y-%m-%d').date()

        agency_id_name = ''
        prod_id_name = ''

        for ag in range(len(read_sql_agency()['name_agency'])):
            if read_sql_agency()['name_agency'].loc[ag] == df['agency_id_name'].loc[a]:
                agency_id_name = read_sql_agency()['id'].loc[ag]

        for prod in range(len(read_sql_prod()['name_product'])):
            if read_sql_prod()['name_product'].loc[prod] == df['prod_id_name'].loc[a]:
                prod_id_name = read_sql_prod()['id'].loc[prod]

        secure_id_name = 1

        cria_cliente(prod_id_name, name, secure_id_name, cpf, cnpj, agency_id_name,policy, amount_paid,date_contract, tel1, cel1, tel2, cel2, comments, date_today)


    print('Feito!')