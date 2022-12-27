from math import gcd

bio_team = int(input("Count of first team -> "))
info_team = int(input("Count of second team -> "))

print((bio_team * info_team) / gcd(bio_team, info_team))
