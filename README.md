# U4S8 — Coronado Córdova René Alejandro

**Alumno:** René Alejandro Coronado Córdova
**Grupo:** DSM 4-1
**Carrera:** TSU en Desarrollo de Software Multiplataforma
**Universidad:** Universidad Tecnológica de Hermosillo

## Demo en vivo (producción)

https://u4s8-coronado-cordova-rene-alejandro.onrender.com

Nota: URL prevista para el nuevo servicio. Se confirmará después del despliegue en Render.

## Qué hace este proyecto

Aplicación web desarrollada con Django que permite a los usuarios registrarse, iniciar sesión, cerrar sesión y administrar sus servicios mediante operaciones CRUD: crear, consultar, editar y eliminar registros.

El sistema incorpora búsqueda de servicios por título, sin distinguir mayúsculas y minúsculas, y paginación de cinco registros por página. La búsqueda se conserva al navegar entre páginas.

Los servicios se almacenan en una base de datos MySQL alojada en Aiven. El sistema utiliza autenticación de Django y consultas filtradas por el usuario autenticado para restringir el acceso a los registros correspondientes.

La Semana 8 corresponde al cierre del proyecto: auditoría, respaldo de datos, documentación, despliegue definitivo y publicación de la versión v1.0, sin incorporar nuevas funcionalidades.

## Stack técnico

- Python y Django.
- MySQL alojado en Aiven.
- HTML y Tailwind CSS.
- Git y GitHub.
- Render para el despliegue web.
- Gunicorn y WhiteNoise.

## Cómo se prueba el aislamiento por usuario

La aplicación está diseñada para que cada usuario consulte y administre únicamente sus propios servicios.

La prueba indicada en la Semana 6 consiste en:

1. Registrar dos usuarios diferentes.
2. Iniciar sesión con la primera cuenta.
3. Crear un servicio.
4. Cerrar sesión e ingresar con la segunda cuenta.
5. Comprobar que el servicio de la primera cuenta no aparece en el listado de la segunda.
6. Intentar acceder a la edición de un servicio ajeno y verificar que la aplicación responde con un error 404.

Estado: prueba pendiente de confirmar en el servicio final de producción.

## Historial de unidades

- **Unidad 1:** portafolio estático con HTML5 y Tailwind CSS.
- **Unidad 2:** modelo Servicio, migraciones a MySQL en Aiven y despliegue dinámico en Render.
- **Unidad 3:** CRUD completo con ModelForms, autenticación y sesiones.
- **Unidad 4:** búsqueda, paginación, revisión de interfaz y defensa final.

## Seguridad y respaldo

La configuración privada se administra mediante variables de entorno. El archivo `.env` no debe publicarse en GitHub.

El respaldo final `backup_final.json` se generó fuera del repositorio para evitar publicar información de los usuarios.

La configuración de producción y el funcionamiento del sistema se verificarán en Render antes de publicar la versión definitiva.