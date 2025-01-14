def remove_null_values(data):
    data.dropna(inplace=True)

def split_overview(data):
    data['overview'] = data['overview'].apply(lambda x: x.split())

def remove_spaces(data, columns):
    for col in columns:
        data[col] = data[col].apply(lambda x: [i.replace(" ", "") for i in x])
