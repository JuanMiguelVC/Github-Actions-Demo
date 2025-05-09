import random
import string


def generar_clave(longitud, incluir_especiales=True):
    """Genera una contraseña aleatoria."""
    caracteres = string.ascii_letters + string.digits
    if incluir_especiales:
        caracteres += string.punctuation

    # Añadido: Validación de la longitud
    if longitud < 1:
        raise ValueError(
            "La longitud de la contraseña debe ser mayor que cero.")

    clave = ''.join(random.choice(caracteres) for i in range(longitud))
    return clave


def generar_multiples_claves(num_claves, longitud, incluir_especiales=True):
    """Genera múltiples contraseñas."""
    claves = []
    for _ in range(num_claves):
        claves.append(generar_clave(longitud, incluir_especiales))
    return claves


def main():  # Encapsula la interacción con el usuario
    """Función principal para ejecutar el generador de contraseñas."""
    try:
        num_claves = int(input("How many passwords do you want to generate? "))
        longitud = int(input("Enter the desired password length: "))
        incluir_especiales = input(
            "Include special characters? (y/n) ").lower() == 'y'

        claves = generar_multiples_claves(
            num_claves, longitud, incluir_especiales)

        print("\nGenerated Passwords:")
        for clave in claves:
            print(clave)
    except ValueError:
        print("Error: Invalid input. Please enter numbers for the number of passwords and length.")


if __name__ == "__main__":
    main()
