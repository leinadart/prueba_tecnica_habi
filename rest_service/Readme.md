# Servicio rest para obtención de propiedades

API REST en arquitectura limpia para obtener información de las propiedades según filtros.

## 🚀 Quick Start

```powershell
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Ejecución
python main.py

# 2. Abrir en el navegador
http://localhost:8000/health

# 3. Pruebas
pytest --cov=app
```

## 📡 Endpoints

### GET /get-properties?city={city}&year={year}&state={state}

Devuelve listado de inmuebles con los filtros seleccionados

**Parámetros:**
- `city={city}`
- `year={year}`
- `state={state}` Estados válidos: pre_venta, en_venta o vendido.

**Respuesta exitosa (200):**

**Body:**
```json
[
  {
    "address": "",
    "city": "",
    "state": "",
    "price": "",
    "description": ""
  },
  {
    ...
  }
]
```
### GET /health
Devuelve estado del servicio

**Respuesta exitosa (200):**
**Body:**
```json
    {
    "details": "Service online"
    }
```
