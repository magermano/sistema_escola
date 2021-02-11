from configparser import ConfigParser

def config(filename='database.ini',section='postgresql'):
    #Cria um parser
    parser = ConfigParser()
    #Leia o arquivo de configuração
    parser.read(filename)

    #Pega a sessão, padrão para postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db