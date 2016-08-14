in_file = open("full-list.csv")
out_file = open("card-face-list.txt","w")

card_face_list = set()

for line in in_file:
    t = line.strip().split(",")
    string = t[-1]
    card_face_list.add(string)

card_face_list = list(card_face_list)
card_face_list.sort()

for card in card_face_list:
    out_file.write(card+"\n")
