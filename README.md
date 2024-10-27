# Unidash
Unidash es un panel de control unificado para generar scripts de FEHM basados en datos introducidos por el usario.

## Descripción del Proyecto
Unidash es una aplicación web diseñada para proporcionar un panel de control unificado para gestionar diversas tareas y datos de FEHM. Permite a los usuarios crear y gestionar archivos de escenarios, y proporciona una interfaz simple para interactuar con la aplicación.

## Requisitos Previos
Hay dos maneras sencillas para para instalar las dependencias de la aplicación.
- Usando Conda (Linux o Windows)
- Usando Python y pip

### Usando Conda (Linux o Windows)
- Conda (miniconda o anaconda) instalado 
- Python 3.8
- Git

### Usando Python y pip
Usando Python sin Conda hay que instalar manualmente algunas dependencias.
- flask
- flask_sqlalchemy
- sqlite
- sphinx

## Instalación
1. Extrae el archivo zip.Lo importante es la localización de la carpeta `Unidash` en tu sistema. De la ruta depende la ejecución de los scripts de FEHM.

   ```plaintext
   root
   ├── Unidash
   └── FEHM
   ```

2. Crea y activa el entorno conda:
   ```bash
   conda create --name unidash_env python=3.8 -y
   ```

3. Dar permisos de ejecución a los archivos de la carpeta `scripts`:
   ```bash
   chmod +x scripts/*
   ```


## Ejecución de la Aplicación
1. Asegúrate de que el entorno conda esté activado:
   ```bash
   conda activate unidash_env
   ```

2. Ejecuta la aplicación:
   ```bash
   python run.py
   ```

## Generar Documentación con Sphinx

Hay una configuración de Sphinx en la carpeta `docs` para generar la documentación de la aplicación. Para generar la documentación, sigue los pasos habituales para generar la documentación con Sphinx.
