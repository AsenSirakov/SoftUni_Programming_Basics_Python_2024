total_tickets = 0
students_tickets = 0
standard_tickets = 0
kids_tickets = 0

movie_name = input()

while movie_name != "Finish":
    total_seats = int(input())
    sold_tickets = 0

    ticket_type = input()
    while ticket_type != "End":
        if ticket_type == "student":
            students_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kids_tickets += 1

        sold_tickets += 1
        total_tickets += 1

        if sold_tickets == total_seats:
            break

        ticket_type = input()

    percent_full = (sold_tickets / total_seats) * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    movie_name = input()

percent_students = (students_tickets / total_tickets) * 100
percent_standard = (standard_tickets / total_tickets) * 100
percent_kids = (kids_tickets / total_tickets) * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")
