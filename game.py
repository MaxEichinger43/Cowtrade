import os

# Definiere den Pfad zum Ordner mit den Strategien
strategies_folder = "C:/Users/Der Maxi/Documents/GitHub/Cowtrade/strategies"

STARTING_CAPITAL = 1000
strategy_list = []
# Iteriere durch alle Dateien im Ordner
i = 0
for strategy in os.listdir(strategies_folder):
    if strategy.endswith(".py") and strategy != "__init__.py":
        # Extrahiere den Dateinamen ohne Erweiterung
        strategy_name = os.path.splitext(strategy)[0]

        try:
            # Versuche die Strategie zu importieren
            exec(f"import strategies.{strategy_name} as strat{i}")
            print(f"{strategy_name} erfolgreich als strat{i} importiert")
            exec(f"strategy_list.append(strat{i})")
            i += 1
            
        except ImportError:
            print(f"{strategy_name} konnte nicht importiert werden")

        exec(f"{strategy_name}_capital = {STARTING_CAPITAL}")

class Strategy:
    def __init__(self, STARTING_CAPITAL, name) -> None:
        self.capital = STARTING_CAPITAL
        self.name = name
    def get_investment(self):
        return self.investment()


def get_starting_capital():
    pass