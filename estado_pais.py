def getCountryInfo(pais):
    import sys, subprocess
    #checa se a biblioteca já está instalada
    if 'pandas' not in sys.modules:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
        
    import pandas as pd
    file = pd.read_csv('http://www.mdic.gov.br/balanca/bd/tabelas/PAIS.csv',sep=';',encoding='cp1252')
    print(file[file['NO_PAIS'].astype(str).apply(lambda x:pais in x)][['CO_PAIS','CO_PAIS_ISON3','CO_PAIS_ISOA3','NO_PAIS_ING','NO_PAIS']].reset_index(drop=True))

def searchDist(municipio):
    import sys, subprocess
    #checa se a biblioteca já está instalada
    if 'pandas' not in sys.modules:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas'])
    import pandas as pd
    mun = pd.read_csv('http://www.mdic.gov.br/balanca/bd/tabelas/UF_MUN.csv',sep=';',encoding='cp1252')
    uf = pd.read_csv('http://www.mdic.gov.br/balanca/bd/tabelas/UF.csv',sep=';',encoding='cp1252')
    file = mun.set_index('SG_UF').join(uf.set_index('SG_UF')).reset_index()
    print(file[file['NO_MUN_MIN'].astype(str).apply(lambda x:municipio in x)][['SG_UF','CO_MUN_GEO','NO_MUN','CO_UF','NO_REGIAO']].reset_index(drop=True))
