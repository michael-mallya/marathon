import africastalking

username = " afyayaakili"
api_key="d35d634657367f9950b769ddef6aff4f0b28617ff5ba732235360b3852410b58"
africastalking.initialize(username, api_key)

sms = africastalking.SMS
resp = sms.send("hello,this is afya akili marathon testing", ["+255733829842"],"Inform")
print(resp) 