from random import choice, randint

zar = 0
skip = False

def get_response(user_input, bos_yapma_orani):
    global zar, eski_zar, skip, bos_yap

    bos_yap = randint(1, int(100/bos_yapma_orani)) # can be improved with math module
    eski_zar = zar if not skip else eski_zar
    zar = randint(1, 6)
    skip = False

    # CSV pretty soon...
    ekstra = [
    f"{zar} geldi",
    f"hayırlı olsun {zar} geldi",
    f"{zar} geldi gele gele",
    f"attım... {zar} geldi",
    f"{zar} gelir anca",
    f"hooop {zar} geldi",
    f"şanslısın {zar} geldi",               
    f"ne diyim {zar} geldi",
    f"{zar} gelmediyse serefsizim",
    f"bahtsızsın {zar} geldi",
    ]

    yinelenenler = [
    f"{zar} geldi yine",
    f"yine {zar} geldi",
    f"yine gele gele {zar} geldi",
    f"NASIL OLUR YINEMI {zar}!!!",
    f"bunu nasıl yaptın yine {zar} geldi",
    f"o kadar olasılık arasından yine {zar} geldi",
    ]

    atma = [
    "yorulmustum zaten",
    "tm kardes sen at yerime",
    "atasım yoktu zaten",
    "atmazdım zaten",
    "küstüm:(",
    "üzdün beni",
    "ayıp ettin",
    "böyle olmaz atmak istiyordum",
    ]

    bos_laflar = [
    "banane atmicam",
    "bilmem atsammı?",
    "yok sen at",
    "canım istemiyor",
    "hiç atasım yok",
    "atmazsam ne olur?",
    "neden bu kadar ciddisin?",
    "atmak mı? yok canım",
    "sen at ben izlicem",
    "cok isterdim ama atamam",
    "baya yorgunum biliyor musun?",
    "yok ya atmam",
    "7 geldi:)", # slkfjdsfsdfs
    ]

    lowered = user_input.lower()                    
#                                                 We don't care about TDK's rules here
    if "zar" in lowered and "at" in lowered: #                     ↓                      
        if "atma" in lowered and not "atmaz" in lowered and not "atmas" in lowered:
            skip = True
            return choice(atma)
        
        elif bos_yap == 1:
            skip = True
            return choice(bos_laflar) # neden bu kadar ciddisin:)
        
        elif zar == eski_zar:
            return choice(yinelenenler)
        
        else:
            return choice(ekstra)
    elif "sa" in lowered and "bot" in lowered or "selam" in lowered and "bot" in lowered: return "as"