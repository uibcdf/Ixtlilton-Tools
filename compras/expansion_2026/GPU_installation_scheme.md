# GPU Installation Scheme – 2‑Node Cluster

## Node A (Heavy)
GPUs:
- RTX 5090 FE (direct slot)
- RTX 5070 Ti (riser)
- RTX 5070 Ti (slot)
- RTX 5070 FE (riser)

Layout strategy:
- Highest TDP GPU in primary airflow path
- Leave air gap between GPUs when possible
- Use stabilizers on riser‑mounted cards

## Node B (Mixed)
GPUs:
- RTX 5070 (slot)
- RTX 2080 Ti (riser)
- RTX 2080 Ti (slot)
- RTX 5070 (riser)

Layout strategy:
- Separate older GPUs to distribute heat
- Balance airflow across front intake

## General Rules
- Dedicated PSU cable per GPU
- Avoid cable tension
- Verify detection in BIOS/IPMI
- Monitor temps on first boot
