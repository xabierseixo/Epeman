# epeman
Medición de temperatura

## Crear a Base de Datos
BEGIN;
CREATE TABLE temperaturas (timestamp DATETIME, temperatura NUMERIC);
COMMIT;
.quit

## Extraer datos
select cast(strftime('%Y', timestamp) as integer), cast(strftime('%m', timestamp) as integer) ,cast(strftime('%W', timestamp) as integer) ,cast(strftime('%d', timestamp) as integer), cast(strftime('%H', timestamp) as integer), cast(strftime('%M', timestamp) as integer), cast(strftime('%S', timestamp) as integer) from temperaturas;