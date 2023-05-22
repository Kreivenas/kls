from sakinys import Sakinys


mano_sakinys = Sakinys("Mano tekstas yra toks")

print(mano_sakinys.atbulai())
print(mano_sakinys.mazosiomis())
print(mano_sakinys.didziosiomis())
print(mano_sakinys.zodis(2))
print(mano_sakinys.skaicius_zodziuose("tekstas"))
print(mano_sakinys.pakeisti_zodi("toks", "kitas"))
mano_sakinys.spausdinti_statistika()

skainys2 = Sakinys("Sianakt miegosiu labai kietai, Nes man jau rauna galva. vienas 1, 2, 3,")

print(skainys2.atbulai())
print(skainys2.mazosiomis())
print(skainys2.didziosiomis())
print(skainys2.zodis(2))
print(skainys2.skaicius_zodziuose("tekstas"))
print(skainys2.pakeisti_zodi("toks", "kitas"))
skainys2.spausdinti_statistika()