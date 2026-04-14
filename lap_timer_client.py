# lap_timer_client.py
# Programa cliente que lee tiempos de vuelta de un archivo
# e imprime la racha decreciente mas larga.

import lap_timer


def main():
    nombre_archivo = input("Nombre del archivo: ")
    
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if not lineas:
                return
            
            n = int(lineas[0].strip())
            datos_vueltas = lap_timer.init()
            
            for i in range(1, n + 1):
                tiempo = float(lineas[i].strip())
                lap_timer.add_lap(datos_vueltas, tiempo)

            tiempos = datos_vueltas['laps']
            
            max_racha = 0
            racha_actual = 0
            
            for j in range(len(tiempos)):
                if j > 0 and tiempos[j] < tiempos[j-1]:
                    racha_actual += 1
                else:
        
                     if racha_actual > max_racha:
                        max_racha = racha_actual
            
            print(max_racha)

    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()