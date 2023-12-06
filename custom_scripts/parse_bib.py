import re

def read_single_bibtex(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_bib_entries(bibtex_content):
    pattern = re.compile(r'@inproceedings\{(?:[^{}]|(?R))*\}', re.MULTILINE )
    matches = pattern.findall(bibtex_content)

    if matches:
        for i in matches:
            print(i)
        return matches
    else:
        print("No BibTeX entries found in the content.")
        return None

def format_md(key, title_value, authors_value, venue_value, year_value, doi_value):
    with open(str(key)+'.md', 'w') as file:
        file.write('---\n')
        file.write('layout: default\n')
        file.write('title: "'+title_value+'"\n')
        file.write('authors: '+authors_value+'\n')
        file.write('venue: "'+venue_value+'"\n')
        file.write('year: '+year_value+"\n")
        file.write('doi: '+ doi_value+ '\n')
        file.write('paperurl: files/publications/papers/'+key+'.pdf\n')
        file.write('citation: files/publications/citations/'+key+'.bib\n')
        file.write('---\n')


# Example usage:
if __name__ == "__main__":
    input_string = read_single_bibtex("custom.bib")
    items = input_string.split('@')
    for item in items: 
        _item = item.split(',\n')
        key = [_item[0].split('{')[1] if len(_item[0].split('{'))>1 else None]
        key = key[0]
        with open(str(key)+'.bib','w') as file:
            file.write('@'+item)
        title_value = ''
        authors_value = ''
        year_value = ''
        doi_value = ''
        venue_value = ''
        _item = re.sub(r'[\n\t ]+', ' ', item).split('{',1)
        if (len(_item) > 1):
            _item = _item[1].split('},')           
        else:
            _item = None
        if _item:
            for e in _item:
                if ' title =' in e:
                    title_value = e.split('{',1)[1]
                    title_value = title_value.replace('{','').replace('}','')
                if 'author' in e:
                    authors_value = e.split('{',1)[1]
                    authors_value = authors_value.replace(' and', ',').replace('{','').replace('}','')             
                if 'year' in e:
                    year_value = e.split('{',1)[1].split('}')[0]
                if 'booktitle' in e:
                    venue_value = e.split('{',1)[1].replace('{','').replace('}','')
                if ' url' in e:
                    doi_value = e.split('{',1)[1].split('}')[0]
            format_md(key, title_value, authors_value, venue_value, year_value, doi_value)


