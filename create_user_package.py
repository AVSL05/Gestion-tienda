#!/usr/bin/env python3
"""
Instalador automático para el Sistema de Gestión de Tienda
Este script prepara todo para que usuarios finales puedan usar la aplicación fácilmente
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def create_user_package():
    """Crear paquete para usuario final"""
    print("📦 Creando paquete para usuario final...")
    
    # Crear carpeta de distribución
    user_package = Path("TiendaGestion_ParaUsuarios")
    if user_package.exists():
        shutil.rmtree(user_package)
    user_package.mkdir()
    
    # Copiar ejecutable
    dist_path = Path("dist")
    if dist_path.exists():
        # Copiar la aplicación .app si existe
        app_file = dist_path / "TiendaGestion.app"
        executable_file = dist_path / "TiendaGestion"
        
        if app_file.exists():
            shutil.copytree(app_file, user_package / "TiendaGestion.app")
            print("✅ Aplicación .app copiada")
        elif executable_file.exists():
            shutil.copy2(executable_file, user_package / "TiendaGestion")
            print("✅ Ejecutable copiado")
        else:
            print("❌ No se encontró el ejecutable. Ejecuta build_app.py primero")
            return False
    
    # Crear instrucciones simples
    instructions = """
🏪 SISTEMA DE GESTIÓN DE TIENDA
================================

🚀 INSTRUCCIONES FÁCILES:

1. Haz DOBLE CLIC en "TiendaGestion" o "TiendaGestion.app"
2. Si aparece una advertencia de seguridad:
   - Ve a Preferencias del Sistema → Seguridad y Privacidad
   - Haz clic en "Abrir de todas formas"
3. ¡Listo! La aplicación se abrirá

💡 QUÉ HACE LA APLICACIÓN:
- ➕ Agregar productos con cálculo automático de ganancias
- 📋 Ver inventario completo
- 💰 Marcar productos como vendidos
- 📊 Calcular ganancias totales

🔄 PARA MOVER A OTRA COMPUTADORA:
- Copia toda esta carpeta
- Haz doble clic en la aplicación
- ¡Ya funciona!

📞 Si tienes problemas:
- Asegúrate de tener macOS 10.14 o superior
- Permite aplicaciones de desarrolladores identificados
- La aplicación creará automáticamente su base de datos

---
¡Disfruta gestionando tu tienda! 🎉
"""
    
    with open(user_package / "INSTRUCCIONES.txt", "w", encoding="utf-8") as f:
        f.write(instructions)
    
    print("✅ Instrucciones creadas")
    
    # Crear un script de lanzamiento alternativo
    launcher_script = """#!/bin/bash
echo "🏪 Iniciando Sistema de Gestión de Tienda..."
cd "$(dirname "$0")"

if [ -f "TiendaGestion.app/Contents/MacOS/TiendaGestion" ]; then
    echo "🚀 Ejecutando aplicación..."
    open TiendaGestion.app
elif [ -f "TiendaGestion" ]; then
    echo "🚀 Ejecutando aplicación..."
    ./TiendaGestion
else
    echo "❌ No se encontró la aplicación"
    echo "📝 Busca el archivo TiendaGestion o TiendaGestion.app"
fi

echo "✅ Lanzamiento completado"
"""
    
    launcher_path = user_package / "Ejecutar_Tienda.command"
    with open(launcher_path, "w") as f:
        f.write(launcher_script)
    
    # Hacer ejecutable el launcher
    os.chmod(launcher_path, 0o755)
    print("✅ Script de lanzamiento creado")
    
    print(f"\n🎉 ¡Paquete listo en: {user_package}/")
    print("\n📋 PARA DISTRIBUIR:")
    print(f"1. Comprime la carpeta '{user_package}'")
    print("2. Envía el archivo ZIP a los usuarios")
    print("3. Los usuarios solo necesitan:")
    print("   - Descomprimir")
    print("   - Hacer doble clic en la aplicación")
    print("   - ¡Listo!")
    
    return True

if __name__ == "__main__":
    create_user_package()
