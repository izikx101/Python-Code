def repToDecimal(str, base):
    result = 0
    dict={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    for b in str:
        a = dict[b]
        result = base * result + a
    return result
    
print(repToDecimal('10', 10))
print(repToDecimal('10', 8))
print(repToDecimal('10', 2))
print(repToDecimal('10', 16))
