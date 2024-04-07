tournaments = 0
matches_won = 0
matches_lost = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

    matches = int(input())
    matches_won_tournament = 0
    matches_lost_tournament = 0

    for match in range(1, matches + 1):
        desis_points = int(input())
        opponents_points = int(input())

        if desis_points > opponents_points:
            matches_won_tournament += 1
            print(f"Game {match} of tournament {tournament_name}: win with {desis_points - opponents_points} points.")
        else:
            matches_lost_tournament += 1
            print(f"Game {match} of tournament {tournament_name}: lost with {opponents_points - desis_points} points.")

    tournaments += 1
    matches_won += matches_won_tournament
    matches_lost += matches_lost_tournament

print(f"{matches_won / (matches_won + matches_lost) * 100:.2f}% matches win")
print(f"{matches_lost / (matches_won + matches_lost) * 100:.2f}% matches lost")
