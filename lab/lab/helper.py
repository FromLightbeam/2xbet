
def fetch_one_dict_from_cursor(cursor):
    row_data = cursor.fetchone()
    row_desc = cursor.description
    row_name = [ r[0].lower() for r in row_desc ]
    
    return dict(zip(row_name, row_data))

def fetch_many_dict_from_cursor(cursor):
    rows_data = cursor.fetchall()
    row_desc = cursor.description
    row_name = [ r[0].lower() for r in row_desc ]
    
    return [ dict(zip(row_name, row_data)) for row_data in rows_data ]

# def fetch_many_dict_from_cursor_with_dublicate_name_column(cursor):
#     rows_data = cursor.fetchall()
#     row_desc = cursor.description
#     print(row_desc)
   
#     row_name = [ r[0].lower() for r in row_desc ]
    
#     return [ dict(zip(row_name, row_data)) for row_data in rows_data ]