#Contagem Regressiva
from time import sleep
import emoji

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize(':fogos_de_artifício: BUMM :fogos_de_artifício:' , language='pt'))

