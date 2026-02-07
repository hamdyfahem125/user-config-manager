import streamlit as st
import pandas as pd
import os

# اسم الملف CSV
SETTINGS_FILE = "settings.csv"

# لو الملف مش موجود، نعمل واحد جديد
if not os.path.exists(SETTINGS_FILE):
    df = pd.DataFrame(columns=["key", "value"])
    df.to_csv(SETTINGS_FILE, index=False)

# دوال CRUD مع CSV
def load_settings():
    return pd.read_csv(SETTINGS_FILE)

def save_settings(df):
    df.to_csv(SETTINGS_FILE, index=False)

def add_setting(df, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in df['key'].str.lower().values:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    df.loc[len(df)] = [key, value]
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(df, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    mask = df['key'].str.lower() == key
    if mask.any():
        df.loc[mask, 'value'] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(df, key):
    key = key.lower()
    mask = df['key'].str.lower() == key
    if mask.any():
        df.drop(df[mask].index, inplace=True)
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(df):
    if df.empty:
        return "No settings available."
    result = "Current User Settings:\n"
    for _, row in df.iterrows():
        result += f"{row['key'].capitalize()}: {row['value']}\n"
    return result

# ===== Streamlit App =====
st.title("User Configuration Manager (CSV Version)")

# تحميل الإعدادات
df = load_settings()
message = ""

# اختيار العملية
operation = st.selectbox("Choose Operation", ["View Settings", "Add Setting", "Update Setting", "Delete Setting"])

if operation == "Add Setting":
    key = st.text_input("Enter setting name")
    value = st.text_input("Enter setting value")
    if st.button("Add"):
        message = add_setting(df, (key, value))
        save_settings(df)
        st.success(message)

elif operation == "Update Setting":
    key = st.text_input("Enter setting name")
    value = st.text_input("Enter new value")
    if st.button("Update"):
        message = update_setting(df, (key, value))
        save_settings(df)
        st.success(message)

elif operation == "Delete Setting":
    key = st.text_input("Enter setting name")
    if st.button("Delete"):
        message = delete_setting(df, key)
        save_settings(df)
        st.success(message)

elif operation == "View Settings":
    st.text_area("Current Settings", value=view_settings(df), height=200)

# زر تحميل الملف CSV
with open(SETTINGS_FILE, "rb") as f:
    file_bytes = f.read()

st.download_button(
    label="Download settings.csv",
    data=file_bytes,
    file_name="settings.csv",
    mime="text/csv"
)
