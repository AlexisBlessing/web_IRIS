import os

def renombrar_webp():
    carpeta = os.getcwd()   # Carpeta donde se ejecuta el script

    # Listar todos los archivos .webp
    archivos = [f for f in os.listdir(carpeta) if f.lower().endswith(".webp")]

    if not archivos:
        print("No se encontraron imágenes .webp en esta carpeta.")
        return

    # Ordenar alfabéticamente para mantener un orden consistente
    archivos.sort()

    print(f"Se encontraron {len(archivos)} archivos .webp\n")

    # Renombrado seguro: primero renombramos a nombres temporales para evitar conflictos
    temporales = []

    for i, archivo in enumerate(archivos):
        temporal = f"temp_{i}.webp"
        os.rename(archivo, temporal)
        temporales.append(temporal)

    # Ahora renombramos a 1.webp, 2.webp, ..., n.webp
    for i, temporal in enumerate(temporales, start=1):
        nuevo_nombre = f"{i}.webp"
        os.rename(temporal, nuevo_nombre)
        print(f"{temporal} → {nuevo_nombre}")

    print("\n¡Renombrado completado!")

if __name__ == "__main__":
    renombrar_webp()
