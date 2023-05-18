import multiprocessing
from search_eshop import*
from search_nuuvem import*
from search_psn import*
from search_steam import*
import sqlite3
from datetime import date
import os
#os.system('cls' if os.name == 'nt' else 'clear')#limpar terminarl





def multi_eshop():
    print("Hello from the new process: Eshop")
    eshopjogo()    

def multi_nuuvem():
    print("Hello from the new process:Nuuvem")
    nuuvemgame()    
def multi_psn():
    print("Hello from the new process: PSN ")
    psnjogo()    

def multi_steam():
    print("Hello from the new process: Steam ")
    steam_()
    
if __name__ == '__main__':
    # Start a new process
    p_eshop = multiprocessing.Process(target=multi_eshop)
    p_nuuvem = multiprocessing.Process(target=multi_nuuvem)
    p_psn = multiprocessing.Process(target=multi_psn)
    p_steam = multiprocessing.Process(target=multi_steam)
    p_eshop.start()
    p_nuuvem.start() 
    p_psn.start()
    p_steam.start()
    p_eshop.join()
    p_nuuvem.join() 
    p_psn.join()
    p_steam.join()
    
    
    

    print("Terminou!")