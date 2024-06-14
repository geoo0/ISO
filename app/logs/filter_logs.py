'''pimport re

def filtrar_accesos_no_autorizados(ruta_archivo_log):
    patron_acceso_no_autorizado = re.compile(r'ERROR in app: .*')

    with open(ruta_archivo_log, 'r', encoding='utf-8') as archivo_log:
        for linea in archivo_log:
            match = patron_acceso_no_autorizado.search(linea)
            if match:
                print(f"Coincidencia encontrada: {match.group()}")

if __name__ == '__main__':
    ruta_archivo_log = '/home/geo/Escritorio/Proyectos/ISO/error.log'
    filtrar_accesos_no_autorizados(ruta_archivo_log)

print('Reporte finalizado')'''


import re
import datetime

def filtrar_accesos_no_autorizados(ruta_archivo_log, ruta_reporte):
    patron_acceso_no_autorizado = re.compile(r'ERROR in app: .*')
    ayer = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    with open(ruta_archivo_log, 'r', encoding='utf-8') as archivo_log, open(ruta_reporte, 'w', encoding='utf-8') as archivo_reporte:
        for linea in archivo_log:
            if ayer in linea:
                match = patron_acceso_no_autorizado.search(linea)
                if match:
                    archivo_reporte.write(f"Coincidencia encontrada: {match.group()}\n")

if __name__ == '__main__':
    ruta_archivo_log = '/home/geo/Escritorio/Proyectos/ISO/error.log'
    fecha_ayer = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    ruta_reporte = f'/home/geo/Escritorio/Proyectos/ISO/app/static/doc/pdf/web/Bonin_ISO/REPORTES/reporte_{fecha_ayer}.txt'
    
    filtrar_accesos_no_autorizados(ruta_archivo_log, ruta_reporte)

print('Reporte finalizado')