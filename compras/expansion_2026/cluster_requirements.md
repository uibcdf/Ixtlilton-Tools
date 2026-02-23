
# Cluster GPU 2 nodos — Requisitos funcionales y técnicos

## 1. Objetivo general

Diseñar e implementar un pequeño cluster de cómputo en rack compuesto por **2 nodos GPU de 4 GPUs cada uno**, orientado a:

- Inferencia y entrenamiento ligero de LLMs
- Simulaciones de dinámica molecular (OpenMM, GROMACS)
- Procesamiento de datasets científicos
- Uso multiusuario con Slurm

El cluster debe ser:

- Montable manualmente
- Estable en entorno hospitalario con variaciones eléctricas
- Escalable sin rediseñar arquitectura

---

## 2. Restricciones físicas

- Rack existente tipo short-depth
- Profundidad útil aproximada: ~59.5 cm
- No se modificará el rack
- Refrigeración ambiental: 18–19 °C con minisplit
- Flujo de aire frontal → trasero

---

## 3. Arquitectura general

### Número de nodos
- 2 nodos independientes
- 4 GPUs por nodo

### Uso principal
- GPU-centric (95% del tiempo)
- CPU principalmente para:
  - I/O
  - orquestación
  - dataloaders

---

## 4. Requisitos por nodo

### CPU
- Aproximadamente 4 cores por GPU
- Objetivo: 16 cores
- Plataforma servidor (EPYC o equivalente)

### Memoria RAM
- Nodo A: 128 GB ECC
- Nodo B: 64 GB ECC (expandible a 128 GB)

### Almacenamiento
- SSD SATA para sistema
- NVMe para scratch local
- Storage persistente externo por red

### GPU
- 4 GPUs doble slot por nodo
- Compatibilidad con GPUs actuales:
  - 1080 Ti
  - 2080 Ti
  - 5070 Ti
  - 5080

---

## 5. Red

Switch actual:
- TP-Link TL-SG1024D (Gigabit)

Configuración:
- 1 red administración / Slurm
- 1 red datos (misma velocidad actualmente)

No se requiere NIC 10Gb actualmente.

---

## 6. Energía y resiliencia

### PSU
- 1 PSU por nodo
- 1600–2000W
- Alta calidad

### UPS
- UPS online/doble conversión
- Capacidad para ambos nodos
- Permitir apagado limpio
- Tolerar transferencias a planta diésel

---

## 7. Requisitos térmicos

- Chasis 4U short-depth
- Ventiladores de alta presión estática
- Flujo frontal → trasero
- Capacidad para GPUs de alto TDP

---

## 8. Expansiones futuras previstas

El diseño debe permitir sin rediseño:

### GPUs de 80 GB
- Espacio físico
- Potencia suficiente
- PCIe lanes suficientes

### Red 10Gb
- Posibilidad de añadir NIC 10Gb en el futuro

### RAM
- Nodo B ampliable a 128 GB

### Energía
- Posibilidad futura de PSU redundante si chasis lo permite

### Almacenamiento
- Segundo NVMe opcional

---

## 9. Filosofía de diseño

- Priorizar estabilidad sobre rendimiento extremo
- Minimizar cuellos de botella GPU
- Evitar dependencias de hardware propietario
- Mantener mantenimiento simple

---

## 10. Riesgos identificados

- Limitación de red a 1 Gb
- Limitación térmica si airflow es insuficiente
- Picos de potencia con GPUs futuras

Mitigación:
- NVMe local
- PSU sobredimensionada
- UPS online

---

## 11. Resultado esperado

Cluster capaz de:

- Ejecutar cargas GPU intensivas de forma continua
- Soportar crecimiento en GPUs y memoria
- Operar de forma estable en entorno eléctrico no ideal
- Servir como infraestructura base para investigación
