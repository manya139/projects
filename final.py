import random
import string
from datetime import datetime
from datetime import date

qna = {
    "hi" : "hello there! My name is xyz how may i help you?",
    "track" : "I have recorded your id, please wait...",
    "how do i request a return?": "Your id has been recorded, fetching details....",
    "i haven't recieved my refund" : "Please check your email for any updates regarding a pending refund. It usually takes 10 days for a refund.",
    "ssup" : "no lol bye",
    "what is your name ?" : "hello there! My name is Polo how may i help you?",
    "i wanna talk to an expert" : "ok",
    "who created you" : "Some smart AI students created me :D",
    "i want a tracking link":" Tracking link is being generated...",
    "bye" : "thank you for using our program!!",
    "diplay my profile" : "Processing...",
    "what time is it" : "Time : ",
    "whats the date" : "Date : "
}
customer_1 = {'user_id':'1', 'name':'Manya','product_name':'black hoodie','warehousename':'thane','numdays':'3','amount':'799','dayssince':'3','phno':'7977964037', 'mop' : 'cod', 'pastorders' : ['tshirt 20-10-2022 delivered', 'skirt 05-11-2022 exchanged', 'top 30-09-2022 returned']}
customer_2 = {'user_id':'2','name':'aaryansh','product_name':'oversized tshirt','warehousename':'nerul','numdays':'2','amount':'1599','dayssince':'1','phno':'7977964332', 'mop' : 'cod', 'pastorders' : ['jeans 25-10-2022 delivered', 'shirt 05-10-2022 exchanged', 'jacket 30-09-2022 delivered', 'shorts 06-09-2022 returned']}
customer_3 = {'user_id':'3','name':'Lakshya','product_name':'satin crop top','warehousename':'lower parel','numdays':'2','amount':'1990','dayssince':'2','phno':'9820830722', 'mop' : 'debitcard', 'pastorders' : ['top 30-09-2022 delivered', 'nightie 05-11-2022 exchanged']}
customer_4 = {'user_id':'4', 'name':'Nivenka','product_name':'Semi-Sheer top with piping','warehousename':'lower parel','numdays':'3','amount':'1590','dayssince':'3','phno':'9930948222', 'mop' : 'gpay', 'pastorders' : ['skirt 10-10-2022 delivered', 'corset 23-11-2022 returned', 'jeans 04-09-2022 exchanged', 'pants 15-10-2022 returned']}
customer_5 = {'user_id':'5','name':'Reuben','product_name':'Corsetery-Inspired Lace top','warehousename':'lower parel','numdays':'2','amount':'2590','dayssince':'1','phno':'9167753827', 'mop' : 'creditcard', 'pastorders' : ['vest 25-10-2022 returned', 'underwear 11-11-2022 exchanged', 'skirt 20-09-2022 returned']}
customer_6 = {'user_id':'6','name':'Malhar','product_name':'Contrast Printed T-Shirt','warehousename':'Kurla','numdays':'4','amount':'2590','dayssince':'4','phno':'9730046761', 'mop' : 'cod', 'pastorders' : ['shoes 09-10-2022 delivered', 'dress 25-11-2022 exchanged']}
customer_7 = {'user_id':'7','name':'Aryaan','product_name':'Basic tshirt','warehousename':'Bandra','numdays':'6','amount':'990','dayssince':'1','phno':'9833887171', 'mop' : 'debitcard', 'pastorders' : ['crocs 20-09-2022 delivered', 'hoodie 07-11-2022 exchanged', 'tracksuit 30-10-2022 returned']}
customer_8 = {'user_id':'8','name':'Yohaan','product_name':'Faded-Effect Sweatshirt','warehousename':'Bandra','numdays':'2','amount':'2990','dayssince':'2','phno':'96192975487', 'mop' : 'gpay', 'pastorders' : ['shirt 25-10-2022 delivered', 'sweater 30-09-2022 exchanged', 'kurta 30-09-2022 delivered', 'shoes 08-10-2022 returned']}
customer_9 = {'user_id':'9', 'name':'Kavya','product_name':'Seamless top with rhinestones','warehousename':'Kurla','numdays':'4','amount':'1590','dayssince':'3','phno':'8591910307', 'mop' : 'cod', 'pastorders':['off shoulder top 21-10-2022 delivered','UCLA hoodie 30-11-2022 exchanged']}
customer_10 = {'user_id':'10','name':'Meera','product_name':'Full trouser','warehousename':'Thane','numdays':'2','amount':'2890','dayssince':'1','phno':'9167356528', 'mop' : 'creditcard','pastorders':['baseball shirt 3-10-22 delivered', 'denim shorts 7-11-2022 exchanged','jewellery 22-11-2022 exchanged' ]}
customer_11 = {'user_id':'11','name':'Sanjana','product_name':'Basic Crop top','warehousename':'Kurla','numdays':'4','amount':'890','dayssince':'4','phno':'9607694333', 'mop' : 'gpay','pastorders':['shorts 5-10-22 delivered','shorts 6-10-22 returned']}
customer_12 = {'user_id':'12','name':'Dhruv','product_name':'printed tshirt','warehousename':'Bandra','numdays':'6','amount':'1990','dayssince':'1','phno':'8962011000', 'mop' : 'cod', 'pastorders':['hoodie 21-09-22 delivered','printed t-shirt 23-09-11 delivered']}
customer_13 = {'user_id':'13','name':'Chaitanya','product_name':'Henley Neck T shirt','warehousename':'Bandra','numdays':'3','amount':'799','dayssince':'2','phno':'96192 02019', 'mop' : 'creditcard','pastorders':['baseball cap 02-08-2022 delivered','kurta 05-09-2022 exchanged']}
customer_14 = {'user_id':'14', 'name':'Kamya','product_name':'Zari Embroidered Kurta Set','warehousename':'Vasai','numdays':'8','amount':'1690','dayssince':'4','phno':'8591911387', 'mop' : 'gpay','pastorders':['shoes 01-08-2022 delivered','necklace 3-09-2022 delivered', 'golden rings 4-09-2022 exchanged','silver snake earrings 07-09-2022 delivered']}
customer_15 = {'user_id':'15','name':'Nandini','product_name':'Women Bootcut Jeans','warehousename':'Marol','numdays':'2','amount':'2199','dayssince':'1','phno':'9166356558', 'mop' : 'cod','pastorders':['kurta 07-07-2022 delivered']}
customer_16 = {'user_id':'16','name':'Bansari','product_name':'Floral Wrap Dress','warehousename':'Kurla','numdays':'4','amount':'890','dayssince':'2','phno':'9607614313', 'mop' : 'creditcard','pastorders':['shiny crop top 3-04-2022 delivered','heels 23-06-2022 returned','floral skirt 03-07-2022 exchanged','denim skirt 4-11-2022 delivered']}
customer_17 = {'user_id':'17','name':'Sachi','product_name':'High Rise Crop Track Pants','warehousename':'Bandra','numdays':'2','amount':'3320','dayssince':'1','phno':'8962011510', 'mop' : 'cod','pastorders':['slippers 04-06-2022 delivered','basic top 03-07-2022 exchanged']}
customer_18 = {'user_id':'18','name':'Karan','product_name':'Varsity Jacket','warehousename':'Bandra','numdays':'5','amount':'7999','dayssince':'2','phno':'96192 02737', 'mop' : 'gpay','pastorders':['printed shirt 09-09-2022 returned','varsity cap 11-10-2022 delivered']}
customer_19 = {'user_id':'19', 'name':'Mahi','product_name':'Flared pants','warehousename':'Borivali','numdays':'8','amount':'1730','dayssince':'4','phno':'8591911727', 'mop' : 'creditcard','pastorders':['floral crop top 04-10-2022 delivered','white quilted slippers 04-10-2022 delivered']}
customer_20 = {'user_id':'20','name':'Zalak','product_name':'Crop top','warehousename':'Mulund','numdays':'2','amount':'2199','dayssince':'1','phno':'9166356558', 'mop' : 'cod','pastorders':['flared jeans 12-10-2022 exchanged', 'ribbed jeans 18-10-2022 delivered']}

user_id_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']



def function_1(customer_info):
    print("Polo : ", qna["how do i request a return?"])
    return f"Polo : Your order for {customer_info['product_name']} is currently at {customer_info['warehousename']}. It will be delivered in {customer_info['numdays']} days"
def function_2(customer_info):
    return f"Polo : Requesting return for {customer_info['product_name']}.Your shipment will be picked up from you soon !"

def function_3(customer_info):
    print("Polo : ", qna["i haven't recieved my refund"])
    return f"Polo : Your refund for amount {customer_info['amount']} is currently processing, please wait for atleast {customer_info['dayssince']} days."
    
def function_4():
    return "Polo : Connecting you to an executive... \n An expert has been assigned, please expect a call in a few minutes "


def function_5():
    print("Polo : " ,qna['i want a tracking link'])
    randt=str(random.randint(10000,99999))
    return f"www.polobot.com/track/{randt}"

def coupon(customer_info):
    if int(customer_info['amount']) > 1800:
        S = 6  # number of characters in the string.   
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
        return f"Polo : Congrats! Redeem your coupon using this code : " + str(ran) # print the random data  
    elif int(customer_info['amount']) <= 1800:
        amtneeded = 1800 - int(customer_info['amount'])
        return f'Polo : No coupon :( shop for atleast {amtneeded} more to redeem a coupon'

def profiledisplay(customer_info):
    return "Polo : Your current profile: \n Name : " + customer_info['name'] + " \n User Id :  " + customer_info['user_id'] + "\n Phone number :  " + customer_info['phno']

def oldorders(customer_info):
    print ("Polo : Past orders are  ")
    for i in customer_info['pastorders']:
        print("       " + i)

def profileedit(customer_info):
    print("Polo : Do you want to edit phone number, name or both? ")
    ch = input("You : ")
    if 'phone' in ch:
        print("Polo : Please enter new number : ")
        newnum = str(input("You : "))
        customer_info['phno'] = newnum
        print("Polo : updation complete!!")
    elif 'name' in ch:
        print("Polo : Please enter new name : ")
        newname = str(input("You : "))
        customer_info['name'] = newname
        print("Polo : updation complete!!")
    elif 'both' in ch:
        print("Polo : Please enter new number : ")
        newnum = str(input("You : "))
        customer_info['phno'] = newnum
        print("Polo : Please enter new name : ")
        newname = str(input("You : "))
        customer_info['name'] = newname
        print("Polo : updation complete!!")
def modeofpayement(customer_info):
    print("Polo : Do you want to change your mode of payment to - cod, gpay, creditcard or debitcard?")
    newmod = str(input("You : "))
    if customer_info['mop'] in newmod:
        print("Polo : Entered payment mode is same as current ")
    else: 
        if 'cod' in newmod:
            print("Polo : mode of payment updated to cod! Please keep exact amount at the time of delivery :) Any amount paid via online payment will be credited to your account in a few days")
        elif 'gpay' in newmod:
            randr=str(random.randint(10000,99999))
            print("Polo : mode of payment updated to gpay! Follow this link for payment gateway : www.polobot.com/paymentgateway/" + randr)
        elif 'creditcard' in newmod:
            randr=str(random.randint(10000,99999))
            print("Polo : mode of payment updated to creditcard! Follow this link for payment gateway : www.polobot.com/paymentgateway/" + randr)
            
        elif 'debitcard' in newmod:
            randr=str(random.randint(10000,99999))
            print("Polo : mode of payment updated to debitcard! Follow this link for payment gateway : www.polobot.com/paymentgateway/" + randr)
def cancelorder(customer_info):
    print(f"order of {customer_info['product_name']} has been cancelled.")



now = datetime.now()
current_time = now.strftime("%H:%M:%S")

today = date.today()
d2 = today.strftime("%B %d, %Y")
database = [customer_1,customer_2,customer_3,customer_4,customer_5,customer_6,customer_7,customer_8, customer_9,customer_10,customer_11,customer_12,customer_13,customer_14,customer_15,customer_16,customer_17,customer_18,customer_19,customer_20]



while True: 
    
    qs = 'input("YOU: ").strip()'
    if 'bye' in qs:
        #print("Polo : Thank you for using polo !! Hope i could help you, Have a nice day :D")
        break
    else:
        user_id = str(input("Polo : Hi My name is polo, enter your id to continue \nYou : "))
        if user_id in user_id_list:

        

            while 'bye' not in qs:
            
                for data in database:
                    if user_id in data['user_id']:
                        customer = data
                        randv = random.randint(1,3)
                        if randv == 1:
                            print("Polo : What may i help you with " + customer['name'] + "?") 
                        elif randv == 2:
                            print("Polo : What do you need " + customer['name'] + "?")
                        elif randv == 3:
                            print("Polo : How can i assist you today " + customer['name'] + "?")
                        qs = input("YOU: ").strip()
                        break
                        
                
    
    
        
                for data in database:
                    if user_id in data['user_id']:
                        customer = data
        
                        if 'return' in qs:
                            print(function_2(customer))
                        elif 'link' in qs:
                            print(function_5())
                        elif 'new ' in qs:
                            print("Polo : your order has been cancelled")
                        elif 'track' in qs:
                            print(function_1(customer))
                        elif 'refund' in qs:
                            print(function_3(customer))
                        elif 'expert' in qs:
                            print(function_4())
                        elif 'coupon' in qs:
                            print(coupon(customer))
                        elif 'created' in qs:
                            print("Polo : " ,qna['who created you'])
                        elif 'edit' in qs:
                            profileedit(customer)
                        elif 'profile' in qs:
                            print(profiledisplay(customer))
                        elif 'time' in qs:
                            print("Polo : It's "+ current_time + " right now")
                        elif 'date' in qs:
                            print("Polo : Today is " + d2 )
                        elif 'payment' in qs:
                            modeofpayement(customer)
                        elif 'past' in qs:
                            oldorders(customer)
                        elif 'cancel' in qs:
                            cancelorder(customer)
                        elif 'bye' in qs:
                            print("Polo : Rate experience with polo out of 5 please :)")
                            ratingofuser = int(input("YOU : "))
                            print("Polo : Thank you for using polo !! Hope i could help you, Have a nice day :D")
                            exit(1)
                            
                        else:
                            print("Polo: I didn't quite get that, could you repeat?")
                        break
                        
                
        else:
            print("Polo : please enter valid id")
        
   


        




        
    

   