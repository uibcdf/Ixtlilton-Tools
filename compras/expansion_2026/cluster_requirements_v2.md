# Cluster GPU HPC – Requerimientos Finales

## Objetivo
Construir un cluster de 2 nodos GPU (4 GPUs por nodo) optimizado para:

- LLM inference y experimentación
- Dinámica molecular (OpenMM, GROMACS)
- Procesamiento científico general
- workloads científicos generales GPU-centric

El diseño prioriza estabilidad, coste-beneficio y capacidad de expansión futura.

## Restricciones

- Presupuesto aproximado: 200,000 MXN
- Rack existente profundidad ~60 cm (puede sobresalir el chasis) porque el rack no tiene puerta trasera y se puede
  distanciar del muro.
- Montaje manual (DIY)
- Compra única (no se prevé adquirir piezas posteriormente)
- Entorno con cortes eléctricos periódicos (uso obligatorio de UPS)

## Supuestos de diseño

- Cluster principalmente GPU-centric
- CPU como soporte de I/O, scheduling y pre/post-processing
- Prioridad en fiabilidad frente a hardware bleeding-edge
- Horizonte de uso esperado: 3–5 años
- Posible upgrade futuro a GPUs de mayor VRAM (80 Gb)

## Arquitectura General

- 2 nodos GPU independientes
- Plataforma AMD EPYC generación Rome/Milan (PCIe 4.0)
- 4 GPUs por nodo
- UPS compartida para ambos nodos
- Red Gigabit existente (preparado para upgrade a 10 GbE)

## Inventario GPU actual

Disponibles o previstos:

- RTX 5090 (1 unidad)
- RTX 5070 Ti (2 unidades)
- RTX 5070 (3 unidades)
- RTX 2080 Ti (8 unidades)
- RTX 1080 Ti (8 unidades)

La asignación por nodo se realizará según consumo y perfiles de carga.

Supuesto posible por nodo:

- Nodo A: 1x RTX 5090 + 2x RTX 5070 Ti + 1x RTX 5070 (enfocado en LLM y cargas más pesadas)
- Nodo B: 2x RTX 5070 + 2x RTX 2080 (enfocado en cargas mixtas y experimentación general y dinámica molecular)

## Plataforma Base

### Motherboard principal
- Supermicro H12SSL-i

### Alternativas compatibles
- Gigabyte MZ32-AR0
- ASRock Rack ROMED8

### CPU
- AMD EPYC serie 7002/7003 (perfil coste-beneficio)

### RAM
- Nodo A: 128 GB ECC RDIMM
- Nodo B: 128 GB ECC RDIMM (expandible)

## Almacenamiento

- NVMe PCIe 4.0 para scratch y datasets
- SSD SATA para sistema operativo

## Chasis

- Chasis 4U GPU E-ATX
- Mínimo 8 slots PCIe físicos
- Perfil económico-robusto tipo Rosewill
- airflow frontal-trasero
- de expansion slots reales (8 o más).
- Si permite full-height y el tipo de retención.
- Si soporta 4 GPUs de ancho real (no solo “4 PCIe x16” en marketing).

- Alternativa premium: chasis GPU Supermicro si el presupuesto lo permite

## Energía

- PSU ATX 1600–2000 W por nodo
- UPS online para ambos nodos
- entorno hospitalario con cortes eléctricos periódicos
- PSU(s) ATX 3.x que incluyan cables nativos 12V-2x6
- si hay que comprar adaptadores que sean marca OEM / marca GPU / marca PSU.

## 10. Condiciones térmicas

- sala dedicada refrigerada (≈18–19 °C)
- flujo de aire frontal-trasero en rack
- diseño compatible con GPUs de alto TDP

## Expansiones Futuras

- GPUs de mayor VRAM (40–80 GB)
- NIC 10/25 GbE
- expansión RAM ≥512 GB
- posible PSU redundante en revisiones futuras

## Filosofía de Diseño

- Priorizar estabilidad sobre hardware bleeding-edge
- Maximizar rendimiento por peso invertido
- Mantener compatibilidad, stabilidad y capacidad de mantenimiento
- Evitar dependencias de hardware específico
- mantener facilidad de mantenimiento y reemplazo

