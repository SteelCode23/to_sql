def insert_sql(dataframe, table_name):
    """
    Generates SQL Statement to insert data from a pandas dataframe
    """
    sql = "INSERT INTO " + str(table_name) + " ( "
    col = dataframe.columns.tolist()
    for counter, colname in enumerate(col):
        if counter < len(col) - 1:
            sql = sql + "["  +  str(colname) + "]" + ","
        else:
            sql = sql + "["  +  str(colname) + "]" + ") VALUES "

    all_lists = _.columns.tolist()
    t = []
    for i in all_lists:
        stri = [str(i).replace("'", '"') for i in _[i].tolist()]
        t.append(stri)
    _sql_ = []
    output = []
    new = sql
    if len(t[0]) > 500:
        for counter, items in enumerate(zip(*t[:len(t[0])])):
            _sql_.append(str(items) + ',')
            if counter % 500 == 0:
                new = sql
                new = new + ''.join(_sql_)
                _sql_ = []
            output.append(new)
    else:
        for counter, items in enumerate(zip(*t[:len(t[0])])):
            _sql_.append(str(items) + ',')
        output = [sql + ''.join(_sql_)]
    return output


def create_sql(dataframe,table_name):
    """
    Generates CREATE SQL Statement from a pandas dataframe
    """
    sql = " DROP TABLE IF EXISTS " + str(table_name) + " CREATE TABLE " + str(table_name) + " ( "
    col = dataframe.columns.tolist()
    for counter, colname in enumerate(col):
        if counter < len(col)-1:
            sql = sql + "[" + str(colname)  + "]" + " VARCHAR(MAX) ,"
        else:
            sql = sql + "[" + str(colname)  + "]" + " VARCHAR(MAX))"

    return sql


def _run(file, table_name, server, database, username, password):
    import pandas as pd
    import pyodbc
    _ = pd.read_excel(file)
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    crsr = cnxn.cursor()
    crsr.execute(create_sql(_, table_name))
    sql = (insert_sql(_, 'File'))
    for link in sql:
        crsr.execute(str(link[:-1]))
        crsr.commit()
    cnxn.close()
