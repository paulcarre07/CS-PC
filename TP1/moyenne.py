import sys

sum = 0
resultat = 0
erreur = "Note non valide"

for val in sys.argv[1:]:
    try:
        val = eval(val)
    except:
        print(erreur)
        sys.exit(0)
    if type(val) == float or type(val) == int:
        if val<0 or val> 20:
            sum += val
            resultat = sum/len(sys.argv[1:])
        else: 
            print(erreur)
            sys.exit(0)
    else:
        print(erreur)
        sys.exit(0)

print(resultat)