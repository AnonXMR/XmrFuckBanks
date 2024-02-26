import requests 

CREATOR_SIGN = """ 

                        ____      ___       ___       ___      ________                              
                        `MM(      )M'       `MMb     dMM'      `MMMMMMMb.                            
                         `MM.     d'         MMM.   ,PMM        MM    `Mb                            
                          `MM.   d'          M`Mb   d'MM        MM     MM                            
                           `MM. d'           M YM. ,P MM        MM     MM                            
                            `MMd             M `Mb d' MM        MM    .M9                            
                             dMM.            M  YM.P  MM        MMMMMMM9'                            
                            d'`MM.           M  `Mb'  MM        MM  \M\                              
                           d'  `MM.          M   YP   MM        MM   \M\                             
                          d'    `MM.         M   `'   MM        MM    \M\                            
                        _M(_    _)MM_       _M_      _MM_      _MM_    \M\_                          
                                                                                                     
                                                                                                     
                                                                                                     
                                                                                                     
                                                                                                     
________ ____     ___   ____   ___    __        ________        _     ___      ______    __   ____   
`MMMMMMM `MM'     `M'  6MMMMb/ `MM    d'        `MMMMMMMb.     dM.    `MM\     `M'`MM    d'  @6MMMMb\ 
 MM       MM       M  8P    YM  MM   d'          MM    `Mb    ,MMb     MMM\     M  MM   d'  6M'      
 MM       MM       M 6M      Y  MM  d'           MM     MM    d'YM.    M\MM\    M  MM  d'   MM       
 MMMMMM   MM       M MM         MMd'             MMMMMMM(    d'  YM.   M  \MM\  M  MMd'      YMMMMb  
 MM       MM       M MM         MMYM.            MM    `Mb  ,P   `Mb   M   \MM\ M  MMYM.         `Mb 
 MM       MM       M MM         MM YM.           MM     MM  d'    YM.  M    \MM\M  MM YM.         MM 
 MM       YM       M YM      6  MM  YM.          MM     MM ,MMMMMMMMb  M     \MMM  MM  YM.        MM 
 MM        8b     d8  8b    d9  MM   YM.         MM    .M9 d'      YM. M      \MM  MM   YM.      ,M9 
_MM_        YMMMMM9    YMMMM9  _MM_   YM._      _MMMMMMM9_dM_     _dMM_M_      \M _MM_   YM.MYMMMM9  

"""
                                                                                                     
print(CREATOR_SIGN)                                                                                                  


print("""\n\n""")


# URL de l'API pour obtenir les données sur XMR
url = 'https://api.minerstat.com/v2/coins?list=XMR'

GetDataXMR = requests.get(url)
liste_datas_xmr = GetDataXMR.json() #data = toutes les clés format json

price_xmr_usd = liste_datas_xmr[0]['price'] #$
network_hashrate = liste_datas_xmr[0]['network_hashrate'] #H/S
reward_per_block_in_xmr = liste_datas_xmr[0]['reward_block'] #XMR/block


CostElecCentime = int(input(">>>>Enter your kWh cost in cents here: "))
HashRate = int(input(">>>>Enter your hashrate (H/s) : "))
ConsoWatt = int(input(">>>>Enter your total electrical consumption (in Watts) : "))

print("""\n \n""")

CostElecEuros = CostElecCentime/100
Conso_kWh = ConsoWatt/1000

CoutTotalDaily = CostElecEuros * Conso_kWh * 24 
CoutTotalMonth = CoutTotalDaily * 30
CoutTotalYear = CoutTotalMonth * 12

print("========================= For your information : =========================")
print()
print("Total hashrate :", int(network_hashrate), "H/s.")
print("Price :", int(price_xmr_usd), "USD.")
print("Daily electricity cost : ", CoutTotalDaily, "USD.")
print("Mnthly electricity cost : ", CoutTotalMonth, "USD.")
print("Yearly electricity cost : ", CoutTotalYear, "USD.")
print()
print("__________________________________________________________________________")

MyHashrateRate = HashRate/network_hashrate     #ma part de puissance de calcul par rapport au réseau
RewardYearly = MyHashrateRate * reward_per_block_in_xmr * 720 * 365 #reward annuel en xmr
RewardMonthly = RewardYearly / 12                                   #reward mensuelle en xmr
RewardDaily = RewardMonthly / 30                                    #reward jour en xmr
print()
print("Daily XMR reward : ", RewardDaily, "XMR")
print("Monthly XMR reward : ", RewardMonthly, "XMR")
print("Yearly XMR reward : ", RewardYearly, "XMR")
print("...calculations based on a theoretical number of 720 blocks per day*")
print()
print("__________________________________________________________________________")
ProfitY = float(RewardYearly * price_xmr_usd -CoutTotalYear)
ProfitM = float(RewardMonthly * price_xmr_usd - CoutTotalMonth)
ProfitD = float(RewardDaily * price_xmr_usd - CoutTotalDaily)
print()
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