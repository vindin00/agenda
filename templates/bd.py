import pymysql

def ob_con():
    return pymysql.connect(host='VinDin.mysql.pythonanywhere-services.com', port=3306, user='VinDin',
                           password='rootroot', db='VinDin$eventos')

