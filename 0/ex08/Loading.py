import os


def get_barre(i, stop) -> str:
    msg = ""
    nbcol = os.get_terminal_size().columns - (7 + len(str(stop)) * 2 + 27)
    nbbarre = int(i*nbcol/stop)
    for b in range(nbbarre):
        msg += "█"
    for s in range(nbcol - nbbarre):
        msg += " "
    return msg


def ft_tqdm(lst: range) -> None:
    for i in lst:
        pourcentage = int(i*100/lst.stop)
        if i == lst.stop:
            pourcentage = 100
        if (pourcentage < 10):
            print(f"\r  {pourcentage}%|{get_barre(i, lst.stop)}", end="")
            print(f"| {i}/{lst.stop}", end="")
        elif (pourcentage < 100):
            print(f"\r {pourcentage}%|{get_barre(i, lst.stop)}", end="")
            print(f"| {i}/{lst.stop}", end="")
        else:
            print(f"\r{pourcentage}%|{get_barre(i, lst.stop)}", end="")
            print(f"| {i}/{lst.stop}", end="")
        yield
    print(f"\r{100}%|{get_barre(lst.stop, lst.stop)}| {lst.stop}/{lst.stop}")
