def getNCM(local_url):
    import sys, subprocess
    #checa se a biblioteca já está instalada.
    if 'pandas' not in sys.modules:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
    #cria um dicionário de NCMs com 4 números e descrição (para conversão em massa de termos em
    # relatórios)
    import pandas as pd
    #lê o aquivo de ncm direto do ministério de comério exterior
    file = pd.read_csv('http://www.mdic.gov.br/balanca/bd/tabelas/NCM.csv',sep=';',encoding='cp1252')

    #selecionando os 4 primeiros números do ncm - o HS code americano não possui a quantidade de números
    #que temos, portanto será feita a redução em ambos para 4
    file['CO_NCM'] = file['CO_NCM'].astype(str).apply(lambda x:x[:4])

    #seleciona as colunas NCM e descrição
    final_dic = file[['CO_NCM','NO_NCM_ING']]
    #inserir o local de salvamento do arquivo
    final_dic.to_excel(local_url)
    
def getHS(local_url):
    import sys, subprocess
    #checa se a biblioteca já está instalada
    if 'pandas' not in sys.modules:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
    #cria um dicionário de NCMs com 4 números e descrição (para conversão em massa de termos em
    # relatórios)
    import pandas as pd
    #lê o aquivo de ncm direto do ministério de comério exterior
    file = pd.read_csv('http://www.mdic.gov.br/balanca/bd/tabelas/NCM_SH.csv',sep=';',encoding='cp1252')

    #selecionando os 4 primeiros números do ncm - o HS code americano não possui a quantidade de números
    #que temos, portanto será feita a redução em ambos para 4
    file['CO_SH6'] = file['CO_SH6'].astype(str).apply(lambda x:x[:4])

    #seleciona as colunas NCM e descrição
    final_dic = file[['CO_SH6','NO_SEC_ING']]
    #inserir o local de salvamento do arquivo
    final_dic.to_excel(local_url)
