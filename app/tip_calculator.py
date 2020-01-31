def bill_amount(num=0):
    return float(num)


def tip_percentage(num=0):
    return num / 100


def main():
    tip_total = bill_amount(10) * tip_percentage(15)
    print(f"Tip total: ${tip_total:0.2f}")


if __name__ == "__main__":
    main()
