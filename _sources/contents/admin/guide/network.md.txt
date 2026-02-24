# Networks

The local network of the UIBCDF is 192.168.0.255
According with this there is an ip range definition for the cluster 1-100.

## Interactive network

The cluster occupies the range 1-100 in the local interactive network in the lab 192.168.0.255.
In the following table the ips are detailed.

| IP or range | Hostname           |
|        :--- | :---               |
|         100 | ixtlilton (master) |
|           1 | node01             |
|           2 | node02             |
|           3 | node03             |
|           4 | node04             |

Despite of being a peripherical, given that the cluster has no storage server
nodes, it hosts now the volume /ColdStorageRoom with the partitions "archive" and "backups".

| IP or range | Hostname           |
|        :--- | :---               |
|         203 | NAS                |


## NFS network

An additional network is set to carry the flow regarding the NFS imported volumes: 172.17.255.255.

| IP or range | Hostname           |
|        :--- | :---               |
|     253.253 | ixtlilton (master) |
|         1.1 | node01             |
|         1.2 | node02             |
|         1.3 | node03             |
|         1.4 | node04             |



