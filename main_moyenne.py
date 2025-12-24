n=int(input("donner le nombre de matieres :"))
d={}
def remplir(d,n):
    for i in range(n):
        ch=input("matiere:")
        notes=()
        tp=float(input("note tp ou oral "))
        ds=float(input("note du ds :"))
        ex=float(input("note de l'examen :"))
        print()
        notes=(tp,ds,ex)
        d.update({ch : notes})
    print (d)
    return d

print()


d1={}
def calcul_moyenne_matiere(d): 
    ptp=float(input("donner le pourcentage de tp ou oral :"))
    pds=float(input("donner le pourcentage de ds: "))
    pex=float(input("donner le pourcentage de l'examen :"))
    while not ptp+pds+pex==100:
        ptp=float(input("donner le pourcentage de tp ou oral :"))
        pds=float(input("donner le pourcentage de ds: "))
        pex=float(input("donner le pourcentage de l'examen :"))
    for i in d.keys() :
        mm=d[i][0]*ptp+d[i][1]*pds+d[i][2]*pex
        mmm=mm/100
        d1.update({i:mmm})
    print()
    print(d1)
    return d1

print()

def calcul_moyenne_generale(d1,n):
    s=0
    sc=0
    for i in d1.items():
        c=float(input("donner le coefficient de "+i[0]))
        s+=i[1]*c
        sc+=c
    m=s/sc
    print("votre moyenne est :"+str(m))
    return(m)   
    
remplir(d,n)
mm=calcul_moyenne_matiere(d)
m=calcul_moyenne_generale(d1,n)

