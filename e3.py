#!/usr/bin/env python

import pandas as pd
lines = []
for line in open("election_id.txt", "r"):
    lines.append(line.split()[0])

lines.reverse()

dictionary = {}
counties = ["Accomack County","Albemarle County","Alexandria City","Alleghany County"]

for v in counties:
    dictionary[v] = {"year" : [], "vote_share" : []}

for i in lines:

    file_name = "year" + i + ".csv"
    header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file_name, index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["year"] = int(i)
    df["vote_share"] = df["Republican"] /df["Total Votes Cast"]

    for v in counties:
        if v in df.index:
            dictionary[v]["year"].append(int(i))
            dictionary[v]["vote_share"].append(df.loc[v]["vote_share"])

for v in counties:
    df = pd.DataFrame(dictionary[v])
    graph = df.plot(x="year", y="vote_share")
    graph.figure.savefig(v.lower().replace(" ", "_") + ".pdf")
