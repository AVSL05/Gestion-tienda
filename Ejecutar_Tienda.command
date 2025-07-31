#!/bin/bash

# Script para ejecutar la Tienda fácilmente en macOS
# Guarda este archivo como "Ejecutar_Tienda.command" y haz doble clic

echo "🏪 SISTEMA DE GESTIÓN DE TIENDA"
echo "======================================"
echo "📍 Ubicación: $(pwd)"

# Navegar al directorio de la aplicación
cd "$(dirname "$0")"

# Función para verificar Python
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        echo "❌ Python no encontrado en el sistema"
        return 1
    fi
    
    echo "🐍 Usando: $PYTHON_CMD ($(${PYTHON_CMD} --version))"
    return 0
}

# Verificar Python
if ! check_python; then
    echo "📝 Instala Python desde https://python.org"
    read -p "Presiona Enter para cerrar..."
    exit 1
fi

# Activar entorno virtual si existe
if [ -d ".venv" ]; then
    echo "✅ Activando entorno virtual..."
    source .venv/bin/activate
    
    echo "🚀 Ejecutando aplicación con configuración optimizada..."
    ${PYTHON_CMD} run_app.py
else
    echo "⚠️  Entorno virtual no encontrado"
    echo "📝 Ejecutando con Python del sistema..."
    
    # Verificar que PyQt6 esté instalado
    if ! ${PYTHON_CMD} -c "import PyQt6" 2>/dev/null; then
        echo "❌ PyQt6 no está instalado"
        echo "📝 Instala las dependencias con: pip install -r requirements.txt"
        read -p "Presiona Enter para cerrar..."
        exit 1
    fi
    
    echo "🚀 Ejecutando aplicación..."
    export QT_QPA_PLATFORM=cocoa
    ${PYTHON_CMD} main.py
fi

echo ""
echo "👋 Aplicación cerrada"
read -p "Presiona Enter para cerrar esta ventana..."
