from task_manager import TaskManager

def show_menu():
    print("\n" + "="*40)
    print("        OdoPy - Aufgabenverwaltung")
    print("="*40)
    print("1 - Aufgabe hinzufügen")
    print("2 - Alle Aufgaben anzeigen")
    print("3 - Aufgabe als erledigt markieren")
    print("4 - Aufgabe löschen")
    print("0 - Beenden")
    print("="*40)

def main():
    tm = TaskManager()
    
    while True:
        show_menu()
        choice = input("Deine Wahl: ").strip()
        
        if choice == "1":
            title = input("Titel der Aufgabe: ").strip()
            if title:
                tm.add_task(title)
            else:
                print("❌ Titel darf nicht leer sein!")
        
        elif choice == "2":
            tm.list_tasks()
        
        elif choice == "3":
            tm.list_tasks()
            try:
                num = int(input("Nummer der erledigten Aufgabe: "))
                tm.complete_task(num)
            except ValueError:
                print("❌ Bitte eine gültige Zahl eingeben!")
        
        elif choice == "4":
            tm.list_tasks()
            try:
                num = int(input("Nummer der zu löschenden Aufgabe: "))
                tm.delete_task(num)
            except ValueError:
                print("❌ Bitte eine gültige Zahl eingeben!")
        
        elif choice == "0":
            print("👋 Auf Wiedersehen!")
            break
        
        else:
            print("❌ Ungültige Auswahl! Bitte 0-4 eingeben.")

if __name__ == "__main__":
    main()


