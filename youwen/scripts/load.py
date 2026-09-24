import json,glob,re,pickle
D=[]
for f in glob.glob('shuowen/data/*.json'):
    D.append(json.load(open(f)))
pickle.dump(D,open('sw.pkl','wb'))
print(len(D))
