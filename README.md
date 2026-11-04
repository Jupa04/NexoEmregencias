# Nexo Emergencias

Mockup de la consola de coordinación de Nexo Emergencias, el proyecto de Base de Datos I. Muestra las zonas afectadas por índice de priorización, la ocupación de albergues, los despachos en curso, el inventario y las cuadrillas, con los datos de prueba de los scripts de Oracle.

Es una maqueta visual: los botones y formularios responden, pero no guardan nada.

## Estructura

```
app.py                 Aplicación de Streamlit que muestra el mockup
mockup/index.html      Diseño del mockup (HTML, CSS y JavaScript)
mockup/datos.json      Datos de prueba que se insertan en el mockup
requirements.txt       Dependencias
.streamlit/config.toml Colores de la app
```

## Correr en local

```bash
pip install -r requirements.txt
streamlit run app.py
```

Se abre en http://localhost:8501.

## Desplegar en Streamlit Community Cloud

1. Sube esta carpeta a un repositorio de GitHub, con `app.py` en la raíz.
2. Entra a https://share.streamlit.io con tu cuenta de GitHub.
3. Toca **Create app** y elige **Deploy a public app from GitHub**.
4. Escoge el repositorio, la rama `main` y el archivo `app.py`.
5. Toca **Deploy**. En uno o dos minutos queda publicada en una dirección `*.streamlit.app`.

Cada vez que hagas *push* a la rama `main`, la app se actualiza sola.

## Cambiar los datos

Edita `mockup/datos.json` y haz *push*. No hace falta tocar el HTML.
