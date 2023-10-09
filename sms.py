# import package
import africastalking


# Initialize SDK
username = "afyayaakili"    #   use 'sandbox' for development in the test environment
api_key = "21615bdc6aebdbeaeea2610e134f2bc34dd94aca4081300cf6556e52df4a47be"      # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello,We're thrilled to inform you that your registration for the Run 4 Schizophrenia event has been successfully received! 🎉 You're now officially part of the Afya ya Akili Marathon on December 10th, 2023, where we'll run for a great cause.", 
                    ["+255766927069"])
print(response)
'''
# Or use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+255733829842"], callback=on_finish)    
'''