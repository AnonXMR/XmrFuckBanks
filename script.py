import requests 


print("                                                                                                     ")
print("                                                                                                     ")
print("                        ____      ___       ___       ___      ________                              ")
print("                        `MM(      )M'       `MMb     dMM'      `MMMMMMMb.                            ")
print("                         `MM.     d'         MMM.   ,PMM        MM    `Mb                            ")
print("                          `MM.   d'          M`Mb   d'MM        MM     MM                            ")
print("                           `MM. d'           M YM. ,P MM        MM     MM                            ")
print("                            `MMd             M `Mb d' MM        MM    .M9                            ")
print("                             dMM.            M  YM.P  MM        MMMMMMM9'                            ")
print("                            d'`MM.           M  `Mb'  MM        MM  \M\                              ")
print("                           d'  `MM.          M   YP   MM        MM   \M\                             ")
print("                          d'    `MM.         M   `'   MM        MM    \M\                            ")
print("                        _M(_    _)MM_       _M_      _MM_      _MM_    \M\_                          ")
print("                                                                                                     ")
print("                                                                                                     ")
print("                                                                                                     ")
print("                                                                                                     ")
print("                                                                                                     ")
print("________ ____     ___   ____   ___    __        ________        _     ___      ______    __   ____   ")
print("`MMMMMMM `MM'     `M'  6MMMMb/ `MM    d'        `MMMMMMMb.     dM.    `MM\     `M'`MM    d'  @6MMMMb\ ")
print(" MM    \  MM       M  8P    YM  MM   d'          MM    `Mb    ,MMb     MMM\     M  MM   d'  6M'    ` ")
print(" MM       MM       M 6M      Y  MM  d'           MM     MM    d'YM.    M\MM\    M  MM  d'   MM       ")
print(" MM   ,   MM       M MM         MM d'            MM    .M9   ,P `Mb    M \MM\   M  MM d'    YM.      ")
print(" MMMMMM   MM       M MM         MMd'             MMMMMMM(    d'  YM.   M  \MM\  M  MMd'      YMMMMb  ")
print(" MM   `   MM       M MM         MMYM.            MM    `Mb  ,P   `Mb   M   \MM\ M  MMYM.         `Mb ")
print(" MM       MM       M MM         MM YM.           MM     MM  d'    YM.  M    \MM\M  MM YM.         MM ")
print(" MM       YM       M YM      6  MM  YM.          MM     MM ,MMMMMMMMb  M     \MMM  MM  YM.        MM ")
print(" MM        8b     d8  8b    d9  MM   YM.         MM    .M9 d'      YM. M      \MM  MM   YM. L    ,M9 ")
print("_MM_        YMMMMM9    YMMMM9  _MM_   YM._      _MMMMMMM9_dM_     _dMM_M_      \M _MM_   YM.MYMMMM9  ")
print("                                                                                                     ")
print("                                                                                                     ")
print("                                                                                                     ")


print("\n")
print("\n")

# URL de l'API pour obtenir les données sur XMR
url = 'https://api.minerstat.com/v2/coins?list=XMR'

GetDataXMR = requests.get(url)
liste_datas_xmr = GetDataXMR.json() #data = toutes les clés format json

price_xmr_usd = liste_datas_xmr[0]['price'] #$
network_hashrate = liste_datas_xmr[0]['network_hashrate'] #H/S
reward_per_block_in_xmr = liste_datas_xmr[0]['reward_block'] #XMR/block


CostElecCentime = int(input(">>>>Enter your kWh cost in cents here: "))
print("")
HashRate = int(input(">>>>Enter your hashrate (H/s) : "))
print("")
ConsoWatt = int(input(">>>>Enter your total electrical consumption (in Watts) : "))
print("")
20
HoursByDay = 24
DayByMonth = 30
MonthByYear = 12
CostElecEuros = CostElecCentime/100
Conso_kWh = ConsoWatt/1000

CoutTotalDaily = CostElecEuros * Conso_kWh * HoursByDay 
CoutTotalMonth = CoutTotalDaily * DayByMonth
CoutTotalYear = CoutTotalMonth * MonthByYear

print("========================= For your information : =========================")
print("\n")
print("Total hashrate :", int(network_hashrate), "H/s.")
print("Price :", int(price_xmr_usd), "USD.")
print("Daily electricity cost : ", CoutTotalDaily, "USD.")
print("Mnthly electricity cost : ", CoutTotalMonth, "USD.")
print("Yearly electricity cost : ", CoutTotalYear, "USD.")
print("\n")
print("__________________________________________________________________________")

MyHashrateRate = HashRate/network_hashrate     #ma part de puissance de calcul par rapport au réseau
RewardYearly = MyHashrateRate * reward_per_block_in_xmr * 720 * 365 #reward annuel en xmr
RewardMonthly = RewardYearly / 12                                   #reward mensuelle en xmr
RewardDaily = RewardMonthly / 30                                    #reward jour en xmr
print("\n")
print("Daily XMR reward : ", RewardDaily, "XMR")
print("Monthly XMR reward : ", RewardMonthly, "XMR")
print("Yearly XMR reward : ", RewardYearly, "XMR")
print("...calculations based on a theoretical number of 720 blocks per day*")
print("\n")
print("__________________________________________________________________________")
ProfitY = float(RewardYearly * price_xmr_usd -CoutTotalYear)
ProfitM = float(RewardMonthly * price_xmr_usd - CoutTotalMonth)
ProfitD = float(RewardDaily * price_xmr_usd - CoutTotalDaily)
print("")
print("Here are your theoreticals :")
print("               - daily profits : ", ProfitD, "USD.")
print("               - monthly profits : ", ProfitM, "USD.")
print("               - yearly profits : ", ProfitY, "USD.")
print("\n")


if ProfitY >= 0:
    print("Worth it :D !")
    print("")
else: 
    print("Every hashrate fuck a bank, so keep it mining :D")
    print("But u ackhually lose money bro")
    print("")

exit()