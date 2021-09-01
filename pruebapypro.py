from pyswip import prolog
prolog= prolog()

prolog.consult('hechos.pl')

X = input('que le gusta a...')

for valor in prolog.query('legusta('+X+',Y)'):
    print(X, 'le gusta ',valor['Y'])
