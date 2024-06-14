from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import datetime

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

app = Flask(__name__)
app.config.from_object(config['development'])

db = MySQL(app)
login_manager_app = LoginManager(app)


@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña Incorrecta...")
                return render_template('auth/login.html')
        else:
            flash("Usuario Incorrecto...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('iso/index.html')

@app.route('/home/MapadeProcesos')
@login_required
def MapadeProcesos():
    return render_template('iso/MapaDeProcesos/index.html')

# ROLES Y PERMISOS

def check_permission(username, route):
    if username == "admin" or "jdirectiva" or "ggeneral" or "auditoria" or "iso":
        return True
    elif username == "prueba":
        return route in ["/home/MapadeProcesos/rrhh",
                         "/home/MapadeProcesos/infraestructura_y_equipo",
                         "/home/MapadeProcesos/operaciones",
                         "/home/MapadeProcesos/compras",
                         "/home/MapadeProcesos/bmp",
                         "/home/MapadeProcesos/bpt",
                         "/home/MapadeProcesos/mercadeo",
                         "/home/MapadeProcesos/produccion",
                         "/home/MapadeProcesos/aseguramiento",
                         "/home/MapadeProcesos/ventas_farma",
                         "/home/MapadeProcesos/hospitalaria",
                         "/home/MapadeProcesos/division_maquila",
                         "/home/MapadeProcesos/exportaciones",
                         "/home/MapadeProcesos/gb",
                         "/home/MapadeProcesos/geel",
                         "/home/MapadeProcesos/finanzas",
                         "/home/MapadeProcesos/creditos",
                         "/home/MapadeProcesos/contabilidad",
                         "/home/MapadeProcesos/costos"]
    elif username == "rrhh":
        return route == "/home/MapadeProcesos/rrhh"
    elif username == "infraestructura":
        return route == "/home/MapadeProcesos/infraestructura_y_equipo"
    elif username == "informatica":
        return route == "/home/MapadeProcesos/informatica"
    elif username == "operaciones":
        return route == "/home/MapadeProcesos/operaciones"
    elif username == "compras":
        return route == "/home/MapadeProcesos/compras"
    elif username == "bmp":
        return route == "/home/MapadeProcesos/bmp"
    elif username == "bpt":
        return route == "/home/MapadeProcesos/bpt"
    elif username == "mercadeo":
        return route == "/home/MapadeProcesos/mercadeo"
    elif username == "produccion":
        return route == "/home/MapadeProcesos/produccion"
    elif username == "aseguramiento":
        return route == "/home/MapadeProcesos/aseguramiento"
    elif username == "farma":
        return route == "/home/MapadeProcesos/ventas_farma"
    elif username == "hospitalaria":
        return route == "/home/MapadeProcesos/hospitalaria"
    elif username == "maquila":
        return route == "/home/MapadeProcesos/division_maquila"
    elif username == "exportaciones":
        return route == "/home/MapadeProcesos/exportaciones"
    elif username == "gb":
        return route == "/home/MapadeProcesos/gb"
    elif username == "heel":
        return route == "/home/MapadeProcesos/heel"
    elif username == "finanzas":
        return route == "/home/MapadeProcesos/finanzas"
    elif username == "creditos":
        return route == "/home/MapadeProcesos/creditos"
    elif username == "contabilidad":
        return route == "/home/MapadeProcesos/contabilidad"
    elif username == "costos":
        return route == "/home/MapadeProcesos/costos"
    else:
        return False

# MAPA DE PROCESOS 

@app.route('/home/MapadeProcesos/rrhh')
@login_required
def MapadeProcesos_RRHH():
    route = "/home/MapadeProcesos/rrhh"  # Definir la ruta
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/RRHH/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_RRHH                  Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/infraestructura_y_equipo')
@login_required
def MapadeProcesos_infraestructura_y_equipo():
    route = "/home/MapadeProcesos/infraestructura_y_equipo"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/InfraestructuraEquipo/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_InfraestructuraEquipo Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
        return

@app.route('/home/MapadeProcesos/informatica')
@login_required
def MapadeProcesos_informatica():
    route = "/home/MapadeProcesos/informatica"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/informatica/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Informatica           Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/operaciones')
@login_required
def MapadeProcesos_operaciones():
    route = "/home/MapadeProcesos/operaciones"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/operaciones/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_operaciones        Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/compras')
@login_required
def MapadeProcesos_compras():
    route = "/home/MapadeProcesos/compras"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/compras/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Compras        Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/bmp')
@login_required
def MapadeProcesos_bmp():
    route = "/home/MapadeProcesos/bmp"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/bmp/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_BMP        Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/bpt')
@login_required
def MapadeProcesos_bpt():
    route = "/home/MapadeProcesos/bpt"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/bpt/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_BPT        Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/mercadeo')
@login_required
def MapadeProcesos_mercadeo():
    route = "/home/MapadeProcesos/mercadeo"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/mercadeo/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Mercadeo              Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/produccion')
@login_required
def MapadeProcesos_produccion():
    route = "/home/MapadeProcesos/produccion"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/produccion/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Produccion            Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/aseguramiento')
@login_required
def MapadeProcesos_aseguramiento():
    route = "/home/MapadeProcesos/aseguramiento"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/aseguramiento/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Aseguramiento         Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/ventas_farma')
@login_required
def MapadeProcesos_ventas_farma():
    route = "/home/MapadeProcesos/ventas_farma"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/VentasFarma/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_VentasFarma         Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/hospitalaria')
@login_required
def MapadeProcesos_hospitalario():
    route = "/home/MapadeProcesos/hospitalaria"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/hospitalaria/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Hospitalaria         Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/division_maquila')
@login_required
def MapadeProcesos_division_maquila():
    route = "/home/MapadeProcesos/division_maquila"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/DivisionMaquila/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_DivisionMaquila         Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/exportaciones')
@login_required
def MapadeProcesos_exportaciones():
    route = "/home/MapadeProcesos/exportaciones"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/exportaciones/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Exportaciones         Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/gb')
@login_required
def MapadeProcesos_gb():
    route = "/home/MapadeProcesos/gb"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/gb/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_GB         Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/heel')
@login_required
def MapadeProcesos_heel():
    route = "/home/MapadeProcesos/heel"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/heel/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Geel    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/finanzas')
@login_required
def MapadeProcesos_finanzas():
    route = "/home/MapadeProcesos/finanzas"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/finanzas/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Finanzas    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/creditos')
@login_required
def MapadeProcesos_creditos():
    route = "/home/MapadeProcesos/creditos"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/creditos/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Creditos    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
@app.route('/home/MapadeProcesos/contabilidad')
@login_required
def MapadeProcesos_contabilidad():
    route = "/home/MapadeProcesos/contabilidad"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/contabilidad/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Contabilidad    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/costos')
@login_required
def MapadeProcesos_costos():
    route = "/home/MapadeProcesos/costos"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/costos/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Costos    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))

@app.route('/home/MapadeProcesos/gestion_de_calidad')
@login_required
def MapadeProcesos_gestion_de_calidad():
    route = "/home/MapadeProcesos/gestion_de_calidad"
    if check_permission(current_user.username, route):
        return render_template('iso/MapaDeProcesos/GestionCalidad/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_GestionCalidad    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
# ORGANIGRAMA Y PERFIL DE PUESTOS

@app.route('/home/Organigrama')
@login_required
def Organigrama():
    return render_template('iso/Organigrama/index.html')


@app.route('/home/Organigrama/produccion')
@login_required
def Org_produccion():
    route = "/home/Organigrama/produccion"
    if check_permission(current_user.username, route):
        return render_template('iso/Organigrama/produccion/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Ogranigrama_Produccion    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    


@app.route('/home/Organigrama/aseguramiento')
@login_required
def Org_aseguramiento():
    route = "/home/Organigrama/aseguramiento"
    if check_permission(current_user.username, route):
        return render_template('iso/Organigrama/aseguramiento/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Ogranigrama_Aseguramiento    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('MapadeProcesos'))
    
# IMPRESION DE FORMATOS (INFORMATICA)

@app.route('/home/Formato_Informatica')
@login_required
def Formato_Informatica():
    route = "/home/Formato_Informatica"
    if check_permission(current_user.username, route):
        return render_template('formatos/informatica/index.html')
    else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        app.logger.error(f"{current_time} | Intento de acceso sin permiso a la pagina Form_Formato_Informatica    Por el Usuario: {current_user.username}    Desde la IP: {request.remote_addr}")
        flash("No tiene permiso para acceder a esta página.", "error")
        return redirect(url_for('home'))

@app.route('/protected')
@login_required
def protected():
    return "<h1>This is a protected view, only for authenticated users.</h1>"


if __name__ == '__main__':
    app.run()