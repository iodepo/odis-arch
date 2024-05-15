import re
import polars as pl

def templateQ(qlist, subject, type):
    template = qlist['q2']  # later select this based on the type variable
    template = template.replace('SUBJECTIRI', subject)
    # print(template)

    return template

def qrSelects(qlist, t):
    template = qlist['q2']  ## TODO update to pull based on type passed

    start_word = 'DISTINCT'
    end_word = 'WHERE'

    start_index = template.find(start_word) + len(start_word)
    end_index = template.find(end_word)

    between_text = template[start_index:end_index].strip()
    matches = re.findall(r'\?\w+', between_text)
    result = [match[1:] for match in matches]

    if 's' in result:
        result.remove('s')

    # The regex finds all cases of ?var so remove duplicates if any
    unique_list = []
    for item in result:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

# Notes:
# df comes in at 1893
def dataset_list(df, store, qlist):

    sl = qrSelects(qlist, "foo") # get vars for query of type "t"
    print(sl)

    dl = []
    for i in range(len(df)):     # this loop will run for len(df)
        row = df.slice(i, 1)
        s = row['id'][0]
        t = row['type'][0]  # fetch column 'type'

        sl = qrSelects(qlist, t) # get vars for query of type "t"
        qr = list(store.query(templateQ(qlist, s, t)))  # query RDF for subject s of type t

        # print("{} : {}".format(s, t))
        # print(qr)

        d = dict()
        for r in qr:
            for term in sl:
                if r[term] is not None:
                    # print("{}  {}".format(term, r[term].value))
                    if r[term].value != '':
                        d[term] = r[term].value

        # print(d)
        if len(d) > 0:
            dl.append(d)

    print("Length of dataset query results: {}".format(len(dl)))

    df = pl.from_records(dl, schema=sl)

    print(len(df))

    # print(df)

