movie = input()
days = int(input())
tickets_number = int(input())
tickets_price = float(input())
percent_for_cinema = int(input())
ticket_per_day = tickets_number * tickets_price
total = days * ticket_per_day
percent_cinema = percent_for_cinema/100 * total
income = total - percent_cinema
print(f"The profit from the movie {movie} is {income:.2f} lv.")