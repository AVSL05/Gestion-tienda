#!/usr/bin/env python3
"""
Script para crear una aplicación ejecutable de la Tienda
"""
import os
import subprocess
import sys

def build_executable():
    """Crear ejecutable con PyInstaller"""
    print("🔨 Creando aplicación ejecutable...")
    
    # Comando PyInstaller con configuraciones optimizadas
    cmd = [
        "pyinstaller",
        "--onefile",                    # Un solo archivo
        "--windowed",                   # Sin ventana de terminal
        "--name=TiendaGestion",         # Nombre de la aplicación
        "--add-data=database.py:.",     # Incluir archivos necesarios
        "--add-data=models.py:.",
        "--add-data=utils.py:.",
        "--add-data=gui.py:.",
        "--hidden-import=PyQt6",        # Asegurar que PyQt6 se incluya
        "--hidden-import=pymongo",      # Asegurar que pymongo se incluya
        "--hidden-import=dotenv",       # Asegurar que python-dotenv se incluya
        "main.py"
    ]
    
    try:
        # Ejecutar PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ ¡Aplicación creada exitosamente!")
        print("📁 El ejecutable está en: dist/TiendaGestion")
        print("\n📋 Instrucciones:")
        print("1. Ve a la carpeta 'dist'")
        print("2. Copia 'TiendaGestion' donde quieras")
        print("3. Haz doble clic para ejecutar")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al crear la aplicación: {e}")
        print("Salida del error:", e.stderr)
    except FileNotFoundError:
        print("❌ PyInstaller no encontrado. Instalando...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller instalado. Ejecuta este script de nuevo.")

if __name__ == "__main__":
    build_executable()
