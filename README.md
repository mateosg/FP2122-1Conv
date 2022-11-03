## Salida esperada: ##
```	
las tres primeros:

Inspeccion(fecha_inspeccion=datetime.datetime(2022, 6, 7, 0, 0), estacion='Sevilla-El Pino', numero=1, fecha_limite=datetime.datetime(2022, 6, 14, 0, 0), matricula='3595KLW', tipo='Turismo gasolina', fecha_matriculacion=datetime.datetime(2018, 6, 14, 0, 0), favorable=True)
Inspeccion(fecha_inspeccion=datetime.datetime(2022, 2, 23, 0, 0), estacion='Sevilla-Gelves', numero=1, fecha_limite=datetime.datetime(2022, 2, 28, 0, 0), matricula='6577KJP', tipo='Turismo gasolina', fecha_matriculacion=datetime.datetime(2018, 2, 28, 0, 0), favorable=False)
Inspeccion(fecha_inspeccion=datetime.datetime(2021, 12, 18, 0, 0), estacion='La Rinconada', numero=1, fecha_limite=datetime.datetime(2021, 12, 19, 0, 0), matricula='2324JJJ', tipo='Turismo diésel', fecha_matriculacion=datetime.datetime(2015, 12, 19, 0, 0), favorable=True)

las tres últimos:

Inspeccion(fecha_inspeccion=datetime.datetime(2022, 1, 5, 0, 0), estacion='Alcalá de Guadaíra', numero=2, fecha_limite=datetime.datetime(2022, 1, 3, 0, 0), matricula='3242JMV', tipo='Turismo diésel', fecha_matriculacion=datetime.datetime(2016, 1, 3, 0, 0), favorable=True)
Inspeccion(fecha_inspeccion=datetime.datetime(2021, 2, 19, 0, 0), estacion='Sevilla-Gelves', numero=1, fecha_limite=datetime.datetime(2021, 2, 21, 0, 0), matricula='1234JGP', tipo='Turismo eléctrico', fecha_matriculacion=datetime.datetime(2015, 2, 21, 
0, 0), favorable=True)
Inspeccion(fecha_inspeccion=datetime.datetime(2017, 4, 5, 0, 0), estacion='Sevilla-El Pino', numero=1, fecha_limite=datetime.datetime(2019, 3, 27, 0, 0), matricula='4545FNY', tipo='Turismo diésel', fecha_matriculacion=datetime.datetime(2007, 3, 15, 0, 
0), favorable=False)

los 3 vehículos más antiguos en el año 2021 con evaluación positiva:

['1234JGP', '8244JFT', '2324JJJ']

las próximas inspecciones:

[('3595KLW', datetime.datetime(2024, 6, 6, 0, 0)), ('2324JJJ', datetime.datetime(2023, 12, 18, 0, 0)), ('8244JFT', datetime.datetime(2023, 2, 24, 0, 0)), ('7734KGB', datetime.datetime(2024, 3, 16, 0, 0)), ('6724JPP', datetime.datetime(2024, 3, 13, 0, 0)), ('5523HST', datetime.datetime(2022, 11, 9, 0, 0)), ('3242JMV', datetime.datetime(2024, 1, 5, 0, 0)), ('1234JGP', datetime.datetime(2023, 2, 19, 0, 0))]

la estación con mayor porcentaje de inspecciones favorables:

('Alcalá de Guadaíra', 100.0)

los tipos de vehículos más inspeccionados:

{'Sevilla-El Pino': 'Turismo gasolina', 'Sevilla-Gelves': 'Turismo gasolina', 'La Rinconada': 'Turismo diésel', 'Alcalá de Guadaíra': 'Turismo gasolina'}

los incrementos de recaudación de la estación Sevilla-Gelves:

[-34.966029999999996, 0, 30.370449999999998, -1.2644499999999965, 1.2644499999999965]
```	