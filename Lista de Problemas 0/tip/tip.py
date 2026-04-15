def main():
    dollars = input("Quanto custou a refeição? ")
    dollars = dollars_to_float(dollars)
    percent = input("What percentage would you like to tip? ")
    percent = percent_to_float(percent)
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")




def dollars_to_float(d):
    d = d.replace('$','')
    d = float(d)
    return d

def percent_to_float(p):
    p = p.replace('%','')
    p = float(p)
    p = p /100
    return p

main()
