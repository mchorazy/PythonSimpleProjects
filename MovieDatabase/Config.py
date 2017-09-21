from configparser import ConfigParser

def config(filename='MovieDatabase/config/dbConfig.ini', section='postgresql'):
    """Import database config from .ini file
    Section: postgresql
    Parameters: host, database, user, password"""
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db