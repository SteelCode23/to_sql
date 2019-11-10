def to_sqlserver(
        frame,
        name,
        con,
        schema=None,
        if_exists="fail",
        index=True,
        index_label=None,
        chunksize=None,
        dtype=None,
        method=None,
):
    create_sql = " DROP TABLE IF EXISTS " + str(name) + " CREATE TABLE " + str(name) + " ( "
    col = frame.columns.tolist()
    for counter, colname in enumerate(col):
        if counter < len(col) - 1:
            create_sql = create_sql + "[" + str(colname) + "]" + " VARCHAR(MAX) ,"
        else:
            create_sql = create_sql + "[" + str(colname) + "]" + " VARCHAR(MAX))"
    con.execute(create_sql)

    insert_sql = "INSERT INTO " + str(name) + " ( "
    col = frame.columns.tolist()
    for counter, colname in enumerate(col):
        if counter < len(col) - 1:
            insert_sql = insert_sql + "[" + str(colname) + "]" + ","
        else:
            insert_sql = insert_sql + "[" + str(colname) + "]" + ") VALUES "

    all_lists = frame.columns.tolist()
    _values_store_ = []
    for i in all_lists:
        stri = [str(i).replace("'", '"') for i in frame[i].tolist()]
        _values_store_.append(stri)
    _sql_ = []
    _exec_insert_sql_ = []

    _greater_than_1000_rows_query_builder = insert_sql
    # 1000 is the current values limit for SQL Server.
    if len(_values_store_[0]) > 1000:
        for counter, items in enumerate(zip(*_values_store_[:len(_values_store_[0])])):
            _sql_.append(str(items) + ',')
            if counter % 1000 == 0:
                _greater_than_1000_rows_query_builder = insert_sql
                _greater_than_1000_rows_query_builder = _greater_than_1000_rows_query_builder + ''.join(_sql_)
                _sql_ = []
            _exec_insert_sql_.append(new)
    else:
        for counter, items in enumerate(zip(*_values_store_[:len(_values_store_)])):
            _sql_.append(str(items) + ',')
        _exec_insert_sql_ = [insert_sql + ''.join(_sql_)]

    # Insert Data Into Table
    for link in _exec_insert_sql_:
        # The logic leaves a comma at the end. Strip it off to create valid T-SQL.
        con.execute(str(link[:-1]))
    con.close()
