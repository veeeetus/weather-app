import os
from rich.table import Table
from rich import print

def beautify(function):
    def wrap():
        os.system("cls")

        result = function()

        input("Press enter to continue...")

        os.system("cls")

        return result
    return wrap

def menu(mode):
    match mode:
        case "base":
            # Creates table body
            table = Table()

            table.add_column("Nr.", justify="center", style="cyan", no_wrap=True)
            table.add_column("Option", justify="left", style="cyan", no_wrap=True)

            table.add_row("1", "Current Temperature")
            table.add_row("2", "Current Day Forecast")
            table.add_row("3", "7 Days Temperature")
            table.add_row("4", "Exit")

            print(table)

def getInput(mode):
    match mode:
        case "option":
            while True:
                try:
                    option = int(input("Choose and option: "))
                    if 1 <= option <= 4:
                        return option
                    else:
                        print("[red]Choose available option 1-4")
                except:
                    print("[red]Invalid type you need to choose a number")