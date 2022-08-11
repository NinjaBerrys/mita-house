import re

duration_options = ["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m",
                    "2h"":30m", "2h:45m", "3h:00m"]
duration = duration_options[10]
print(duration)
print(duration.split(":"))
duration = duration.split(":")
print(duration)
print(re.sub("\D", "", duration[0]))
print(re.sub("\D", "", duration[1]))

# for i in duration_options:
#     duration = duration_options[i]
#     print(duration.split(":"))
#     duration = duration.split(":")
#     print(re.sub("\D", "", duration[0]))
#     print(re.sub("\D", "", duration[1]))
