#!/bin/bash

# Script para ejecutar la Tienda fácilmente en macOS
# Guarda este archivo como "Ejecutar_Tienda.command" y haz doble clic

echo "🏪 Iniciando Sistema de Gestión de Tienda..."
echo "📍 Ubicación: $(pwd)"

# Navegar al directorio de la aplicación
cd "$(dirname "$0")"

# Activar entorno virtual y ejecutar
if [ -d ".venv" ]; then
    echo "✅ Activando entorno virtual..."
    source .venv/bin/activate
    echo "🚀 Ejecutando aplicación..."
    python main.py
else
    echo "❌ Entorno virtual no encontrado"
    echo "📝 Ejecutando con Python del sistema..."
    python3 main.py
fi

echo "👋 Aplicación cerrada"
read -p "Presiona Enter para cerrar esta ventana..."
