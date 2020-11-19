import random
import sys

class Markedsstatus():

    def __init__(self, status, volum, pris):
        self.status = status
        self.volum = volum
        self.pris = pris

class Kostnadsscenario():

    def __init__(self, header, kostnad):
        self.header = header
        self.kostnad = kostnad

markedsvalg = []
markedsvalg.append(Markedsstatus("GODT", 100000, 40))
markedsvalg.append(Markedsstatus("MIDDELS", 75000, 50))
markedsvalg.append(Markedsstatus("SAKTE", 50000, 55))

kostnadsscenarioer = []
kostnadsscenarioer.append(Kostnadsscenario("ALTERNATIV 1", 27.5))
kostnadsscenarioer.append(Kostnadsscenario("ALTERNATIV 2", 32.5))
kostnadsscenarioer.append(Kostnadsscenario("ALTERNATIV 3", 37.5))

def tilf_markv_kostns():
    markv = random.choice(markedsvalg)
    kostns = random.choice(kostnadsscenarioer)
    return markv, kostns

def netto_profitt(markedsstatus, kostnadsscenario, faste_kostnader):
    return markedsstatus.volum*(markedsstatus.pris-kostnadsscenario.kostnad) - faste_kostnader

def simulate():
    markv, kostns = tilf_markv_kostns()
    net_prof = netto_profitt(markv, kostns, 600000)
    return net_prof

def run_monte_carlo(N): 
    # Num of simulations.
    net_profs = []
    for i in range(N):
        net_profs.append(simulate())

    mean = 0
    for i in range(len(net_profs)):
        mean += net_profs[i]

    return mean/len(net_profs) 



if __name__ == "__main__":
    N = int(sys.argv[1])
    print(run_monte_carlo(N))
