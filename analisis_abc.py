import pandas as pd

# 1. Simulación de datos operativos de un CEDI (Inventario y Ventas Anuales)
data = {
    'SKU': ['SKU_001', 'SKU_002', 'SKU_003', 'SKU_004', 'SKU_005', 'SKU_006', 'SKU_007', 'SKU_008'],
    'Descripcion': ['Analgésico A', 'Antibiótico B', 'Anestésico C', 'Suero Fisiológico', 'Material Quirúrgico', 'Jeringas X', 'Guantes de Látex', 'Vendas Elásticas'],
    'Stock_Actual': [150, 300, 50, 1200, 80, 5000, 2500, 600],
    'Costo_Unitario': [45.50, 120.00, 350.00, 15.00, 500.00, 2.50, 8.00, 12.50]
}

df = pd.DataFrame(data)

# 2. Calcular el valor total del inventario por SKU
df['Valor_Total_Inventario'] = df['Stock_Actual'] * df['Costo_Unitario']

# 3. Ordenar los productos de mayor a menor valor de inventario (Regla de Pareto)
df = df.sort_values(by='Valor_Total_Inventario', ascending=False).reset_index(drop=True)

# 4. Calcular el porcentaje acumulado del valor
df['Valor_Acumulado'] = df['Valor_Total_Inventario'].cumsum()
df['Porcentaje_Acumulado'] = (df['Valor_Acumulado'] / df['Valor_Total_Inventario'].sum()) * 100

# 5. Asignar la Clasificación ABC
def clasificar_abc(porcentaje):
    if porcentaje <= 80:
        return 'Clase A (Alto Valor / Control Estricto)'
    elif porcentaje <= 95:
        return 'Clase B (Valor Moderado)'
    else:
        else_val = 'Clase C (Bajo Valor / Stock Masivo)'
        return else_val

df['Clasificacion_ABC'] = df['Porcentaje_Acumulado'].apply(clasificar_abc)

# Mostrar resultados limpios en consola
print("--- REPORTE DE CLASIFICACIÓN ABC DE INVENTARIOS ---")
print(df[['SKU', 'Descripcion', 'Stock_Actual', 'Valor_Total_Inventario', 'Clasificacion_ABC']])
