import tkinter as tk
from tkinter import StringVar, ttk
import string as s
from random import *

ch = s.ascii_letters+s.digits+s.punctuation
password = "".join(choice(ch)for j in range(randint(8, 18)))
print(password)
