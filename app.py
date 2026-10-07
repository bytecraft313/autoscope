import streamlit as st

from obd_interface.connection import OBDConnection
from obd_interface.reader import OBDReader
from obd_interface.parameters import PARAMETERS

# Must be the first Streamlit call
st.set_page_config(page_title="AutoScope", page_icon="🚗", layout="wide")

st.title("🚗 AutoScope")
st.caption("Python-based OBD-II vehicle diagnostics and data analysis")


@st.cache_resource
def get_reader():
    connection = OBDConnection(simulation=True)
    return connection, OBDReader(connection)


connection, reader = get_reader()

# Connection status
st.subheader("Connection")
if connection.connected:
    st.success(connection.status())
else:
    st.error(connection.status())


def show_metric(key, value, decimals):
    p = PARAMETERS[key]
    text = "N/A" if value is None else f"{value:.{decimals}f} {p['unit']}"
    st.metric(p["name"], text)


# Vehicle data
st.subheader("Vehicle Data")

data = reader.read_parameters(PARAMETERS)

layout = [
    [("rpm", 0), ("speed", 0), ("coolant_temp", 1)],
    [("throttle", 1), ("engine_load", 1), ("intake_temp", 1)],
]

for row in layout:
    for col, (key, decimals) in zip(st.columns(3), row):
        with col:
            show_metric(key, data[key], decimals)