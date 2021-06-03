#Função que Limpa Nan e Textos indesejáveis:
    #IMPORTANTE!!-Testar essa função em datasets diferentes para validar o seu uso ou não
def clean_nan(df, bad_str):
    
    '''
    clean_nan(df = pd.DataFrame, bad_str = str)
    How to use/ Como utilizar:
    Recebe um DataFrame e um str indesejado dentro do mesmo, e retorna o DataFrame com 0 substituindo o texto e os       dados que são NaN.
    df recebe -> pd.DataFrame
    bad_str -> str
    
    df receive -> pd.DataFrame
    bad_str -> str

    {str(type_arg)[-5:-2]}
    '''

    type_arg = type(bad_str)
    if type(bad_str) is not str:        
        return(f'''

        Português Br:
        Houve um erro, bad_str é do tipo {str(type_arg)[-5:-2]}, tente novamente com um tipo str para bad_str!
        
        English US:
        Error, your bad_str type is a {str(type_arg)[-5:-2]} type , try one more time with a str!
        ''')
        
        return(f'Houve um erro, bad_str é do tipo {str(type_arg)[-5:-2]}, tente novamente com um tipo str para bad_str!')
    
    for i in df:
        ex = df[f'{i}'].tolist()
        ex2 = []
        for value in ex:
            z=value
            if value == bad_str:
                z=0
            elif type(value) is float and math.isnan(value) is True:
                z=0
            else:
                z=value
            ex2.append(z)
        df[f'{i}'] = ex2
        
    return df

source = clean_nan(source,2)
source
