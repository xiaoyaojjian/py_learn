import configparser

config = configparser.ConfigParser()
config.read('example.ini')

config.set('shiina', 'age', '666')

config.add_section('so what')
config.set('so what', 'uccu', 'sun')

config.remove_option('shiina', 'gender')
config.write(open('updata.ini', 'w'))