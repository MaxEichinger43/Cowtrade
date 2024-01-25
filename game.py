import os

# Definiere den Pfad zum Ordner mit den Strategien
strategies_folder = "C:/Users/Der Maxi/Documents/GitHub/Cowtrade/strategies"

STARTING_CAPITAL = 1000

"""
objects
"""
class Strategy:
    def __init__(self) -> None:
        self.capital = STARTING_CAPITAL
        self.invest = 0
    def get_investment(self):
        pass


strategy_list = []


"""
import
"""
i = 0
# Iteriere durch alle Dateien im Ordner
for strategy in os.listdir(strategies_folder):
    if strategy.endswith(".py") and strategy != "__init__.py":
        # Extrahiere den Dateinamen ohne Erweiterung
        strategy_name = os.path.splitext(strategy)[0]

        try:
            # Versuche die Strategie zu importieren
            exec(f"from strategies.{strategy_name} import *")
            print(f"{strategy_name} erfolgreich importiert")

        except ImportError:
            print(f"{strategy_name} konnte nicht importiert werden")

        strategy_name = Strategy()
        strategy_list.append(strategy_name)
        print("Capital: ",strategy_list[i].capital)
        strategy_list[i].invest = strategy_list[i].get_investment()
        print("Invest: ",strategy_list[i].invest)
        i+=1


def get_starting_capital(strategy_list):
    pass