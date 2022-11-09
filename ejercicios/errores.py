# "Programa de manejo de errores:"

def divisioncero():
    x = 1/0
def except2():
    try:
        divisioncero()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
#except2()
# EXCEPCIONES MULTIPLES
# Gracias a los identificadores de errores podemos crear múltiples comprobaciones,
# siempre que dejemos en último lugar la excepción por defecto
# Excepcion que engloba cualquier tipo de error
# (si la pusiéramos al principio las demas excepciones nunca se ejecutarían):
def except3():
    try:
        n = float(input("Introduce un número divisor: "))
        5/n
    except TypeError:
        print("No se puede dividir el número entre una cadena")
    except ValueError:
        print("Debes introducir una cadena que sea un número")
    except ZeroDivisionError:
        print("No se puede dividir por cero, prueba otro número")
    except (ValueError, TypeError):
        print("Ha ocurrido un error")
    except Exception as e:
        print("Ha ocurrido un error no previsto", type(e).__name__ )
except3()