import africastalking

username = " afyayaakili"
api_key="ebd62d4425"
africastalking.initialize(username, api_key)

sms = africastalking.SMS
resp = sms.send("hello,this is afya akili marathon testing", ["+255733829842"])
print(resp) 