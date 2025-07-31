#!/usr/bin/env python3
"""
Script de configuración para PyQt6
Soluciona problemas comunes de plugins en macOS
"""

import os
import sys
import platform

def setup_qt_environment():
    """Configura las variables de entorno necesarias para PyQt6"""
    
    print(f"🖥️  Sistema: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    
    # Configuración mínima y efectiva para macOS
    os.environ['QT_QPA_PLATFORM'] = 'cocoa'
    
    print("✅ PyQt6 configurado para macOS")
    return True

def test_qt_import():
    """Prueba la importación de Qt antes de ejecutar la app"""
    try:
        print("🧪 Probando importación de PyQt6...")
        from PyQt6.QtWidgets import QApplication
        from PyQt6.QtCore import qVersion
        
        print("✅ PyQt6 importado correctamente")
        print(f"🏷️  Qt Version: {qVersion()}")
        return True
        
    except Exception as e:
        print(f"❌ Error importando PyQt6: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("🏪 INICIANDO SISTEMA DE GESTIÓN DE TIENDA")
    print("=" * 60)
    
    # Configurar entorno
    if not setup_qt_environment():
        print("❌ No se pudo configurar el entorno de PyQt6")
        sys.exit(1)
    
    print("-" * 60)
    
    # Probar importación de Qt
    if not test_qt_import():
        print("❌ PyQt6 no se puede importar correctamente")
        sys.exit(1)
    
    print("-" * 60)
    print("🚀 Iniciando aplicación...")
    
    # Importar y ejecutar la aplicación
    try:
        from main import main
        main()
    except Exception as e:
        print(f"❌ Error ejecutando la aplicación: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
