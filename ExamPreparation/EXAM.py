import math

paint = 21.50
wallpaper = 5.20
number_of_paint_cans = int(input())
number_of_wallpaper_rolls = int(input())
price_of_one_pair_of_gloves = float(input())
price_of_one_brush = float(input())
gloves = math.ceil(number_of_wallpaper_rolls * 0.35)
brushes = math.floor(number_of_paint_cans * 0.48)
paint_total_cost = number_of_paint_cans * paint
wallpaper_total_cost = number_of_wallpaper_rolls * wallpaper
gloves_total_cost = gloves * price_of_one_pair_of_gloves
brushes_total_cost = brushes * price_of_one_brush
total_cost = paint_total_cost + wallpaper_total_cost + gloves_total_cost + brushes_total_cost
delivery_cost = total_cost / 15
print(f"This delivery will cost {delivery_cost:.2f} lv.")
