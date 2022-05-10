import sys 
somme=0
for notes in sys.argv[1:]:
    try:
        arg=eval(notes)
    except:
        print("non valide")
        sys.exit(0)

    if arg<0 or arg>20:
        print("non valide")
        sys.exit(0)

    somme+=arg

moy=somme/len(sys.argv[1:])

print(moy)


