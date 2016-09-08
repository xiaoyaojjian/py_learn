import configparser

config = configparser.ConfigParser()
config.read('example.ini')

print(config.defaults())
print(config.sections())
print(config['shiina']['name'])
print('shiina' in config)