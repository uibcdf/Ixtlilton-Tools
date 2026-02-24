# Cluster Runbook

## Purpose
Operational reference for 2-node GPU cluster.

## Startup
1. Power UPS
2. Power node
3. Check IPMI
4. Boot OS

## Monitoring
- nvidia-smi
- sensors
- uptime

## Shutdown
1. Stop workloads
2. Shutdown OS
3. Power off nodes
4. Power off UPS (if needed)
