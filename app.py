import streamlit as st
import obd

from obd_interface.connection import OBDConnection
from obd_interface.reader import OBDReader


st.set_page_config(
    page_title="AutoScope",
    page_icon="🚗",
    layout="wide",
)

st.title("🚗 AutoScope")
st.caption("Python-based OBD-II vehicle diagnostics and data analysis")


# Connection
connection = OBDConnection(simulation=True)
reader = OBDReader(connection)


# Connection status
st.subheader("Connection")

if connection.connected:
    st.success(connection.status())
else:
    st.error(connection.status())


# Vehicle data
st.subheader("Vehicle Data")

rpm = reader.read(obd.commands.RPM)
speed = reader.read(obd.commands.SPEED)
coolant = reader.read(obd.commands.COOLANT_TEMP)
throttle = reader.read(obd.commands.THROTTLE_POS)
load = reader.read(obd.commands.ENGINE_LOAD)
intake_temp = reader.read(obd.commands.INTAKE_TEMP)


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("RPM", f"{rpm:.0f}")

with col2:
    st.metric("Speed", f"{speed:.0f} km/h")

with col3:
    st.metric("Coolant", f"{coolant:.1f} °C")


col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Throttle", f"{throttle:.1f}%")

with col5:
    st.metric("Engine Load", f"{load:.1f}%")

with col6:
    st.metric("Intake Temperature", f"{intake_temp:.1f} °C")