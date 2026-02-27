"""
REPL entry point for the calculator application.
"""

from colorama import Fore, Style, init

from app.calculator_config import CalculatorConfig
from app.history import History
from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.input_validators import parse_two_numbers
from app.logger import setup_logger
from app.exceptions import ValidationError, OperationError, PersistenceError

init(autoreset=True)


class App:
    def __init__(self):
        self.config = CalculatorConfig()
        self.history = History(self.config)
        self.calculator = Calculator(self.config, self.history)

        self.logger = setup_logger()
        self.calculator.add_observer(LoggingObserver(self.logger))
        self.calculator.add_observer(AutoSaveObserver(self.config))

        self._commands = {
            "add", "subtract", "multiply", "divide",
            "power", "root", "modulus", "int_divide", "percent", "abs_diff",
            "history", "clear", "undo", "redo", "save", "load",
            "help", "exit"
        }

    def print_help(self):
        print(Fore.CYAN + "Available commands:")
        for cmd in sorted(self._commands):
            if cmd in {"history", "clear", "undo", "redo", "save", "load", "help", "exit"}:
                print(f"  - {cmd}")
            else:
                print(f"  - {cmd} <num1> <num2>")

    def run(self):
        print(Fore.GREEN + "Enhanced Calculator REPL (type 'help' for commands)")

        while True:
            try:
                user_input = input(Fore.YELLOW + "calc> ").strip()
                if not user_input:
                    continue

                parts = user_input.split()
                cmd = parts[0].lower()
                args = parts[1:]

                if cmd == "exit":
                    print(Fore.GREEN + "Bye!")
                    break

                if cmd == "help":
                    self.print_help()
                    continue

                if cmd == "history":
                    items = self.history.get_all()
                    if not items:
                        print(Fore.CYAN + "No history yet.")
                    else:
                        for i, c in enumerate(items, start=1):
                            print(f"{i}. {c.operation}({c.operand1}, {c.operand2}) = {c.result} @ {c.timestamp}")
                    continue

                if cmd == "clear":
                    self.history.clear()
                    print(Fore.GREEN + "History cleared.")
                    continue

                if cmd == "undo":
                    self.calculator.undo()
                    print(Fore.GREEN + "Undo successful.")
                    continue

                if cmd == "redo":
                    self.calculator.redo()
                    print(Fore.GREEN + "Redo successful.")
                    continue

                if cmd == "save":
                    self.history.save()
                    print(Fore.GREEN + f"Saved history to {self.config.history_path}")
                    continue

                if cmd == "load":
                    self.history.load()
                    print(Fore.GREEN + f"Loaded history from {self.config.history_path}")
                    continue

                # Operations
                a, b = parse_two_numbers(args, self.config.max_input_value)
                result = self.calculator.calculate(cmd, a, b)
                print(Fore.GREEN + f"Result: {result}")

            except (ValidationError, OperationError, PersistenceError) as e:
                print(Fore.RED + f"Error: {e}")
                self.logger.error(str(e))
            except KeyboardInterrupt:
                print("\n" + Fore.GREEN + "Bye!")
                break
