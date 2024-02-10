# Pokemon Dataset Analysis
Solución a items relacionados con el Dataset de Pokémon para analisis estadístico.

## Pasos para ejecutar el proyecto

### Crear entorno virtual (venv)
Ejecutamos el comando `py -m venv ./.venv` o `python -m venv ./.venv` para inicializar el entorno virtual de ejecución para el proyecto.

### Activar el entorno virtual
Antes de ejecutar, probar o modificar el proyecto es importante activar el entorno virtual para trabajar el proyecto de manera local, para ello ejecutamos el script de activacion del entorno virtual dentro de la consola o PowerShell:
- **PowerShell:** `.\.venv\Scripts\activate`
- **Command Prompt (CMD):** Primero accedemos al directorio con `cd .\.venv\Scripts\` y luego ejecutamos la utilidad `activate` (*activate.bat*)

### Instalación de paquetes
Instalamos los paquetes listados en el archivo de requerimientos *requirements_lock.txt* para replicar el entorno funcional del proyecto. Ejecutamos el comando: 
`pip install -r .\requirements_lock.txt`

### Ejecutando el notebook
#### Visual Studio Code: 
1. Seleccionar el entorno virtual *.venv* entre los entornos de python disponibles en la selección del Kernel del notebook como entorno de ejecución para el proyecto. Tambien podemos ejecutar el shortcut de teclado `Control+Shift+P` y escribir *Python: Select Interpreter* para seleccionar como interprete la instalación de Python en el entorno virtual (*.venv*)
2. Abrir/seleccionar el archivo *03-Pokemon Dataset Analysis.ipynb*.
3. Ejecutar todas las celdas del notebook *03-Pokemon Dataset Analysis.ipynb* y comprobar los resultados o ejecutarlas una a una.

#### Jupyter notebook:
1. Ejecutar el comando `jupyter notebook` (Se instala a partir del archivo de requerimientos) para inicializar el servidor de Jupyter utilizando como Kernel el entorno virtual actual.
2. Abrir/seleccionar el archivo *03-Pokemon Dataset Analysis.ipynb*.
3. Ejecutar todas las celdas del notebook *03-Pokemon Dataset Analysis.ipynb* y comprobar los resultados o ejecutarlas una a una.

### Cleaning up
Una vez finalizado el trabajo con el proyecto, el entorno virtual se puede desactivar ejecutando la utilidad/comando: `deactivate` (*deactivate.bat*) o simplemente cerrando la consola o shell donde se activo el entorno virtual.

Para volver a activarlo se debe volver a ejecutar el script de activación.

En caso que no se quiera trabajar con el entorno virtual omitir todos los pasos anteriores excepto el paso de instalación de los paquetes necesarios para la ejecución del proyecto con `pip install -r .\requirements_lock.txt` (`py|python -m pip install -r .\requirements_lock.txt` si no se encuentra `pip` disponible de manera global). 

De esta manera estariamos ejecutando el proyecto utilizando la instalación global de python en lugar del entorno virtual dedicado al proyecto.