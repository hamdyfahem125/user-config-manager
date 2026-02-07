import json

def load_settings():
    try:
        with open("settings.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_settings(settings):
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)

def add_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    settings[key] = value
    save_settings(settings)
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, setting_pair):
    key, value = setting_pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        save_settings(settings)
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        save_settings(settings)
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"

def view_settings(settings):
    if not settings:
        return "No settings available."
    
    result = "Current User Settings:\n"
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result
