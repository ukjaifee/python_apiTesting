import json

with open('C:\\Users\\Umesh_Kumar\\Documents\\Json\\al.json') as f:
    resp = json.load(f)
    #print(resp['routingInfo']['sourceNode']['location']['countryCode'])
    print(resp['order']['orderId'])
    respJson=resp['order']['orderId']
    #assert respJson=='US'