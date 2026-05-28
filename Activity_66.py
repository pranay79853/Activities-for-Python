country_code = {'India' : '0091',
'Australia' : '0025',
'Nepal' : '00977'}
print(country_code)
print("Country code for India -")
print(country_code.get('India'))
print("Country code for Australia -")
print(country_code.get('Australia'))
print("Country code for Nepal -")
print(country_code.get('Nepal'))
print(country_code.get('Japan', 'Not Found'))