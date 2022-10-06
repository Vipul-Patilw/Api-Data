import requests
r = requests.get('http://aamras.com/dummy/EmployeeDetails.json')
json_data = r.json()
