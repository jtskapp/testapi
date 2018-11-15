import urllib.request, json
from urllib.error import URLError, HTTPError

max_user = 10
url = 'https://randomuser.me/api/'

def loaddata():
    json_data = []

    #Test Api Connection
    connected = False
    try:
        response = urllib.request.urlopen(url)
        connected = True
    except HTTPError as e:
        # do something
        print('Error code: ', e.code)
        return
    except URLError as e:
        # do something
        print('Reason: ', e.reason)
        return

    if connected:
        for i in range(max_user):
            with urllib.request.urlopen(url) as api:
                data = json.loads(api.read().decode())
            for d in data['results']:
                firstname = (d['name']['first']).encode('utf-8')
                lastname = (d['name']['last']).encode('utf-8')
                displayname = firstname.decode('utf-8') + ", " + lastname.decode('utf-8')
                json_data.append(
                    {
                        'gender':d['gender'],
                        'title':d['name']['title'],
                        'first_name':firstname,
                        'last_name':lastname,
                        'display_name':displayname,
                        'email_address':(d['email']).encode('utf-8'),
                        'street':(d['location']['street']).encode('utf-8'),
                        'city':(d['location']['city']).encode('utf-8'),
                        'state':(d['location']['state']).encode('utf-8'),
                        'postal_code':d['location']['postcode'],
                        'age':d['dob']['age'],
                        'phone':(d['phone']).encode('utf-8'),
                        'cell':(d['cell']).encode('utf-8'),
                    }
                )
    
    #return data
    return json_data

#Loadl Data from API
#loaddata()


# for d in json_data:
#     print(d['gender'])
#     print(d['title'])
#     print(d['first_name'].decode('utf-8'))
#     print(d['last_name'].decode('utf-8'))
#     # print(d['display_name'])