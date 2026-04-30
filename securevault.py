# securevault.py

from crypto_utils import encrypt_file, decrypt_file


def menu():
    while True:
        print("\n=== SecureVault CLI ===")
        print("1. Encrypt file")
        print("2. Decrypt file")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            filename = input("File to encrypt: ")
            password = input("Password: ")

            try:
                encrypt_file(filename, password)
            except FileNotFoundError:
                print("❌ File not found.")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "2":
            filename = input("Encrypted file (.bin): ").strip().strip('"')
            password = input("Password: ").strip()

            try:
                decrypt_file(filename, password)
            except FileNotFoundError:
                print("❌ File not found.")
            except ValueError:
                print("❌ Wrong password or file tampered!")
            except Exception as e:
                print(f"❌ Error: {e}")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()