class VolunteerRegistry:

    def __init__(self):
        self.volunteers = []

    def register_volunteer(self, name, age):

        if age < 16:
            return False

        volunteer = {
            "name": name,
            "age": age
        }

        self.volunteers.append(volunteer)
        return True

    def volunteer_exists(self, name):

        return any(
            volunteer["name"] == name
            for volunteer in self.volunteers
        )

    def total_volunteers(self):

        return len(self.volunteers)

    def view_volunteers(self):

        return self.volunteers


def main():

    registry = VolunteerRegistry()

    while True:

        print("\n=== Volunteer Registration System ===")
        print("1. Register Volunteer")
        print("2. View Volunteers")
        print("3. View Total Volunteers")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter volunteer name: ")

            try:
                age = int(input("Enter age: "))
            except ValueError:
                print("Age must be a number.")
                continue

            if registry.register_volunteer(name, age):
                print("Volunteer registered successfully.")
            else:
                print("Volunteer must be at least 16 years old.")

        elif choice == "2":

            volunteers = registry.view_volunteers()

            if not volunteers:
                print("No volunteers registered.")
            else:
                print("\nRegistered Volunteers:")
                for volunteer in volunteers:
                    print(
                        f"{volunteer['name']} (Age: {volunteer['age']})"
                    )

        elif choice == "3":

            print(
                f"Total Volunteers: {registry.total_volunteers()}"
            )

        elif choice == "4":

            print("Exiting system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()