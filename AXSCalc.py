def main():
    # initial variables
    STARTING_AXS, MONTHLY_REFILL, AXS_PRICE, APY, YEARS, RESTAKE, AXS_MOON = get_vars()
    BASE_START = STARTING_AXS, MONTHLY_REFILL, AXS_PRICE
    print_start_recap(BASE_START, RESTAKE)
    axs, axs_last_year = STARTING_AXS, STARTING_AXS
    gain, stake_gain, last_gain = APY, 0, 0
    # algorithm
    for i in range(1, 365 * YEARS + 1):
        if not i % 30:
            axs += MONTHLY_REFILL
            gain = max(50, gain - 5)
        stake_gain += axs * gain / 365 / 100
        if not i % RESTAKE:
            axs += stake_gain
            stake_gain = 0
        if not i % 365:
            last_gain = print_year_recap(
                axs, axs_last_year, i // 365, last_gain, BASE_START
            )
            axs_last_year = axs
    print_total_recap(axs, BASE_START, AXS_MOON, YEARS, RESTAKE)


# ---- Variables


def get_vars():
    starting_amount = int(input("How many AXS you start with? (Default 0) ") or 0)
    refill = int(input("How many AXS you buy a month? (Default 0) ") or 0)
    axs_price = int(input("Current AXS Price? (Default 85€) ") or 85)
    moon_price = int(input("Which price if moon? (Default 200€) ") or 200)
    gain = int(input("Current APY? (Default 110%) ") or 110)
    years = int(input("How many years you wanna stake? (Default 1y) ") or 1)
    restake = int(input("How frequently you restake? (Default 1d) ") or 1)
    return starting_amount, refill, axs_price, gain, years, restake, moon_price


# ---- Recap functions


def print_start_recap(base_start, restake):
    starting_axs, monthly_refill, axs_price = base_start
    print(
        f"\n@ Day 0\n Starting with {starting_axs * axs_price:.0f} € "
        f"({starting_axs} AXS)\n Adding {monthly_refill * axs_price:.0f} € "
        f"({monthly_refill} AXS) every month\n Restaking every {restake} day(s)\n"
    )


def print_year_recap(axs, axs_last_year, year, last_gain, base_start):
    starting_axs, monthly_refill, axs_price = base_start
    gain = (axs - starting_axs - monthly_refill * 12 * year) * axs_price
    print(
        f"# Year {year}\n AXS in wallet: {axs:.2f}\n"
        f" Gain: {gain - last_gain:.0f} € ({axs * axs_price:.0f} € in wallet)\n"
    )
    return gain


def print_total_recap(axs, base_start, axs_moon, years, restake):
    starting_axs, monthly_refill, axs_price = base_start
    gain = (axs - starting_axs - monthly_refill * 12 * years) * axs_price
    moon_gain = (axs - starting_axs - monthly_refill * 12 * years) * axs_moon
    axs_bought = monthly_refill * years * 12 + starting_axs
    print(
        f"> Total AXS in wallet: {axs:.2f}\n"
        f"> Total gain: {gain:.0f} € ({axs * axs_price:.0f} € in wallet)\n"
        f"> Total gain (if moon to {axs_moon} €): {moon_gain:.0f} € "
        f"({axs * axs_moon:.0f} € in wallet)\n> Total AXS bought: "
        f"{axs_bought:.2f} ({axs * axs_price - gain:.0f} €)\n"
    )


if __name__ == "__main__":
    main()
