# 🏪 Sistema de Gestión de Tienda

Un sistema completo de gestión de inventario para pequeñas tiendas, desarrollado en Python con interfaz gráfica moderna.

![Python](https://img.shields.io/badge/python-v3.13+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-GUI-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Características

- 📦 **Gestión de Inventario**: Control completo de stock por cantidades
- 💰 **Cálculos Automáticos**: Inversión, ganancias y márgenes en tiempo real
- 🛒 **Ventas Inteligentes**: Venta parcial de productos con stock múltiple
- 📊 **Estadísticas Visuales**: Dashboard con ganancias totales y estado del inventario
- 🎨 **Interfaz Moderna**: Diseño intuitivo con códigos de colores
- 💾 **Base de Datos**: Almacenamiento persistente con MongoDB
- 🖥️ **Ejecutable**: Aplicación independiente sin necesidad de instalar Python

## 🚀 Instalación y Uso

### Opción 1: Ejecutable (Recomendado para usuarios finales)

1. Descarga el archivo `TiendaGestion_ParaUsuarios.zip` desde [Releases](../../releases)
2. Descomprime el archivo
3. Haz doble clic en `TiendaGestion.app` (macOS)
4. ¡Listo! La aplicación se ejecutará automáticamente

### Opción 2: Desde el código fuente

#### Prerrequisitos
- Python 3.13+
- MongoDB (local o remoto)

#### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/sistema-gestion-tienda.git
cd sistema-gestion-tienda

# Crear entorno virtual
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python main.py
```

## 🛠️ Desarrollo

### Estructura del Proyecto
```
sistema-gestion-tienda/
├── main.py              # Punto de entrada de la aplicación
├── gui.py               # Interfaz gráfica (PyQt6)
├── models.py            # Modelos de datos (Product)
├── database.py          # Conexión y operaciones de MongoDB
├── utils.py             # Utilidades auxiliares
├── requirements.txt     # Dependencias del proyecto
├── build_app.py         # Script para crear ejecutable
├── create_user_package.py # Script para paquete de distribución
├── Ejecutar_Tienda.command # Script de ejecución rápida
└── README.md            # Este archivo
```

### Tecnologías Utilizadas
- **Python 3.13**: Lenguaje principal
- **PyQt6**: Framework de interfaz gráfica
- **MongoDB**: Base de datos NoSQL
- **PyMongo**: Driver de MongoDB para Python
- **PyInstaller**: Creación de ejecutables
- **python-dotenv**: Gestión de variables de entorno

### Crear Ejecutable
```bash
# Instalar PyInstaller
pip install pyinstaller

# Crear ejecutable
python build_app.py

# Crear paquete para distribución
python create_user_package.py
```

## 📋 Funcionalidades Detalladas

### Gestión de Productos
- ✅ Agregar productos con información completa
- ✅ Categorización automática
- ✅ Control de cantidad por producto
- ✅ Cálculo automático de inversión total
- ✅ Previsualización de ganancias esperadas
- ✅ Validación de datos en tiempo real

### Sistema de Ventas
- ✅ Venta de cantidades específicas
- ✅ Control automático de stock
- ✅ Actualización de inventario en tiempo real
- ✅ Registro de ventas parciales
- ✅ Confirmaciones de seguridad

### Análisis y Reportes
- ✅ Dashboard con estadísticas en tiempo real
- ✅ Ganancia total acumulada
- ✅ Productos disponibles vs vendidos
- ✅ Alertas de stock bajo
- ✅ Estados visuales por colores

## 🎯 Casos de Uso

### Pequeña Tienda de Ropa
- Gestiona inventario de zapatos, ropa, accesorios
- Control de tallas y cantidades
- Cálculo de márgenes de ganancia

### Tienda de Perfumería
- Inventario de perfumes y cosméticos
- Control de stock por unidades
- Seguimiento de productos más vendidos

### Negocio de Accesorios
- Gestión de joyería, bolsas, mochilas
- Control preciso de inventario
- Análisis de rentabilidad por producto

## 🔧 Configuración

### Variables de Entorno (Opcional)
Crea un archivo `.env` en la raíz del proyecto:
```env
MONGODB_URI=mongodb://localhost:27017/
```

### Categorías de Productos
Las categorías predefinidas incluyen:
- Joyería
- Perfumería
- Calzado
- Bolsas
- Mochilas
- Cobertores
- Sábanas

*Puedes modificar las categorías en `models.py`*

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la sección de [Issues](../../issues)
2. Crea un nuevo issue si no encuentras solución
3. Proporciona detalles del error y tu sistema operativo

## 🚀 Roadmap

### Próximas Funcionalidades
- [ ] Exportación de reportes a PDF/Excel
- [ ] Sistema de códigos de barras
- [ ] Múltiples sucursales
- [ ] API REST para integración
- [ ] Aplicación móvil complementaria
- [ ] Sistema de usuarios y permisos
- [ ] Backup automático de datos

---

**Desarrollado con ❤️ para pequeños negocios**

*¿Te gusta el proyecto? ¡Dale una ⭐ en GitHub!*
