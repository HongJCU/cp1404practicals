"""
Wimbledon.py
Estimate: 60 minutes
Actual:   50 minutes
"""

# Add a funciton to read csv file
def read_csv_file(filename):
    with open(filename,"r",encoding="utf-8-sig") as in_file:
        #after done reading, the cursor will jump down one line
        in_file.readline()
        data=[line.strip().split(",") for line in in_file]
    return data

# Add a counter to count the champion
def count_champions(data):

    champion_to_count = {}
    for row in data:
        champion = row[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count

# Created a function remove duplicate and sort them alphabetically for display
def get_countries(data):
    countries = {row[1] for row in data}
    return sorted(countries)

# Created a function to display the result as formatted
def main():
    filename = "wimbledon.csv"
    data=read_csv_file(filename)
    champion_to_count = count_champions(data)
    countries = get_countries(data)
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_count.items()):
        print(f"{champion:20} {wins}", sep="")

    print(f"There {len(countries)} countries have won Wimbledon: ", ", ".join(countries))


main()
