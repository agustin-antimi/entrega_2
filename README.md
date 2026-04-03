Alumno: Agustin Antimi

Legajo: 17816/1

# entrega_2
Este repositrio consta de la entrega 2 de la practica.

## Instalación de dependencias

Para que este proyecto funcione correctamente, es necesario instalar las librerías indicadas en el archivo `requirements.txt`. Siguiendo estos pasos:

### 1. Crear y activar un entorno virtual (Recomendado)

Es una buena práctica aislar las dependencias del proyecto utilizando un entorno virtual.

**windows**

```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual en Windows
.\env\Scripts\activate
```

**Linux**

```bash
# Crear el entorno virtual
python -m venv env

# Activar el entorno virtual en macOS o Linux
source env/bin/activate
```

### 2. Instalar las dependecias

Nos aseguramos de estar posicionados en la carpeta correcta donde tenemos acceso al file de `requiremnts.txt` y ejecutamos.

```bash
# Instalar todas las dependencias
pip install -r requirements.txt
```

## Ejecución del proyecto (Jupyter Notebooks)

Este proyecto utiliza notebooks de Python (archivos con extensión `.ipynb`) para organizar y ejecutar el código de manera interactiva. Para correr el programa, hay difrentes opciones:

### Opción 1: Desde el IDE

Si utilizas VS Code como tu editor principal, la integración es muy sencilla:

1. Asegúrate de tener instaladas las extensiones oficiales de **Python** y **Jupyter** en tu editor.
2. Abre el archivo `.ipynb` desde el explorador de archivos de VS Code.
3. En la esquina superior derecha del notebook, haz clic en **Select Kernel** (Seleccionar Kernel) o en la versión de Python que aparezca.
4. Elige la opción que corresponde al entorno virtual de este proyecto `.venv`.
5. Puedes ejecutar todo el código de una vez con el botón **Run All** (Ejecutar todo) en el menú superior, o correr cada celda de forma individual presionando `Shift + Enter`.

### Opción 2: Desde la terminal (Jupyter Notebook clásico)

Para usar la interfaz web clásica desde tu navegador:

1. Abre tu terminal y asegúrate de tener el entorno virtual activado.
2. Ejecuta el siguiente comando:

```bash
# Iniciar el servidor local de Jupyter
jupyter notebook
```