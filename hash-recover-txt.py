import os
import csv
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

def load_map_hashes_from_directory(directory_path):
    try:
        map_hashes = {}
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path) and filename.endswith(".txt"):
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        word_number, hash_value = line.strip().split(": ")
                        map_hashes[hash_value] = word_number
        return map_hashes
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el directorio de mapas de hashes: {e}")
        return {}

def load_tree_hashes_from_file():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                tree_hashes = [line.strip() for line in file.readlines()[1:]]  # Ignorar la primera línea (título)
            messagebox.showinfo("Éxito", "Árbol de hashes cargado correctamente.")
            return tree_hashes
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo de árbol de hashes: {e}")
        return []

def validate_hash(tree_hashes, map_hashes):
    try:
        hash_comprobatorio = ""
        for tree_hash in tree_hashes:
            if not tree_hash.strip():
                continue  # Salta la línea si está vacía
            if tree_hash in map_hashes:
                word_number = map_hashes[tree_hash]
                print(f"Coincidencia encontrada: {word_number} -> {tree_hash}")
            else:
                messagebox.showwarning("Advertencia", f"Verifica el hash probatorio de tu lista vs la lista creada para validar que la lista es integra: {tree_hash}")

            # Construir la cadena para el hash comprobatorio
            hash_comprobatorio += f"{word_number}-{tree_hash}\n"

        # Calcular el hash comprobatorio de la lista
        list_hash = hashlib.sha256(hash_comprobatorio.encode()).hexdigest()
        print(f"Hash comprobatorio de la lista: {list_hash}")

        # Escribir la cadena en un archivo de texto plano
        with open("hash_comprobatorio.txt", "w") as file:
            file.write(hash_comprobatorio)

        print("La cadena para el hash comprobatorio se ha guardado en el archivo 'hash_comprobatorio.txt'")

    except Exception as e:
        messagebox.showerror("Error", f"Error al validar el hash: {e}")

def main():
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Directorio donde se encuentran los archivos de mapa de hashes
    directory_path = filedialog.askdirectory(title="Seleccionar directorio de mapas de hashes")
    if directory_path:
        # Cargar el mapa de hashes desde el directorio
        map_hashes = load_map_hashes_from_directory(directory_path)
        if map_hashes:
            messagebox.showinfo("Éxito", "Diccionario creado satisfactoriamente.")

    # Cargar el árbol de hashes desde un archivo
    tree_hashes = load_tree_hashes_from_file()
    print(tree_hashes)  # Solo para verificar que se cargó correctamente

    # Validar el hash
    if map_hashes and tree_hashes:
        validate_hash(tree_hashes, map_hashes)

    root.mainloop()

if __name__ == "__main__":
    main()