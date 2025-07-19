from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton,
                           QLabel, QLineEdit, QComboBox, QMessageBox, 
                           QTableWidget, QTableWidgetItem, QHBoxLayout,
                           QGroupBox, QFormLayout, QHeaderView, QFrame,
                           QSpacerItem, QSizePolicy, QSpinBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette
from models import Product
from database import DatabaseConnection

class StoreGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('🏪 Sistema de Gestión de Tienda')
        self.setGeometry(100, 100, 900, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 15px;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QLabel {
                font-size: 12px;
                color: #333;
            }
        """)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Título principal
        title_label = QLabel('Sistema de Gestión de Tienda')
        title_label.setFont(QFont('Arial', 24, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title_label)

        # Grupo de botones principales
        buttons_group = QGroupBox("Acciones Principales")
        buttons_group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
            }
        """)
        buttons_layout = QVBoxLayout(buttons_group)
        buttons_layout.setSpacing(15)

        # Botón agregar producto
        add_button = QPushButton('➕ Agregar Producto')
        add_button.clicked.connect(self.show_add_product_window)
        add_button.setMinimumHeight(60)
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        buttons_layout.addWidget(add_button)

        # Botón ver inventario
        view_button = QPushButton('📋 Ver Inventario')
        view_button.clicked.connect(self.show_inventory_window)
        view_button.setMinimumHeight(60)
        view_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        buttons_layout.addWidget(view_button)

        layout.addWidget(buttons_group)
        
        # Espaciador
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

    def show_add_product_window(self):
        self.add_window = AddProductWindow(self.db)
        self.add_window.show()

    def show_inventory_window(self):
        self.inventory_window = InventoryWindow(self.db)
        self.inventory_window.show()

class AddProductWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('➕ Agregar Nuevo Producto')
        self.setGeometry(200, 200, 500, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QGroupBox {
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 12px;
            }
            QLineEdit:focus, QComboBox:focus {
                border-color: #3498db;
            }
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Título
        title_label = QLabel('Agregar Nuevo Producto')
        title_label.setFont(QFont('Arial', 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title_label)

        # Grupo de información del producto
        product_group = QGroupBox("Información del Producto")
        form_layout = QFormLayout(product_group)
        form_layout.setSpacing(15)

        # Categoría
        self.category_combo = QComboBox()
        self.category_combo.addItems(Product.CATEGORIES)
        self.category_combo.setMinimumHeight(40)
        form_layout.addRow("🏷️ Categoría:", self.category_combo)

        # Nombre
        self.name_entry = QLineEdit()
        self.name_entry.setPlaceholderText("Ej: iPhone 13 Pro")
        self.name_entry.setMinimumHeight(40)
        form_layout.addRow("📱 Nombre:", self.name_entry)

        # Descripción
        self.desc_entry = QLineEdit()
        self.desc_entry.setPlaceholderText("Descripción del producto...")
        self.desc_entry.setMinimumHeight(40)
        form_layout.addRow("📝 Descripción:", self.desc_entry)

        # Cantidad
        self.quantity_entry = QLineEdit()
        self.quantity_entry.setPlaceholderText("1")
        self.quantity_entry.setText("1")
        self.quantity_entry.setMinimumHeight(40)
        form_layout.addRow("📦 Cantidad en Stock:", self.quantity_entry)

        layout.addWidget(product_group)

        # Grupo de precios
        price_group = QGroupBox("Información de Precios")
        price_layout = QFormLayout(price_group)
        price_layout.setSpacing(15)

        # Precio de costo
        self.cost_entry = QLineEdit()
        self.cost_entry.setPlaceholderText("0.00")
        self.cost_entry.setMinimumHeight(40)
        price_layout.addRow("💰 Precio de Costo:", self.cost_entry)

        # Precio de venta
        self.price_entry = QLineEdit()
        self.price_entry.setPlaceholderText("0.00")
        self.price_entry.setMinimumHeight(40)
        price_layout.addRow("💸 Precio de Venta:", self.price_entry)

        layout.addWidget(price_group)

        # Grupo de cálculos automáticos
        calc_group = QGroupBox("📊 Cálculos Automáticos")
        calc_layout = QFormLayout(calc_group)
        calc_layout.setSpacing(15)

        # Inversión total
        self.investment_label = QLabel("$0.00")
        self.investment_label.setStyleSheet("""
            QLabel {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        calc_layout.addRow("📈 Inversión Total:", self.investment_label)

        # Ganancia esperada
        self.profit_label = QLabel("$0.00")
        self.profit_label.setStyleSheet("""
            QLabel {
                background-color: #27ae60;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        calc_layout.addRow("💰 Ganancia Esperada:", self.profit_label)

        # Margen de ganancia
        self.margin_label = QLabel("0%")
        self.margin_label.setStyleSheet("""
            QLabel {
                background-color: #9b59b6;
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
            }
        """)
        calc_layout.addRow("📊 Margen de Ganancia:", self.margin_label)

        layout.addWidget(calc_group)

        # Conectar eventos para cálculo en tiempo real
        self.cost_entry.textChanged.connect(self.calculate_profits)
        self.price_entry.textChanged.connect(self.calculate_profits)
        self.quantity_entry.textChanged.connect(self.calculate_profits)

        # Botón guardar
        save_button = QPushButton('💾 Guardar Producto')
        save_button.clicked.connect(self.save_product)
        save_button.setMinimumHeight(50)
        save_button.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #229954;
            }
        """)
        layout.addWidget(save_button)

        # Espaciador
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

    def calculate_profits(self):
        """Calcula la inversión, ganancia y margen en tiempo real"""
        try:
            cost_text = self.cost_entry.text().strip()
            price_text = self.price_entry.text().strip()
            quantity_text = self.quantity_entry.text().strip()
            
            if not cost_text or not price_text or not quantity_text:
                self.investment_label.setText("$0.00")
                self.profit_label.setText("$0.00")
                self.margin_label.setText("0%")
                return
            
            cost = float(cost_text)
            price = float(price_text)
            quantity = int(quantity_text)
            
            # Calcular valores por cantidad total
            total_investment = cost * quantity
            profit_per_unit = price - cost
            total_profit = profit_per_unit * quantity
            margin = (profit_per_unit / price * 100) if price > 0 else 0
            
            # Actualizar etiquetas con colores según el resultado
            self.investment_label.setText(f"${total_investment:.2f}")
            
            # Configurar color de ganancia según si es positiva o negativa
            if total_profit > 0:
                self.profit_label.setStyleSheet("""
                    QLabel {
                        background-color: #27ae60;
                        color: white;
                        padding: 10px;
                        border-radius: 5px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                """)
                self.profit_label.setText(f"+${total_profit:.2f}")
            elif total_profit < 0:
                self.profit_label.setStyleSheet("""
                    QLabel {
                        background-color: #e74c3c;
                        color: white;
                        padding: 10px;
                        border-radius: 5px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                """)
                self.profit_label.setText(f"-${abs(total_profit):.2f}")
            else:
                self.profit_label.setStyleSheet("""
                    QLabel {
                        background-color: #95a5a6;
                        color: white;
                        padding: 10px;
                        border-radius: 5px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                """)
                self.profit_label.setText("$0.00")
            
            # Configurar color de margen
            if margin > 20:
                margin_color = "#27ae60"  # Verde para buen margen
            elif margin > 10:
                margin_color = "#f39c12"  # Naranja para margen medio
            elif margin > 0:
                margin_color = "#e67e22"  # Naranja oscuro para margen bajo
            else:
                margin_color = "#e74c3c"  # Rojo para margen negativo
            
            self.margin_label.setStyleSheet(f"""
                QLabel {{
                    background-color: {margin_color};
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                }}
            """)
            self.margin_label.setText(f"{margin:.1f}%")
            
        except ValueError:
            # Si hay error en la conversión, mostrar valores en cero
            self.investment_label.setText("$0.00")
            self.profit_label.setText("$0.00")
            self.margin_label.setText("0%")

    def save_product(self):
        try:
            # Validaciones
            if not self.name_entry.text().strip():
                QMessageBox.warning(self, '⚠️ Advertencia', 'El nombre del producto es requerido')
                return
            
            if not self.cost_entry.text().strip() or not self.price_entry.text().strip():
                QMessageBox.warning(self, '⚠️ Advertencia', 'Los precios son requeridos')
                return
            
            if not self.quantity_entry.text().strip():
                QMessageBox.warning(self, '⚠️ Advertencia', 'La cantidad es requerida')
                return

            cost = float(self.cost_entry.text())
            price = float(self.price_entry.text())
            quantity = int(self.quantity_entry.text())
            
            if cost < 0 or price < 0:
                QMessageBox.warning(self, '⚠️ Advertencia', 'Los precios no pueden ser negativos')
                return
                
            if quantity <= 0:
                QMessageBox.warning(self, '⚠️ Advertencia', 'La cantidad debe ser mayor a 0')
                return
                
            if price <= cost:
                reply = QMessageBox.question(self, '⚠️ Advertencia', 
                    'El precio de venta es menor o igual al costo. ¿Desea continuar?',
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.No:
                    return

            product = Product(
                name=self.name_entry.text().strip(),
                category=self.category_combo.currentText(),
                cost_price=cost,
                selling_price=price,
                description=self.desc_entry.text().strip(),
                quantity=quantity
            )
            self.db.add_product(product.to_dict())
            
            # Mensaje de éxito más atractivo
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('✅ Éxito')
            msg.setText('¡Producto agregado correctamente!')
            msg.setInformativeText(f'"{product.name}" ({quantity} unidades) ha sido añadido al inventario.')
            msg.exec()
            
            self.close()
        except ValueError as e:
            QMessageBox.critical(self, '❌ Error', f'Error en los datos ingresados:\n{str(e)}')

class InventoryWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('📋 Inventario de Productos')
        self.setGeometry(200, 200, 1100, 700)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QTableWidget {
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 8px;
                gridline-color: #eee;
                font-size: 12px;
                color: #2c3e50;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #eee;
                color: #2c3e50;
                background-color: white;
            }
            QTableWidget::item:alternate {
                background-color: #f8f9fa;
                color: #2c3e50;
            }
            QTableWidget::item:selected {
                background-color: #e3f2fd;
                color: #1976d2;
            }
            QTableWidget::item:hover {
                background-color: #f5f5f5;
                color: #2c3e50;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
                font-size: 13px;
            }
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border: none;
                padding: 12px 20px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #2c3e50;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Título
        title_label = QLabel('📋 Inventario de Productos')
        title_label.setFont(QFont('Arial', 20, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
        layout.addWidget(title_label)

        # Panel de estadísticas
        stats_frame = QFrame()
        stats_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        stats_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 2px solid #bdc3c7;
                padding: 10px;
            }
        """)
        stats_layout = QHBoxLayout(stats_frame)
        
        # Etiquetas de estadísticas
        self.total_products_label = QLabel("📦 Total Productos: 0")
        self.available_products_label = QLabel("✅ Disponibles: 0")
        self.sold_products_label = QLabel("💰 Vendidos: 0")
        self.total_profit_label = QLabel("💚 Ganancia Total: $0.00")
        
        # Aplicar estilos a las etiquetas
        for label in [self.total_products_label, self.available_products_label, 
                     self.sold_products_label, self.total_profit_label]:
            label.setStyleSheet("""
                QLabel {
                    font-size: 14px;
                    font-weight: bold;
                    color: #2c3e50;
                    padding: 8px;
                    border-radius: 5px;
                    background-color: #ecf0f1;
                }
            """)
        
        # Estilo especial para ganancia total
        self.total_profit_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: white;
                padding: 10px;
                border-radius: 5px;
                background-color: #27ae60;
            }
        """)
        
        stats_layout.addWidget(self.total_products_label)
        stats_layout.addWidget(self.available_products_label)
        stats_layout.addWidget(self.sold_products_label)
        stats_layout.addWidget(self.total_profit_label)
        
        layout.addWidget(stats_frame)

        # Tabla de inventario
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            'Nombre', 'Categoría', 'Costo', 'Precio', 'Stock', 'Vendido', 'Ganancia', 'Estado'
        ])
        
        # Configurar el header para que se ajuste automáticamente
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)  # Nombre
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # Categoría
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Costo
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Precio
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Stock
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Vendido
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)  # Ganancia
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)  # Estado
        
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        layout.addWidget(self.table)

        # Botones de acción
        buttons_layout = QHBoxLayout()
        
        # Botón para marcar como vendido
        sell_button = QPushButton('💰 Marcar como Vendido')
        sell_button.clicked.connect(self.mark_sold)
        sell_button.setMinimumHeight(45)
        
        # Botón para actualizar
        refresh_button = QPushButton('🔄 Actualizar')
        refresh_button.clicked.connect(self.load_products)
        refresh_button.setMinimumHeight(45)
        refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        
        buttons_layout.addWidget(sell_button)
        buttons_layout.addWidget(refresh_button)
        buttons_layout.addStretch()
        
        layout.addLayout(buttons_layout)

        self.load_products()

    def load_products(self):
        products = self.db.get_all_products()
        self.table.setRowCount(len(products))
        
        # Variables para estadísticas
        total_products = len(products)
        available_count = 0
        sold_count = 0
        total_profit = 0.0
        available_profit = 0.0
        
        for row, product in enumerate(products):
            # Manejar productos antiguos sin cantidad
            quantity = product.get('quantity', 1)
            sold_quantity = product.get('sold_quantity', 0)
            available_quantity = quantity - sold_quantity
            
            profit_per_unit = product['selling_price'] - product['cost_price']
            total_profit_for_item = profit_per_unit * sold_quantity
            
            # Determinar estado
            if available_quantity == 0:
                status = "🔴 Agotado"
                sold_count += 1
                total_profit += total_profit_for_item
            elif sold_quantity > 0:
                status = f"🟡 Parcial ({available_quantity} disponibles)"
                available_count += 1
                available_profit += profit_per_unit * available_quantity
                total_profit += total_profit_for_item
            else:
                status = "� Disponible"
                available_count += 1
                available_profit += profit_per_unit * available_quantity
            
            # Llenar la tabla
            name_item = QTableWidgetItem(product['name'])
            name_item.setForeground(QColor(44, 62, 80))
            self.table.setItem(row, 0, name_item)
            
            category_item = QTableWidgetItem(product['category'])
            category_item.setForeground(QColor(44, 62, 80))
            self.table.setItem(row, 1, category_item)
            
            cost_item = QTableWidgetItem(f"${product['cost_price']:.2f}")
            cost_item.setForeground(QColor(44, 62, 80))
            self.table.setItem(row, 2, cost_item)
            
            price_item = QTableWidgetItem(f"${product['selling_price']:.2f}")
            price_item.setForeground(QColor(44, 62, 80))
            self.table.setItem(row, 3, price_item)
            
            # Stock disponible
            stock_item = QTableWidgetItem(str(available_quantity))
            if available_quantity == 0:
                stock_item.setBackground(QColor(231, 76, 60, 40))
                stock_item.setForeground(QColor(183, 28, 28))
            elif available_quantity < quantity / 2:
                stock_item.setBackground(QColor(243, 156, 18, 40))
                stock_item.setForeground(QColor(175, 122, 197))
            else:
                stock_item.setForeground(QColor(44, 62, 80))
            stock_item.setFont(QFont('Arial', 11, QFont.Weight.Bold))
            self.table.setItem(row, 4, stock_item)
            
            # Cantidad vendida
            sold_item = QTableWidgetItem(str(sold_quantity))
            if sold_quantity > 0:
                sold_item.setBackground(QColor(39, 174, 96, 40))
                sold_item.setForeground(QColor(27, 94, 32))
            else:
                sold_item.setForeground(QColor(44, 62, 80))
            sold_item.setFont(QFont('Arial', 11, QFont.Weight.Bold))
            self.table.setItem(row, 5, sold_item)

            # Ganancia con color verde
            profit_item = QTableWidgetItem(f"${total_profit_for_item:.2f}")
            if total_profit_for_item > 0:
                profit_item.setBackground(QColor(39, 174, 96, 40))
                profit_item.setForeground(QColor(27, 94, 32))
            elif total_profit_for_item < 0:
                profit_item.setBackground(QColor(231, 76, 60, 40))
                profit_item.setForeground(QColor(183, 28, 28))
            else:
                profit_item.setForeground(QColor(44, 62, 80))
            profit_item.setFont(QFont('Arial', 11, QFont.Weight.Bold))
            self.table.setItem(row, 6, profit_item)
            
            # Estado con colores
            status_item = QTableWidgetItem(status)
            if available_quantity == 0:
                status_item.setBackground(QColor(255, 235, 238))
                status_item.setForeground(QColor(183, 28, 28))
            elif sold_quantity > 0:
                status_item.setBackground(QColor(255, 248, 225))
                status_item.setForeground(QColor(191, 144, 0))
            else:
                status_item.setBackground(QColor(232, 245, 233))
                status_item.setForeground(QColor(27, 94, 32))
            status_item.setFont(QFont('Arial', 10, QFont.Weight.Bold))
            self.table.setItem(row, 7, status_item)
        
        # Actualizar estadísticas
        self.total_products_label.setText(f"📦 Total Productos: {total_products}")
        self.available_products_label.setText(f"✅ Disponibles: {available_count}")
        self.sold_products_label.setText(f"💰 Vendidos: {sold_count}")
        
        # Mostrar ganancia total con diferente color según el valor
        total_profit_text = f"💚 Ganancia Total: ${total_profit:.2f}"
        if total_profit > 0:
            self.total_profit_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    background-color: #27ae60;
                }
            """)
        elif total_profit < 0:
            self.total_profit_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    background-color: #e74c3c;
                }
            """)
            total_profit_text = f"💸 Pérdida Total: ${abs(total_profit):.2f}"
        else:
            self.total_profit_label.setStyleSheet("""
                QLabel {
                    font-size: 16px;
                    font-weight: bold;
                    color: white;
                    padding: 10px;
                    border-radius: 5px;
                    background-color: #95a5a6;
                }
            """)
        
        self.total_profit_label.setText(total_profit_text)

    def mark_sold(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, '⚠️ Advertencia', 
                'Por favor, seleccione un producto de la tabla')
            return

        product_name = self.table.item(current_row, 0).text()
        available_stock = int(self.table.item(current_row, 4).text())
        
        # Verificar si hay stock disponible
        if available_stock == 0:
            QMessageBox.information(self, 'ℹ️ Sin Stock', 
                f'El producto "{product_name}" está agotado.')
            return
        
        # Abrir ventana de venta
        self.sell_window = SellProductWindow(self.db, product_name, available_stock, self)
        self.sell_window.show()

class SellProductWindow(QMainWindow):
    def __init__(self, db, product_name, available_stock, parent_window):
        super().__init__()
        self.db = db
        self.product_name = product_name
        self.available_stock = available_stock
        self.parent_window = parent_window
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f'💰 Vender - {self.product_name}')
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QGroupBox {
                font-size: 14px;
                font-weight: bold;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                margin: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 10px 0 10px;
            }
            QLineEdit, QSpinBox {
                padding: 8px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 12px;
            }
            QLineEdit:focus, QSpinBox:focus {
                border-color: #3498db;
            }
            QPushButton {
                color: white;
                border: none;
                padding: 12px;
                border-radius: 6px;
                font-size: 14px;
                font-weight: bold;
                margin: 5px;
            }
            QPushButton:hover {
                opacity: 0.8;
            }
        """)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Título
        title_label = QLabel(f'Vender: {self.product_name}')
        title_label.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title_label)

        # Información del stock
        info_group = QGroupBox("Información de Stock")
        info_layout = QFormLayout(info_group)
        
        available_label = QLabel(f"{self.available_stock} unidades")
        available_label.setStyleSheet("""
            QLabel {
                background-color: #27ae60;
                color: white;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
        """)
        info_layout.addRow("📦 Stock Disponible:", available_label)
        
        layout.addWidget(info_group)

        # Cantidad a vender
        sell_group = QGroupBox("Cantidad a Vender")
        sell_layout = QFormLayout(sell_group)
        
        self.quantity_spinbox = QSpinBox()
        self.quantity_spinbox.setMinimum(1)
        self.quantity_spinbox.setMaximum(self.available_stock)
        self.quantity_spinbox.setValue(1)
        self.quantity_spinbox.setMinimumHeight(40)
        sell_layout.addRow("🛒 Cantidad:", self.quantity_spinbox)
        
        layout.addWidget(sell_group)

        # Botones
        buttons_layout = QHBoxLayout()
        
        # Botón confirmar venta
        sell_button = QPushButton('✅ Confirmar Venta')
        sell_button.clicked.connect(self.confirm_sale)
        sell_button.setMinimumHeight(45)
        sell_button.setStyleSheet("background-color: #27ae60;")
        
        # Botón cancelar
        cancel_button = QPushButton('❌ Cancelar')
        cancel_button.clicked.connect(self.close)
        cancel_button.setMinimumHeight(45)
        cancel_button.setStyleSheet("background-color: #e74c3c;")
        
        buttons_layout.addWidget(sell_button)
        buttons_layout.addWidget(cancel_button)
        
        layout.addLayout(buttons_layout)
        
        # Espaciador
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

    def confirm_sale(self):
        quantity_to_sell = self.quantity_spinbox.value()
        
        # Confirmar la venta
        reply = QMessageBox.question(self, '💰 Confirmar Venta', 
            f'¿Confirma la venta de {quantity_to_sell} unidad(es) de "{self.product_name}"?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes)
        
        if reply == QMessageBox.StandardButton.Yes:
            # Buscar el producto y actualizar la cantidad vendida
            products = self.db.get_all_products()
            for product in products:
                if product['name'] == self.product_name:
                    # Obtener cantidades actuales
                    current_sold = product.get('sold_quantity', 0)
                    total_quantity = product.get('quantity', 1)
                    
                    # Calcular nueva cantidad vendida
                    new_sold_quantity = current_sold + quantity_to_sell
                    
                    # Actualizar el producto
                    updates = {
                        'sold_quantity': new_sold_quantity,
                        'sold': new_sold_quantity >= total_quantity
                    }
                    
                    self.db.update_product(product['_id'], updates)
                    break
            
            # Mensaje de confirmación
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('✅ Venta Registrada')
            msg.setText('¡Venta completada exitosamente!')
            msg.setInformativeText(f'{quantity_to_sell} unidad(es) de "{self.product_name}" vendida(s).')
            msg.exec()
            
            # Actualizar la ventana padre y cerrar
            self.parent_window.load_products()
            self.close()