from spreadsheet import Spreadsheet
import config

columns = {
    'date': str,
    'email': str,
    'firstname': str,
    'lastname': str,
    'dni': str,
    'phone': str,
    'year': str,
    'division': str,
    'problem': str,
}
ss = Spreadsheet(config.drive.url, config.drive.pedidos, columns=columns)
sheet = ss.query(converters=columns)
print(sheet[-3:])
