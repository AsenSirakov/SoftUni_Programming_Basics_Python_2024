jury_members = int(input())
total_score = 0
presentation_count = 0

while True:
    presentation_name = input()

    if presentation_name == "Finish":
        average_score = total_score / presentation_count
        print(f"Student's final assessment is {average_score:.2f}.")
        break

    current_presentation_score = 0
    for _ in range(jury_members):
        current_presentation_score += float(input())

    average_presentation_score = current_presentation_score / jury_members
    total_score += average_presentation_score
    presentation_count += 1

    print(f"{presentation_name} - {average_presentation_score:.2f}.")
