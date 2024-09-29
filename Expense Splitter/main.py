# def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:


def calculate_split(
    total_amount: float, percentages: list[float], currency: str
) -> None:
    # if number_of_people < 1:
    if len(percentages) < 1:
        # raise ValueError("Number of people must be greater than one.")
        raise ValueError("At least one person must be sharing the expense.")

    for i, percentage in enumerate(percentages, start=1):
        share = (percentage / 100) * total_amount
        print(f"Person {i} should pay : {currency} {share:,.2f} ({percentage}%)")

    # share_per_person: float = total_amount / number_of_people
    # print(f"Total expenses:{currency} {total_amount:,.2f}")
    # print(f"Number of people:{number_of_people}")
    # print(f"Each person should pay: {currency} {share_per_person:,.2f}")


def main() -> None:
    while True:
        try:
            total_amount: float = float(
                input("Enter the total amount of the expense: ")
            )
            number_of_people: int = int(
                input("Enter the number of people sharing the expense: ")
            )
            if number_of_people < 1:
                raise ValueError("Number of people should be greater than zero.")
                continue

            print(
                "Enter the percentage share for each person (make sure they sum up to 100):"
            )
            percentages = []

            for i in range(number_of_people):
                percentage = float(input(f"Percentage for person {i + 1}: "))
                percentages.append(percentage)

            if sum(percentages) != 100:
                raise ValueError("The sum of all percentages must be equal to 100.")
                continue
            # calculate_split(total_amount, number_of_people, currency="Rs")
            calculate_split(total_amount, percentages, currency="Rs")
            break

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
