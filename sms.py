# import package
import africastalking


# Initialize SDK
username = "afyayaakili"    #   use 'sandbox' for development in the test environment
api_key = "d35d634657367f9950b769ddef6aff4f0b28617ff5ba732235360b3852410b58"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+255733829842"])
print(response)

# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+255733829842"], callback=on_finish)    
