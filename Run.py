import os, sys
from rich.console import Console
from login import Login as ZoraID

class Assetnya:
  def __init__(self) -> None:
    self.Create_Dir()
    pass

  def Create_Dir(self):
    try: os.mkdir('/sdcard/OK')
    except: pass
    try: os.mkdir('/sdcard/CP')
    except: pass
      
  def asset(self):
    try:
      os.system('git pull')
      ZoraID()
    except (Exception) as e:
      Console(width = 65, style = "bold grey50").print(Panel(f"[italic red]{str(e).title()}!", title = "[bold red]>[bold yellow]>[bold green]>[bold grey50] (Error) [bold green]<[bold yellow]<[bold red]<"))
      exit()

Assetnya().asset()
