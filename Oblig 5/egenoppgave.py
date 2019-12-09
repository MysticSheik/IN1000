#                                                |
#                                              /---\
#                                              : = :
#                                              :   :
#                            :,','. '.         :   :---\
#               ..,,,',.',',;,'.';'.'.'.,.'.'..:.  :   :
# 
#             Cow town after a visit by the cow-struction worker.

def tommer_til_cm(antall_tommer):
    return antall_tommer * 2.54

def les_fil(filnavn):
    fil = open(filnavn)
    ordbok = {}
    for avakado in fil:
        ting = avakado.split()
        assert len(ting) == 2
        ordbok[ting[0]] = tommer_til_cm(float(ting[1]))
    fil.close()
    return ordbok

for key, value in les_fil("egenoppgave.txt").items():
    print(key, value, "cm")
