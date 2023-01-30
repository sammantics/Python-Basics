#Programa para crear strings intercaladas.

import random

words=['papa','roto']

for i in range(100):
    print ''.join(random.samples(words, random.eandint(,1,5)))