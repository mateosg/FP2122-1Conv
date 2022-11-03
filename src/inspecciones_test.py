from inspecciones import *

def test_vehiculos_mas_antiguos(inspecciones, año, n):
    print(vehiculos_mas_antiguos(inspecciones, año, n))

def test_proximas_inspecciones(inspecciones):
    print(proximas_inspecciones(inspecciones))

def test_estacion_mayor_porcentaje_inspecciones_favorables(inspecciones, estaciones):
    print(estacion_mayor_porcentaje_inspecciones_favorables(inspecciones, estaciones))

def test_tipos_de_vehiculos_mas_inspeccionados(inspecciones, f1=None, f2=None):
    print(tipos_de_vehiculos_mas_inspeccionados(inspecciones, f1, f2))

def test_incrementos_recaudacion_estacion(inspecciones, estacion):
    print(incrementos_recaudacion_estacion(inspecciones, estacion))

########################### Llamadas a tests ###########################

if __name__=='__main__':
    #leer fichero
    inspecciones=lee_inspecciones('data/inspecciones.csv')
    #mostrar los tres primeros
    print("los tres primeros:\n")
    for i in inspecciones[:3]:
        print(i)
    #mostrar los tres últimos
    print("\nlos tres últimos:\n")
    for i in inspecciones[-3:]:
        print(i)
    #mostrar los vehículos más antiguos
    print("\nlos 3 vehículos más antiguos en el año 2021 con evaluación positiva:\n")
    test_vehiculos_mas_antiguos(inspecciones, 2021, 3)

    #mostrar las próximas inspecciones
    print("\nlas próximas inspecciones:\n")
    test_proximas_inspecciones(inspecciones)

    #mostrar la estación con mayor porcentaje de inspecciones favorables
    print("\nla estación con mayor porcentaje de inspecciones favorables:\n")
    test_estacion_mayor_porcentaje_inspecciones_favorables(inspecciones,['Alcalá de Guadaíra','Sevilla-Gelves','Sevilla-El Pino'])

    #mostrar los tipos de vehículos más inspeccionados
    print("\nlos tipos de vehículos más inspeccionados:\n")
    test_tipos_de_vehiculos_mas_inspeccionados(inspecciones)

    #mostrar los incrementos de recaudación de una estación
    print("\nlos incrementos de recaudación de la estación Sevilla-Gelves:\n")
    test_incrementos_recaudacion_estacion(inspecciones,'Sevilla-El Pino')
    

