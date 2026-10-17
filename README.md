# 📦 Análisis y Clasificación de Inventarios ABC para CEDI (Supply Chain Analytics)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas)
![Status](https://img.shields.io/badge/Status-Completado-success)

## 🎯 Objetivo del Proyecto
Optimizar el control de stock y la toma de decisiones en un Centro de Distribución (CEDI) mediante la **clasificación ABC** basada en la **Regla de Pareto (80/20)**. 

Este proyecto busca identificar los productos (SKUs) de mayor impacto financiero y rotación para priorizar conteos cíclicos, minimizar descalces de inventario y optimizar la disposición física en el almacén.

---

## 🛠️ Tecnologías y Herramientas
* **Lenguaje de Programación:** Python 3.x
* **Librerías de Análisis:** `Pandas`, `NumPy`
* **Entorno de Desarrollo:** Visual Studio Code / Jupyter Notebook
* **Enfoque de Negocio:** Gestión de Inventarios, Logística Operativa y Supply Chain.

---

## 📊 Metodología y Desarrollo
1. **Modelado y Consolidación de Datos:**
   * Evaluación de stock actual, descripciones de producto y costos unitarios de almacenamiento.
2. **Cálculo de Impacto Financiero:**
   * Determinación del valor total de inventario por SKU (`Stock_Actual * Costo_Unitario`).
3. **Ponderación y Acumulados (Regla de Pareto):**
   * Ordenamiento descendente y cálculo del porcentaje acumulado sobre la inversión total en stock.
4. **Segmentación de Inventario (Clasificación ABC):**
   * **Clase A (Hasta 80% del valor total):** Productos críticos de alto valor. Requieren conteos cíclicos diarios/semanales y ubicación estratégica en zonas de rápido picking.
   * **Clase B (80% - 95% del valor total):** Productos de valor e impacto moderado.
   * **Clase C (95% - 100% del valor total):** Productos de bajo costo unitario o baja rotación. Se gestionan con controles periódicos automatizados.

---

## 📈 Resultados e Insights Clave
* **Control Focalizado:** Se logró clasificar y aislar el **20% del catálogo** que representa cerca del **80% del capital inmovilizado** en el CEDI.
* **Optimización Operativa:** La propuesta incluye reubicar los artículos Clase A cerca de las mallas de despacho para reducir los recorridos de picking y optimizar tiempos de alistamiento.

---

## 📁 Estructura del Repositorio
```text
├── data/                    # Datasets (simulados / anonimizados)
├── notebooks/               # Jupyter Notebooks con el análisis paso a paso
├── scripts/                 # Script ejecutable en Python (analisis_abc.py)
└── README.md                # Documentación del proyecto
