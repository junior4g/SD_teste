import redis
conn = redis.Redis('localhost')

user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai", "Location":"RCP"}

conn.hmset("pythonDict", user)

conn.hgetall("pythonDict")

{'Company': 'SCTL', 'Address': 'Mumbai', 'Location': 'RCP', 'Name': 'Pradeep'}


mensagem = "48922"
        
print(mensagem[0])