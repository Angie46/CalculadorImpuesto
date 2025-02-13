import streamlit as st

# Título de la aplicación
st.title("🧮 Cálculo del Impuesto a la Renta (4ta y 5ta Categoría) - Perú")

# Entrada de valor de la UIT (editable)
st.sidebar.header("⚙️ Configuración")
UIT = st.sidebar.number_input("Valor de la UIT (S/.)", min_value=5000, max_value=6000, value=5350, step=50)

# Entrada de ingresos
st.header("📌 Ingresos")
ingreso_4ta = st.number_input("Ingresos por 4ta Categoría (S/.)", min_value=0.0, value=0.0, step=100.0)
ingreso_5ta = st.number_input("Ingresos por 5ta Categoría (S/.)", min_value=0.0, value=0.0, step=100.0)

# Aplicar descuento del 20% a la renta de 4ta categoría
descuento_4ta = ingreso_4ta * 0.20
ingreso_4ta_neto = ingreso_4ta - descuento_4ta

# Suma de ingresos anuales
ingreso_total = ingreso_4ta_neto + ingreso_5ta

# Deducciones
st.header("📉 Deducciones")
deduccion_7uit = min(7 * UIT, ingreso_total)  # Solo se descuenta hasta el total de ingresos
base_imponible = max(0, ingreso_total - deduccion_7uit)

# Función para calcular el impuesto según las escalas
def calcular_impuesto(base):
    tramos = [5 * UIT, 20 * UIT, 35 * UIT, 45 * UIT]  # Límites de cada tramo
    tasas = [0.08, 0.14, 0.17, 0.20, 0.30]  # Tasas de impuestos

    impuesto = 0
    for i, tramo in enumerate(tramos):
        if base > tramo:
            impuesto += tramo * tasas[i]
            base -= tramo
        else:
            impuesto += base * tasas[i]
            return impuesto
    impuesto += base * tasas[-1]  # Último tramo (30%)
    return impuesto

# Cálculo del impuesto
impuesto_anual = calcular_impuesto(base_imponible)

# Mostrar resultados
st.header("📊 Resultados")
st.write(f"🔹 **Ingresos 4ta Categoría Neto:** S/. {ingreso_4ta_neto:,.2f}")
st.write(f"🔹 **Ingresos Totales:** S/. {ingreso_total:,.2f}")
st.write(f"🔹 **Deducción 7 UIT:** S/. {deduccion_7uit:,.2f}")
st.write(f"🔹 **Base Imponible:** S/. {base_imponible:,.2f}")
st.write(f"🟢 **Impuesto a la renta Anual a Pagar:** S/. {impuesto_anual:,.2f}")

# Visualización de impuestos en una barra de progreso
st.progress(min(1, impuesto_anual / ingreso_total) if ingreso_total > 0 else 0)

st.write("**Creado por los alumnos:** Angie Cordova Angulo, Arvic Jara Herrera y Junior Saavedra Dominguez")
