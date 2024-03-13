start_range = int(input())
end_range = int(input())

barcodes = []

for i in range(start_range // 1000, end_range // 1000 + 1):
    for j in range((start_range // 100) % 10, (end_range // 100) % 10 + 1):
        for k in range((start_range // 10) % 10, (end_range // 10) % 10 + 1):
            for l in range(start_range % 10, end_range % 10 + 1):
                barcode = str(i) + str(j) + str(k) + str(l)
                if all(int(digit) % 2 != 0 for digit in barcode):
                    barcodes.append(barcode)

print(" ".join(barcodes))
