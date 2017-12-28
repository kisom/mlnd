import pandas

def prepare_dataframe(path):
    df = pandas.read_csv(path, sep='\t', header=None, names=['label', 'text'])
    df['label'] = df.label.map({'ham':0, 'spam':1})
    
    # TODO: count vector
    
    # TODO: frequency
    return df