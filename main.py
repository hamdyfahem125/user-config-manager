from config_manager import *

def main():
    settings = load_settings()

    while True:
        print("\nUser Configuration Manager")
        print("1. Add Setting")
        print("2. Update Setting")
        print("3. Delete Setting")
        print("4. View Settings")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            key = input("Enter setting name: ")
            value = input("Enter setting value: ")
            print(add_setting(settings, (key, value)))

        elif choice == "2":
            key = input("Enter setting name: ")
            value = input("Enter new value: ")
            print(update_setting(settings, (key, value)))

        elif choice == "3":
            key = input("Enter setting name: ")
            print(delete_setting(settings, key))

        elif choice == "4":
            print(view_settings(settings))

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
