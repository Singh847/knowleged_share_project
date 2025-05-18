import time
import random


class User:
    def __init__(self, name, age, sex, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.workout_history = []

    def add_workout(self, workout):
        self.workout_history.append(workout)

    def show_history(self):
        if not self.workout_history:
            print("No workout recorded yet.")
        else:
            print("\n🏋️ Workout History:")
            for workout in self.workout_history:
                print(f"🔹 {workout}")


class Workout:
    def __init__(self, name, duration, difficulty):
        self.name = name
        self.duration = duration
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.name} ({self.duration} min) - Difficulty: {self.difficulty}"


class WorkoutPlan:
    def __init__(self, user):
        self.user = user
        self.exercises = []

    def add_exercise(self, name, duration, difficulty):
        self.exercises.append(Workout(name, duration, difficulty))

    def show_plan(self):
        if not self.exercises:
            print("No exercises in your plan.")
        else:
            print("\n📋 Your Workout Plan:")
            for exercise in self.exercises:
                print(f"🔹 {exercise}")


class GymApp:
    def __init__(self):
        self.user = None
        self.workout_plan = None

    def register_user(self):
        name = input("Enter your name: ")
        while True:
            try:
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        sex = input("Enter your gender (M/F): ").strip().upper()
        while True:
            try:
                weight = float(input("Enter your weight (kg): "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        self.user = User(name, age, sex, weight)
        self.workout_plan = WorkoutPlan(self.user)
        print(f"\n✅ Welcome, {self.user.name}! Your gym journey begins now!\n")

    def generate_workout(self):
        exercises = [
            ("Push-ups", 10, "Medium"),
            ("Squats", 15, "Easy"),
            ("Burpees", 12, "Hard"),
            ("Plank", 5, "Medium"),
            ("Lunges", 10, "Easy"),
            ("Jumping Jacks", 10, "Easy"),
            ("Bench Press", 15, "Hard"),
            ("Deadlifts", 12, "Hard"),
            ("Bicep Curls", 10, "Medium"),
        ]
        chosen = random.choice(exercises)
        print(f"\n🤖 AI Suggests: {chosen[0]} ({chosen[1]} min) - Difficulty: {chosen[2]}")
        self.user.add_workout(f"{chosen[0]} ({chosen[1]} min) - {chosen[2]}")

    def rest_timer(self, seconds):
        print(f"\n⏳ Resting for {seconds} seconds...")
        for i in range(seconds, 0, -1):
            print(i, end=" ", flush=True)
            time.sleep(1)
        print("\n✅ Rest over! Get back to your workout! 💪")

    def add_custom_workout(self):
        if not self.user:
            print("⚠️ No user found! Please register first.")
            return

        name = input("Enter workout name: ")
        while True:
            try:
                duration = int(input("Enter duration (minutes): "))
                break
            except ValueError:
                print("Invalid input! Please enter a number.")

        difficulty = input("Enter difficulty (Easy/Medium/Hard): ").capitalize()
        self.workout_plan.add_exercise(name, duration, difficulty)
        print(f"✅ Workout {name} added to your plan!")

    def menu(self):
        while True:
            print("\n🏋️ Gym Workout App 🏋️")
            print("1️⃣ Register User")
            print("2️⃣ Show Workout History")
            print("3️⃣ Get Workout Suggestion")
            print("4️⃣ Start Rest Timer")
            print("5️⃣ Add Custom Workout")
            print("6️⃣ Show Workout Plan")
            print("7️⃣ Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                if self.user:
                    self.user.show_history()
                else:
                    print("⚠️ No user found! Please register first.")
            elif choice == "3":
                if self.user:
                    self.generate_workout()
                else:
                    print("⚠️ No user found! Please register first.")
            elif choice == "4":
                if self.user:
                    seconds = int(input("Enter rest time in seconds: "))
                    self.rest_timer(seconds)
                else:
                    print("⚠️ No user found! Please register first.")
            elif choice == "5":
                self.add_custom_workout()
            elif choice == "6":
                if self.workout_plan:
                    self.workout_plan.show_plan()
                else:
                    print("⚠️ No user found! Please register first.")
            elif choice == "7":
                print("🚪 Exiting Gym Workout App. Stay fit! 💪")
                break
            else:
                print("❌ Invalid choice, please try again.")


if __name__ == "__main__":
    app = GymApp()
    app.menu()
