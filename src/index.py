from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen: ")
    mehuvarasto(mehua)
    olutvarasto(olutta)

    olut_getter(olutta)
    mehu_setterit(mehua)
    virhe1()
    lisays_virhe(mehua, olutta)
    olutvarasto(olutta)
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    olutvarasto(olutta)

    mehuvarasto(mehua)
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    mehuvarasto(mehua)


def mehuvarasto(mehua):
    print(f"Mehuvarasto: {mehua}")

def olutvarasto(olutta):
    print(f"Olutvarasto: {olutta}")

def olut_getter(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    mehuvarasto(mehua)
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    mehuvarasto(mehua)

def virhe1():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def lisays_virhe(mehua, olutta):
    olutvarasto(olutta)
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    olutvarasto(olutta)

    mehuvarasto(mehua)
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    mehuvarasto(mehua)



if __name__ == "__main__":
    main()
