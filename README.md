# Pre-Entrega Automation Testing - Franco Tomas Bondioni

## Propósito del proyecto
Este proyecto aplica los conocimientos de automatización de flujos básicos de navegación web utilizando Selenium WebDriver y Python. Automatiza las pruebas de inicio de sesión, verificación del catálogo y la interacción con el carrito de compras en el sitio de pruebas saucedemo.com.

## Tecnologías utilizadas
* Python 
* Pytest 
* Selenium WebDriver 
* Git y GitHub 

## Instrucciones de instalación
1. Clonar este repositorio localmente
2. Crear un entorno virtual en la terminal: `python -m venv venv`
3. Activar el entorno virtual: `.\venv\Scripts\activate` 
4. Instalar las dependencias necesarias: `pip install pytest selenium pytest-html`

## Cómo ejecutar las pruebas
Para ejecutar los tests de forma independiente y generar un reporte en HTML con los resultados, ejecuta el siguiente comando en la raíz del proyecto

## Terminal
python -m pytest tests/test_saucedemo.py -v --html=reports/reporte.html