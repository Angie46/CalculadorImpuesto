import streamlit as st

# Definición de la UIT para 2025
UIT = 5350  # Unidad Impositiva Tributaria 2025

def calcular_impuesto(renta_neta):
    """
    Calcula el impuesto a la renta aplicando las tasas progresivas según los tramos establecidos.
    """
    if renta_neta <= 5 * UIT:
        impuesto = renta_neta * 0.08
    elif renta_neta <= 20 * UIT:
        impuesto = (5 * UIT * 0.08) + ((renta_neta - 5 * UIT) * 0.14)
    elif renta_neta <= 35 * UIT:
        impuesto = (5 * UIT * 0.08) + (15 * UIT * 0.14) + ((renta_neta - 20 * UIT) * 0.17)
    elif renta_neta <= 45 * UIT:
        impuesto = (5 * UIT * 0.08) + (15 * UIT * 0.14) + (15 * UIT * 0.17) + ((renta_neta - 35 * UIT) * 0.20)
    else:
        impuesto = (5 * UIT * 0.08) + (15 * UIT * 0.14) + (15 * UIT * 0.17) + (10 * UIT * 0.20) + ((renta_neta - 45 * UIT) * 0.30)
    return impuesto

def calcular_impuesto_total(ingreso_anual):
    """
    Calcula el impuesto total considerando la deducción de 7 UIT y aplicando las tasas progresivas.
    """
    deduccion = 7 * UIT  # Deducción fija de 7 UIT
    renta_neta = max(0, ingreso_anual - deduccion)
    impuesto = calcular_impuesto(renta_neta)
    return impuesto

# Título de la aplicación
st.title("Calculadora de Impuestos - Perú 2025")

# Sección de ingresos de cuarta categoría
st.header("Ingresos de Cuarta Categoría")
st.write("Ingrese su ingreso anual proveniente de trabajos independientes (honorarios profesionales, consultorías, etc.).")
ingreso_cuarta = st.number_input("Ingreso anual de cuarta categoría (S/):", min_value=0.0, step=100.0)

# Sección de ingresos de quinta categoría
st.header("Ingresos de Quinta Categoría")
st.write("Ingrese su ingreso anual proveniente de trabajos dependientes (planilla, sueldos, salarios, etc.).")
ingreso_quinta = st.number_input("Ingreso anual de quinta categoría (S/):", min_value=0.0, step=100.0)

# Botón para calcular impuestos
if st.button("Calcular Impuestos"):
    # Cálculo de impuestos para cada categoría
    impuesto_cuarta = calcular_impuesto_total(ingreso_cuarta)
    impuesto_quinta = calcular_impuesto_total(ingreso_quinta)
    total_impuesto = impuesto_cuarta + impuesto_quinta

    # Mostrar resultados
    st.subheader("Resultados")
    st.write(f"**Impuesto a pagar por cuarta categoría:** S/ {impuesto_cuarta:,.2f}")
    st.write(f"**Impuesto a pagar por quinta categoría:** S/ {impuesto_quinta:,.2f}")
    st.write(f"**Total de impuesto a pagar:** S/ {total_impuesto:,.2f}")

# Pie de página con créditos
st.write("---")
st.write("**Creado por los alumnos:** Angie Cordova Angulo, Arvic Jara Herrera y Junior Saavedra Dominguez")
