import spacy
import pandas as pd
import neuralcoref    

nlp = spacy.load("en_core_web_sm")
neuralcoref.add_to_pipe(nlp)

df = pd.read_csv('nlp_restaurant_reviews1.csv', header=None)
df = df.iloc[:, 0]
df = pd.DataFrame(df)
df.rename(columns = {0:'text'}, inplace = True) 

resolved = []


for i in range(len(df)):
    doc = nlp(df.iloc[i, 0])
    resolved.append(doc._.coref_resolved)
    
df['resolved'] = resolved
df.to_csv('resolved_data.csv', index=False)