from random import choice, randint
import json

zar = 0
skip = False

with open("responses.json", "r", encoding="utf-8") as j:
    RESPONSES = json.load(j)

def get_response(user_input, bos_yapma_orani):
    global RESPONSES, zar, eski_zar, skip, bos_yap

    bos_yap = randint(1, int(100/bos_yapma_orani)) # can be improved with math module
    eski_zar = zar if not skip else eski_zar
    zar = randint(1, 6)
    skip = False

    lowered = user_input.lower()                    
    if "zar" in lowered and "at" in lowered:           
        if "atma" in lowered and not "atmaz" in lowered and not "atmas" in lowered:
            skip = True
            return choice(RESPONSES["atma"])
        
        elif bos_yap == 1:
            skip = True
            return choice(RESPONSES["bos_laflar"])
        
        elif zar == eski_zar:
            return choice(RESPONSES["yinelenenler"]).format(zar=zar)
        
        else:
            return choice(RESPONSES["ekstra"]).format(zar=zar)
    elif "sa" in lowered and "bot" in lowered or "selam" in lowered and "bot" in lowered: return "as"