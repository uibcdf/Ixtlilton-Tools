# Cluster GPU HPC – Requerimientos Finales

## Objetivo
Construir un cluster de 2 nodos GPU (4 GPUs por nodo) optimizado para:

- LLM inference y experimentación
- Dinámica molecular (OpenMM, GROMACS)
- Procesamiento científico general

## Restricciones

- Presupuesto aproximado: 200,000 MXN
- Rack existente profundidad ~60 cm (puede sobresalir el chasis)
- Montaje manual (DIY)
- Compra única (no se prevé adquirir piezas posteriormente)

## Arquitectura General

- 2 nodos GPU independientes
- Plataforma AMD EPYC generación Rome/Milan
- 4 GPUs por nodo
- UPS compartida >= 5 kW, 6-8 kVA (online doble conversión) con entrada NEMA L5-30P o similar (30 A)
- Red Gigabit existente (preparado para upgrade a 10 GbE)

## Plataforma Base

### Motherboard principal
- Supermicro H12SSL-i

### Alternativas compatibles
- Gigabyte MZ32-AR0
- ASRock Rack ROMED8

### CPU
- AMD EPYC serie 7002/7003 (perfil coste-beneficio)

### Refrigeración CPU
- 1 × Dynatron A26 SP3 Active CPU Cooler
  (Alternativa: Supermicro SNK-P0064AP4)

### RAM
- Nodo A: 8x16 GB ECC RDIMM
- Nodo B: 8x16 GB ECC RDIMM

## Almacenamiento

- 1 × NVMe PCIe 4.0 1 TB por nodo
- 1 × SSD SATA 480 GB por nodo
- cables SATA adicionales

## Chasis

- 1 × Chasis 4U GPU E-ATX tipo Rosewill (≥8 slots PCIe)
- Mínimo 8 slots PCIe físicos
- Perfil económico-robusto tipo Rosewill
- Alternativa premium: chasis GPU Supermicro si el presupuesto lo permite
- rails o soportes universales

## Energía

- UPS online para ambos nodos
- 1 × PSU ATX 1600–2000 W 80+ Platinum por nodo
- cables PCIe adicionales
- adaptadores 12V-2×6
- cable EPS adicional

### Refrigeración general
- ventiladores incluidos en el chasis
- 2 ventiladores adicionales alta presión
- hub PWM

### Red
- 2 cables Cat6 por nodo

### Miscelánea
- pasta térmica
- 2 kit universal M.2 mounting kit por nodo (Tornillos M2 × 3 mm, standoffs, sepadores, ...)
- bridas de cableado
- speaker POST
- adaptador de vídeo diagnóstico
- 2 brackets 2.5" por nodo

## Infraestructura común

- 1 × UPS online ≥3 kVA
- 1 × PDU con entrada L5-30P o IEC C20
- cables IEC adicionales
- 8 risers PCIe x16
- 2 cables SATA datos por nodo
- 1 cable de alimentación SATA con al menos 2 conectores
- cables red extra
- 1 SSD de repuesto opcional
- Salidas IEC C19 en PDU
- PDU con salidas IEC C19
- Cables de alimentación C19–C20 (uno por nodo + repuestos)
- 2 cables Ethernet adicionales por nodo

## Expansiones Futuras

- GPUs de mayor VRAM (40–80 GB)
- NIC 10/25 GbE
- expansión RAM ≥512 GB

Si el presupuesto lo permite:

- sustituir chasis por chasis GPU Supermicro 4U

## Filosofía de Diseño

- Priorizar estabilidad sobre hardware bleeding-edge
- Maximizar rendimiento por peso invertido
- Mantener compatibilidad y capacidad de mantenimiento
