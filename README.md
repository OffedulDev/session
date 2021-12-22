
> from objectmanager import (CreateObject, 
> GetObject, DeleteObject, InitializeSession, 
> GetJson, PrintContentOnFile, UpdateSession)

> import json  

> def init():
	> InitializeSession("b43783985vb478bperosbvy47vn7etsjrnvte4bg7t9e9")

	> CreateObject("nome", "pina", str)
	> CreateObject("ladra", "grazia", str)
	> CreateObject("poliziotto", "filippo", str)
	> CreateObject("attore", "andrea", str)
	> CreateObject("gestore", "marco", str)
	> CreateObject("direttori", ["claudio", "sandro", "cagliari"], list)
	> CreateObject("soldi", 34, int)
	> CreateObject("gemme", 2, int)
	> UpdateSession()

	> PrintContentOnFile("test")






> if __name__ == "__main__":
	> init()
