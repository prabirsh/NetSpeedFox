import json

config = {
    "from_email": "",
    "from_password": "",
    "to_email": "",
    "speed_threshold": 5
}

config["from_email"] = input("Enter your email: ")
config["from_password"] = input("Enter your email password: ")
config["to_email"] = input("Enter recipient email: ")
config["speed_threshold"] = float(input("Enter speed threshold (Mbps): "))

with open('config.json', 'w') as config_file:
    json.dump(config, config_file)

print("Configuration saved to config.json")
