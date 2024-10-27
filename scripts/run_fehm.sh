#!/bin/bash

# Comando codificado para ser ejecutado por el botón "Run FEHM"
echo "Ejecutando FEHM..."
# Agrega el comando real para ejecutar FEHM aquí

# Move files from app/output/pared2d to ../FEHM/fehmpytests/escenarios/heat/pared/input
if [ -d "app/output/pared2d" ]; then
    mv app/output/pared2d/* ../FEHM/fehmpytests/escenarios/heat/pared/input/
    echo $PWD
    echo "Archivos movidos de app/output/pared2d a ../FEHM/fehmpytests/escenarios/heat/pared/input"
fi

# Move files from app/output/pared3d to ../FEHM/fehmpytests/escenarios/heat/pared3d/input
if [ -d "app/output/pared3d" ]; then
    mv app/output/pared3d/* ../FEHM/fehmpytests/escenarios/heat/pared3d/input/
    echo "Archivos movidos de app/output/pared3d a ../FEHM/fehmpytests/escenarios/heat/pared3d/input"
    echo $PWD
fi

# Move files from app/output/barovel to ../FEHM_mast/fehmpytests/escenarios/isotermal/baro_vel_V2/input
if [ -d "app/output/barovel" ]; then
    mv app/output/barovel/* ../FEHM_mast/fehmpytests/escenarios/isotermal/baro_vel_V2/input/
    echo "Archivos movidos de app/output/barovel a ../FEHM/fehmpytests/escenarios/isotermal/baro_vel_V2/input"
    echo $PWD
fi
