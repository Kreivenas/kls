# from PIL import Image, ImageEnhance, ImageFilter, ImageStat
# from PIL import Image, ImageEnhance
# gele = Image.open('puokste.jpg')
#
# # Konvertuoti į pilkąjį vaizdą
# gele = gele.convert('L')
#
# # Apskaičiuoti vidutinę reikšmę///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# bw = int(ImageStat.Stat(gele).mean[0] + 0.5)
# print("Paveikslėlio vidutinė reikšmė:", bw)
#
# # Taikyti burbuliuko filtrą
# gele = gele.filter(ImageFilter.BLUR)
#
# # Pakeisti kontrastą
# gele = ImageEnhance.Contrast(gele).enhance(2.0)
#
# # Parodyti paveikslėlį su visais efektais
# gele.show()
#

# def keisti_paveikslelio_savybes(paveikslas, kontrastas, spalvingumas,
#                                 asumumas, ryskumas, issaugoti=False):
#     # Atidaryti paveikslėlį naudojant PIL
#     paveikslelis = Image.open(paveikslas)
#
#     # Keisti kontrastą
#     kontrasto_keitiklis = ImageEnhance.Contrast(paveikslelis)
#     paveikslelis = kontrasto_keitiklis.enhance(kontrastas)
#
#     # Keisti spalvingumą
#     spalvingumo_keitiklis = ImageEnhance.Color(paveikslelis)
#     paveikslelis = spalvingumo_keitiklis.enhance(spalvingumas)
#
#     # Keisti aštrumą
#     asumumo_keitiklis = ImageEnhance.Sharpness(paveikslelis)
#     paveikslelis = asumumo_keitiklis.enhance(asumumas)
#
#     # Keisti ryškumą
#     ryskumo_keitiklis = ImageEnhance.Brightness(paveikslelis)
#     paveikslelis = ryskumo_keitiklis.enhance(ryskumas)
#
#     # Išsaugoti paveikslėlį arba grąžinti pakeistą paveikslėlį
#     if issaugoti:
#         paveikslelis.save("pakeistas.jpg")
#     else:
#         return paveikslelis
#
# keisti_paveikslelio_savybes("puokste.jpg", 1.5, 0.8,
#                            2.0, 1.2, issaugoti=True)

# logo = Image.open("logo.png")
# logo1 = (0, 28, 128, 128)
# alogo = logo.crop(logo1)
# alogo.show()
# alogo.save("alogo.png")

