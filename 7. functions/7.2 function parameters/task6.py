# В какое время созвон?

def print_perm_time_call(msc_time: str):
    if msc_time[0:2] != "00":
        h = msc_time[0:2].lstrip("0")
        m = msc_time[3:]
    else:
        h = msc_time[0:2]
        m = msc_time[3:]

    if int(h) + 2 >= 10:
        print("Созвон будет в ", end="")
        print(int(h) + 2, m, sep=":", end=".")
    elif int(h) + 2 < 10:
        print("Созвон будет в ", end="")
        print("0" + str(int(h) + 2), m, sep=":", end=".")

print_perm_time_call("00:05")