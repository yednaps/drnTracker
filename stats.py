#!/usr/bin/python

import cPickle as pickle

dl = pickle.load(open('/home/sp/python/drn/drnDict.p','rb'))

status = sorted(set([k for m in dl.keys() for j,k in dl[m]]))
maxwidth = max([len(x) for x in status])

for i in dl:
    dates = [j.date() for j,k in dl[i]]
    print('\n{}: {} records from {} to {}'.format(i.upper(),len(dates),min(dates),max(dates)))
    st = [k for j,k in dl[i]]
    for s in status:
        print('{:{}} {:3} ({:5.2f}%)'.format(s,maxwidth,st.count(s),float(st.count(s))/len(st)*100).rjust(7))

