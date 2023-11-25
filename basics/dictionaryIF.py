# days = {
#     "s":"Sunday",
#     "m": "Monday",
#     "t":"Tuesday",
#     "w":"Wednesday",
#     "th":"Thursday",
#     "f":"Friday",
#     "sa":"Saturday"}

days = dict(
     s ="Sunday",
     m = "Monday",
     t ="Tuesday",
     w ="Wednesday",
     th ="Thursday",
     f ="Friday",
     sa ="Saturday")
day = "s"
print(days.get(day,"please you have a mistake"))