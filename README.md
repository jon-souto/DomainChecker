# DomainChecker
Script en Python que busca posibles dominios homográficos y parecidos para un dominio dado, comprobando si están activos.
# Prerrequisitos
Instalar los módulos dnspython, tabulate y tqdm
```bash
pip install dnspython
pip install tabulate
pip install tqdm
```
# Ejemplo de uso
Ejecuta el script
```bash
python DomainChecker.py
```
Introduce el dominio
```bash
Ingrese el dominio a comprobar: google.es
```
Resultado
```bash
+-----------+----------+-----------------+
| Dominio   | Estado   | Dirección IP    |
+===========+==========+=================+
| boogle.es | Activo   | 185.53.177.54   |
+-----------+----------+-----------------+
| coogle.es | Activo   | 185.53.177.73   |
+-----------+----------+-----------------+
| doogle.es | Activo   | 213.186.33.5    |
+-----------+----------+-----------------+
| foogle.es | Activo   | 185.53.177.51   |
+-----------+----------+-----------------+
| hoogle.es | Activo   | 213.186.33.5    |
+-----------+----------+-----------------+
| koogle.es | Activo   | 213.171.209.5   |
+-----------+----------+-----------------+
| soogle.es | Activo   | 185.53.177.20   |
+-----------+----------+-----------------+
| voogle.es | Activo   | 81.169.145.164  |
+-----------+----------+-----------------+
| woogle.es | Activo   | 185.86.210.114  |
+-----------+----------+-----------------+
| xoogle.es | Activo   | 217.76.156.252  |
+-----------+----------+-----------------+
| zoogle.es | Activo   | 51.255.26.63    |
+-----------+----------+-----------------+
| geogle.es | Activo   | 185.53.178.53   |
+-----------+----------+-----------------+
| ggogle.es | Activo   | 185.53.178.50   |
+-----------+----------+-----------------+
| giogle.es | Activo   | 64.190.63.111   |
+-----------+----------+-----------------+
| glogle.es | Activo   | 103.224.182.250 |
+-----------+----------+-----------------+
| gpogle.es | Activo   | 185.53.177.51   |
+-----------+----------+-----------------+
| goggle.es | Activo   | 185.53.178.50   |
+-----------+----------+-----------------+
| goigle.es | Activo   | 199.59.243.223  |
+-----------+----------+-----------------+
| golgle.es | Activo   | 185.53.177.73   |
+-----------+----------+-----------------+
| gopgle.es | Activo   | 185.53.178.74   |
+-----------+----------+-----------------+
| gougle.es | Activo   | 185.53.177.71   |
+-----------+----------+-----------------+
| gooble.es | Activo   | 185.53.177.50   |
+-----------+----------+-----------------+
| goofle.es | Activo   | 213.186.33.5    |
+-----------+----------+-----------------+
| goohle.es | Activo   | 185.53.177.50   |
+-----------+----------+-----------------+
| gooqle.es | Activo   | 164.138.210.36  |
+-----------+----------+-----------------+
| goovle.es | Activo   | 185.53.178.74   |
+-----------+----------+-----------------+
| googie.es | Activo   | 81.88.53.67     |
+-----------+----------+-----------------+
| googje.es | Activo   | 81.88.53.67     |
+-----------+----------+-----------------+
| googke.es | Activo   | 185.53.177.53   |
+-----------+----------+-----------------+
| googoe.es | Activo   | 185.53.178.51   |
+-----------+----------+-----------------+
| googla.es | Activo   | 81.169.145.70   |
+-----------+----------+-----------------+
| googld.es | Activo   | 185.53.177.11   |
+-----------+----------+-----------------+
| googli.es | Activo   | 81.169.145.70   |
+-----------+----------+-----------------+
| googlr.es | Activo   | 185.53.177.53   |
+-----------+----------+-----------------+
| googls.es | Activo   | 185.53.177.53   |
+-----------+----------+-----------------+
| googlw.es | Activo   | 185.53.177.52   |
+-----------+----------+-----------------+
| google.as | Activo   | 172.217.168.163 |
+-----------+----------+-----------------+
| google.bs | Activo   | 142.250.200.99  |
+-----------+----------+-----------------+
| google.is | Activo   | 142.250.200.67  |
+-----------+----------+-----------------+
| google.ms | Activo   | 142.250.184.4   |
+-----------+----------+-----------------+
| google.ps | Activo   | 142.250.200.68  |
+-----------+----------+-----------------+
| google.rs | Activo   | 142.250.185.3   |
+-----------+----------+-----------------+
| google.us | Activo   | 142.250.200.132 |
+-----------+----------+-----------------+
| google.ws | Activo   | 142.250.200.99  |
+-----------+----------+-----------------+
| google.ec | Activo   | 142.250.185.4   |
+-----------+----------+-----------------+
| google.ee | Activo   | 142.250.178.163 |
+-----------+----------+-----------------+
| google.eu | Activo   | 142.250.184.164 |
+-----------+----------+-----------------+
```
