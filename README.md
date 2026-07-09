# ODOO 19

Este repositorio contiene la configuración necesaria para ejecutar una instancia de Odoo community utilizando contenedores de Docker

### Caracteristicas

- Entorno de desarrollo aislado
- Configuración persistente a través de un archivo odoo.conf personalizado
- Estructura organizada para cargar módulos en la carpeta addons

### Estructura del proyecto

```
.
├── compose.yml
├── config/
│   └── odoo.conf
├── addons/
│   └── (mis módulos personalizados)
├── Dockerfile
└── README.md
```

---

## Módulos

| Módulo | Descripción | Estado |
|---|---|---|

*(Esta tabla se irá actualizando conforme avance)*

---

## Instalación y Configuración

1. **Clonar el repositorio:**
    ```bash
    git clone <https://github.com/GSaori/Odoo.git>
    cd Odoo
2. **Configurar variables:**
    Revisar archivo config/odoo.conf y ajustar los parametros necesarios.

3. **Iniciar servicios:**
    Ejecutar el siguiente comando en la raíz del proyecto para descargar las imágenes y levantar los contenedores:
    ```bash
    docker compose up -d
4. **Verificar estado**
    ```bash
    docker compose ps