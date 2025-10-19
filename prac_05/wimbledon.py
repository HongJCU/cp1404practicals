"""
Wimbledon.py
Estimate: 60 minutes
Actual:   40 minutes
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


#