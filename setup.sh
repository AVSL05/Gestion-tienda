#!/bin/bash

# Script de configuración automática para el Sistema de Gestión de Tienda
# Ejecuta: chmod +x setup.sh && ./setup.sh

echo "🏪 CONFIGURACIÓN DEL SISTEMA DE GESTIÓN DE TIENDA"
echo "================================================="

# Verificar que estamos en el directorio correcto
if [ ! -f "main.py" ]; then
    echo "❌ Error: Este script debe ejecutarse desde el directorio del proyecto"
    echo "📝 Asegúrate de estar en la carpeta que contiene main.py"
    exit 1
fi

# Verificar Python
echo "🐍 Verificando Python..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Python no encontrado"
    echo "📝 Instala Python desde https://python.org"
    exit 1
fi

PYTHON_VERSION=$(${PYTHON_CMD} --version | grep -oE '[0-9]+\.[0-9]+')
echo "✅ Python ${PYTHON_VERSION} encontrado"

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
if [ -d ".venv" ]; then
    echo "⚠️  El entorno virtual ya existe"
    read -p "¿Quieres recrearlo? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -rf .venv
        ${PYTHON_CMD} -m venv .venv
        echo "✅ Entorno virtual recreado"
    else
        echo "✅ Usando entorno virtual existente"
    fi
else
    ${PYTHON_CMD} -m venv .venv
    echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
echo "🔌 Activando entorno virtual..."
source .venv/bin/activate

# Actualizar pip
echo "⬆️  Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "📚 Instalando dependencias..."
pip install -r requirements.txt

# Verificar instalación de PyQt6
echo "🧪 Verificando PyQt6..."
if ${PYTHON_CMD} -c "from PyQt6.QtCore import qVersion; print(f'PyQt6 {qVersion()} instalado correctamente')" 2>/dev/null; then
    echo "✅ PyQt6 funciona correctamente"
else
    echo "⚠️  Problema con PyQt6, instalando versión compatible..."
    pip uninstall PyQt6 PyQt6-Qt6 -y
    pip install PyQt6==6.7.1
    echo "✅ PyQt6 6.7.1 instalado (compatible con macOS M1/M2)"
fi

# Hacer ejecutables los scripts
echo "🔐 Configurando permisos..."
chmod +x Ejecutar_Tienda.command
chmod +x run_app.py

echo ""
echo "🎉 ¡CONFIGURACIÓN COMPLETADA!"
echo "=============================="
echo ""
echo "📋 Para ejecutar la aplicación:"
echo "   • Doble clic en: Ejecutar_Tienda.command"
echo "   • O desde terminal: python run_app.py"
echo ""
echo "📋 Para crear un ejecutable:"
echo "   • python build_app.py"
echo ""
echo "📋 Para crear paquete de distribución:"
echo "   • python create_user_package.py"
echo ""
echo "🔗 Documentación completa en README.md"
echo ""

read -p "¿Quieres ejecutar la aplicación ahora? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Iniciando aplicación..."
    ${PYTHON_CMD} run_app.py
fi
