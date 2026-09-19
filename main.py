import datetime


def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello, GitHub! Push test at {now}")


if __name__ == "__main__":
    main()
