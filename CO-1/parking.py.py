from datetime import datetime


class ParkingSystem:

    def __init__(self):

        # Parking area with 100 slots
        self.areas = {
            "A": {
                "name": "Parking Area A",
                "slots": {i: None for i in range(1, 101)}
            }
        }

        # Store vehicle details
        self.vehicles = {}

        # Charges per hour
        self.rates = {
            "bike": 20,
            "car": 30,
            "truck": 50
        }

    # --------------------------------------------------
    # 1. Display Parking Areas
    # --------------------------------------------------

    def display_areas(self):

        print("\n========== PARKING AREAS ==========")

        for area_id, area in self.areas.items():

            total = len(area["slots"])
            occupied = 0

            for vehicle in area["slots"].values():

                if vehicle is not None:
                    occupied += 1

            available = total - occupied

            print("Area      :", area_id)
            print("Total     :", total)
            print("Occupied  :", occupied)
            print("Available :", available)

    # --------------------------------------------------
    # 2. Show Available Slots
    # --------------------------------------------------

    def show_available_slots(self):

        print("\n========== AVAILABLE SLOTS ==========")

        for area_id, area in self.areas.items():

            available = []

            for slot, vehicle in area["slots"].items():

                if vehicle is None:
                    available.append(slot)

            print("\nParking Area:", area_id)
            print("Available Slots:", len(available))

            print(available)

    # --------------------------------------------------
    # 3. Park Vehicle
    # --------------------------------------------------

    def park_vehicle(self):

        print("\n========== PARK VEHICLE ==========")

        area_id = input("Enter parking area: ").upper()

        vehicle_number = input(
            "Enter vehicle number: "
        ).upper()

        vehicle_type = input(
            "Enter vehicle type (bike/car/truck): "
        ).lower()

        # Check area
        if area_id not in self.areas:

            print("Invalid parking area.")
            return

        # Check vehicle type
        if vehicle_type not in self.rates:

            print("Invalid vehicle type.")
            return

        # Check vehicle already parked
        if vehicle_number in self.vehicles:

            print("Vehicle is already parked.")
            return

        # Find empty slot
        slot_number = None

        for slot in self.areas[area_id]["slots"]:

            if self.areas[area_id]["slots"][slot] is None:

                slot_number = slot
                break

        # Parking full
        if slot_number is None:

            print("Parking is FULL.")
            return

        # Entry time
        entry_time = datetime.now()

        # Store vehicle
        self.vehicles[vehicle_number] = {

            "type": vehicle_type,
            "area": area_id,
            "slot": slot_number,
            "entry": entry_time
        }

        # Occupy slot
        self.areas[area_id]["slots"][slot_number] = vehicle_number

        print("\n========== VEHICLE PARKED ==========")

        print("Vehicle Number :", vehicle_number)
        print("Vehicle Type   :", vehicle_type)
        print("Parking Area   :", area_id)
        print("Slot Number    :", slot_number)

        print(
            "Entry Time     :",
            entry_time.strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )
        )

        print("Status         : Parking Successful")

    # --------------------------------------------------
    # 4. Calculate Charge
    # --------------------------------------------------

    def calculate_charge(self, vehicle_type, entry_time, exit_time):

        # Find total seconds
        seconds = (exit_time - entry_time).total_seconds()

        # Convert seconds to minutes
        minutes = seconds / 60

        # Convert rate from per hour to per minute
        rate_per_hour = self.rates[vehicle_type]

        rate_per_minute = rate_per_hour / 60

        # Calculate charge
        charge = minutes * rate_per_minute

        return minutes, charge

    # --------------------------------------------------
    # 5. Vehicle Exit
    # --------------------------------------------------

    def vehicle_exit(self):

        print("\n========== VEHICLE EXIT ==========")

        vehicle_number = input(
            "Enter vehicle number: "
        ).upper()

        # Check vehicle
        if vehicle_number not in self.vehicles:

            print("Vehicle not found.")

            return

        # Get vehicle information
        vehicle = self.vehicles[vehicle_number]

        vehicle_type = vehicle["type"]
        area_id = vehicle["area"]
        slot_number = vehicle["slot"]
        entry_time = vehicle["entry"]

        # Get exit time
        exit_time = datetime.now()

        # Calculate charge
        minutes, charge = self.calculate_charge(
            vehicle_type,
            entry_time,
            exit_time
        )

        # Convert minutes to hours
        hours = minutes / 60

        # Release slot
        self.areas[area_id]["slots"][slot_number] = None

        # Remove vehicle
        del self.vehicles[vehicle_number]

        # Display bill
        print("\n========== PARKING BILL ==========")

        print("Vehicle Number :", vehicle_number)
        print("Vehicle Type   :", vehicle_type)
        print("Parking Area   :", area_id)
        print("Slot Number    :", slot_number)

        print(
            "Entry Time     :",
            entry_time.strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )
        )

        print(
            "Exit Time      :",
            exit_time.strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )
        )

        print(
            "Parking Time   :",
            round(hours, 2),
            "hours"
        )

        print(
            "Rate           : Rs.",
            self.rates[vehicle_type],
            "per hour"
        )

        print(
            "Parking Charge : Rs.",
            round(charge, 2)
        )

        print("\nSlot released successfully.")

    # --------------------------------------------------
    # 6. Show Parked Vehicles
    # --------------------------------------------------

    def show_vehicles(self):

        print("\n========== PARKED VEHICLES ==========")

        if len(self.vehicles) == 0:

            print("No vehicles are parked.")

            return

        for number, vehicle in self.vehicles.items():

            print("--------------------------------")

            print("Vehicle Number :", number)
            print("Vehicle Type   :", vehicle["type"])
            print("Parking Area   :", vehicle["area"])
            print("Slot Number    :", vehicle["slot"])

            print(
                "Entry Time     :",
                vehicle["entry"].strftime(
                    "%d-%m-%Y %I:%M:%S %p"
                )
            )

    # --------------------------------------------------
    # 7. Search Vehicle
    # --------------------------------------------------

    def search_vehicle(self):

        print("\n========== SEARCH VEHICLE ==========")

        number = input(
            "Enter vehicle number: "
        ).upper()

        if number not in self.vehicles:

            print("Vehicle is not currently parked.")

            return

        vehicle = self.vehicles[number]

        print("\nVehicle Number :", number)
        print("Vehicle Type   :", vehicle["type"])
        print("Parking Area   :", vehicle["area"])
        print("Slot Number    :", vehicle["slot"])

        print(
            "Entry Time     :",
            vehicle["entry"].strftime(
                "%d-%m-%Y %I:%M:%S %p"
            )
        )

    # --------------------------------------------------
    # 8. Show Charges
    # --------------------------------------------------

    def show_charges(self):

        print("\n========== PARKING RATES ==========")

        print("Bike  : Rs.20 per hour")
        print("Car   : Rs.30 per hour")
        print("Truck : Rs.50 per hour")

        print("\nThe system calculates the charge")
        print("according to the actual parking time.")

    # --------------------------------------------------
    # MAIN MENU
    # --------------------------------------------------

    def menu(self):

        while True:

            print("\n")
            print("==========================================")
            print("       PARKING MANAGEMENT SYSTEM")
            print("==========================================")

            print("1. Display Parking Areas")
            print("2. Show Available Slots")
            print("3. Park Vehicle")
            print("4. Vehicle Exit")
            print("5. Show Parked Vehicles")
            print("6. Search Vehicle")
            print("7. Show Parking Charges")
            print("8. Exit")

            print("==========================================")

            choice = input("Enter your choice: ")

            if choice == "1":

                self.display_areas()

            elif choice == "2":

                self.show_available_slots()

            elif choice == "3":

                self.park_vehicle()

            elif choice == "4":

                self.vehicle_exit()

            elif choice == "5":

                self.show_vehicles()

            elif choice == "6":

                self.search_vehicle()

            elif choice == "7":

                self.show_charges()

            elif choice == "8":

                print("\nThank you for using Parking System.")

                break

            else:

                print("Invalid choice.")


# --------------------------------------------------
# Start Program
# --------------------------------------------------

parking = ParkingSystem()

parking.menu()