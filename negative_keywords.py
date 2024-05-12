import csv, json

search_terms_path = 'Search terms report.csv'
save_results_path = 'results.csv'

with open(search_terms_path,'r',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    keywords = [row for row in reader if reader.fieldnames[0] != None]
    keywords = json.loads(json.dumps(keywords))

terms = ['clean','wash','routine']
found = []

for term in terms:
    for i in range(0,len(keywords)):
        if term in keywords[i]['Search term']:
            if i not in found:
                found.append(i)

found.sort(reverse=True)

for i in found:
    del keywords[i]

cleaned_list = []
for kw in keywords:
    cleaned_list.append(kw['Search term'])

cleaned_list.sort()

with open(save_results_path,'a',newline="",encoding="utf-8") as f:
    writer = csv.DictWriter(f,fieldnames=["term"])
    for kw in cleaned_list:
        k = "[" + kw + "]"
        writer.writerow({'term':k})
