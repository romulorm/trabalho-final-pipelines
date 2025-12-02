"""
Pipeline - Etapa 1: Carregar e Explorar Dados
"""

import pandas as pd


def carregar_dados(caminho_arquivo):
    """
    Carrega o dataset de clientes.
    
    Args:
        caminho_arquivo: caminho para o CSV
        
    Returns:
        DataFrame com os dados
    """
    # TODO 1: Use pd.read_csv() para carregar o arquivo
    # Dica: df = pd.read_csv(caminho_arquivo)
    
    print("=" * 50)
    print("              1. CARREGANDO DADOS")
    print("=" * 50)

    try:
        # 1. Tenta carregar o arquivo CSV
        df = pd.read_csv(caminho_arquivo)
        print(f"✅ Dados carregados do arquivo: {caminho_arquivo}")
        return df
    
    except FileNotFoundError:
        # 2. Verifica se o arquivo não foi encontrado
        print(f"❌ Erro: Arquivo não encontrado: {caminho_arquivo}")
        print("Verifique o caminho e o nome do arquivo.")
        return None
        
    except pd.errors.EmptyDataError:
        # 3. Verifica se o arquivo está vazio
        print(f"❌ Erro: O arquivo {caminho_arquivo} está vazio.")
        return None
        
    except pd.errors.ParserEror:
        # 4. Verifica se há erro de parsing (formato incorreto)
        print(f"❌ Erro: Falha no parse do arquivo {caminho_arquivo}. O arquivo pode estar corrompido ou com diferente delimitador.")
        return None
        
    except Exception as e:
        # 5. Verifica qualquer outro erro inesperado
        print(f"❌ Um erro inesperado ocorreu: {e}")
        return None



def explorar_dados(df):
    """
    Mostra informações básicas sobre o dataset.
    
    Args:
        df: DataFrame a ser explorado
    """
    print("")
    print("=" * 50)
    print("              EXPLORAÇÃO DOS DADOS")
    print("=" * 50)
        
    # TODO 2: Mostre o shape do DataFrame (linhas, colunas)
    # Dica: print(f"Shape: {df.shape}")
    
    print("\n2. DATASET SHAPE")
    print("-" * 30)
    print(f"Shape: {df.shape}")
    

    # TODO 3: Mostre os tipos de cada coluna
    # Dica: print(df.dtypes)

    print("")
    print("\n3. TIPOS DAS COLUNAS")
    print("-" * 30)
    print(df.dtypes)
    
    # TODO 4: Mostre as 5 primeiras linhas
    # Dica: print(df.head())

    print("")
    print("\n4. PRIMEIRAS 5 LINHAS DO DATAFRAME")
    print("-" * 30)
    print(df.head())


def verificar_target(df, coluna_target='respondeu_campanha'):
    """
    Verifica a distribuição da variável target.
    
    Args:
        df: DataFrame
        coluna_target: nome da coluna target
    """
    print("")
    print("")
    print("=" * 50)
    print("              DISTRIBUIÇÃO DO TARGET")
    print("=" * 50)
    
    # TODO 5: Mostre a contagem de cada valor do target
    # Dica: print(df[coluna_target].value_counts())
    
    print("")
    print("\n5. CONTAGEM DO TARGET")
    print("-" * 30)
    print(df['respondeu_campanha'].value_counts())
    
    # TODO 6: Mostre a proporção (percentual) de cada valor
    # Dica: print(df[coluna_target].value_counts(normalize=True))
    
    print("")
    print("\n6. PROPORÇÃO DO TARGET")
    print("-" * 30)
    print(df['respondeu_campanha'].value_counts(normalize=True))


# Teste local (executar este arquivo diretamente)
if __name__ == "__main__":
    df = carregar_dados("data/clientes_campanha.csv")
    if df is not None:
        explorar_dados(df)
        verificar_target(df)
    else:
        print("ERRO: DataFrame não foi carregado. Complete o TODO 1!")
