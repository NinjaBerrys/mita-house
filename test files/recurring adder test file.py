import re
duration_options = ["0h:15m", "0h:30m", "0h:45m", "1h:00m", "1h:15m", "1h:30m", "1h:45m", "2h:00m", "2h:15m",
                    "2h"":30m", "2h:45m", "3h:00m"]
formatted_duration_options = [["0", "15"], ["0", "30"], ["0", "45"], ["1", "00"], ["1", "15"], ["1", "30"], ["1", "45"],
                              ["2", "00"], ["2", "15"], ["2", "30"], ["2", "45"], ["3", "00"]]
# for i in formatted_duration_options:
#     duration = duration_options[i]
#     print(duration.split(":"))
#     duration = duration.split(":")
#     print(re.sub("\D", "", duration[0]))
#     print(re.sub("\D", "", duration[1]))
print(sum(formatted_duration_options))