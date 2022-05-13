from flask import Flask, render_template, request
import calendar

from datetime import datetime

from templates import control

calendar.setfirstweekday(firstweekday=6)

app = Flask(__name__)

cont=0
semana = ['Dom', 'Lun', 'Mar', 'Mie', 'Jue', 'Vie', 'Sab']
mesA = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def calc_calendario(date):
    año = date.year
    añoInfo = dict()

    for mes in range(1, 13):
        dias = calendar.monthcalendar(año, mes)
        if len(dias) !=6:
            dias.append([0 for _ in range(7)])
        mes_addr = calendar.month_abbr[mes]
        añoInfo[mes_addr] = dias
    return añoInfo

@app.route('/', methods=["GET"])
def index():
    fecha = datetime.today()
    this_mes= calendar.month_abbr[fecha.month]
    cdr= control.obtenerEv()
    return render_template('index.html', fecha=fecha, this_mes=this_mes, content=calc_calendario(fecha), mesA=mesA, cdr=cdr)

@app.route('/lista/<mes>/<dia>/<year>', methods=["POST"])
def lista(mes, dia, year):
    fecha=datetime.today()
    dia = int(dia)
    this_mes = calendar.month_abbr[fecha.month]
    this_dia = str(fecha.day)
    return render_template('lista.html', mes=mes, dia=dia, year=year, fecha=fecha, this_mes=this_mes, mesA=mesA, this_dia=this_dia)

@app.route('/hola/<dia>/<mes>/<year>/', methods=["POST"])
def lista2(dia, mes, year):
    even = request.form["Evento"]
    mes = mes
    dia = dia
    year = year
    fecha = datetime.today()
    control.guardar(even, dia, mes, year)
    ctr = control.obtenerEv()
    return  render_template('visual.html', ctr=ctr, fecha=fecha, mesA=mesA)

@app.route('/ver/', methods=["POST"])
def ver():
    ctr = control.obtenerEv()
    fecha = datetime.today()
    return render_template('visual.html', ctr=ctr, fecha=fecha, mesA=mesA)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
