import requests

url = 'http://127.0.0.1:8000/api/accounts/loans/'

account_numbers = ["6010105070", "5000145080", "4006010097", "1003010405", "1112070906", "1002000989"]

authToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMDM2NjUwLCJpYXQiOjE2ODA5NTAyNTAsImp0aSI6IjI0ZWI4OGRmNmNhMzQ1OGM5OGQ3YThmOTZmNjc1YWM4IiwidXNlcl9pZCI6MX0.iVrgi8kE9xENzBx3R3aA0G4telmNJ7hJU1XsRYBG5NI"
headers = {
    'Authorization': "Bearer " + authToken,
    'Content-Type': 'application/json'
}

for account in account_numbers:
    payload = {'account': account}
    response = requests.post(url, json=payload, headers=headers)

    with open("simulation-results.txt", "a") as simulationFile:
        simulationFile.write(response.text)
        simulationFile.write("\n")

print("Script Done ...")