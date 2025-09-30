from math import factorial
from decimal import Decimal, getcontext
print("Pistributed, an app to calculate Pi with distributed power.")
print("Do not run on systems owned by another entity, entities, person, or people, without explicit permission from them.")
print("""This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.""")
print("By continuing, you agree to these terms, disclaimers, and acknowledge that there is NO WARRANTY.")
input("I agree, and would like to continue. (to continue, press enter)")
print("Thanks for confirming! I just need one more thing.")
server = input("What is the server URL that you'd like to connect to? (ex: example.com) ")
print("Alright! Thanks. Let the calculating begin :D (to exit, run ctrl+c or close terminal)")
print("-------------------")
getcontext().prec=100
def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)
    k = 0
    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)                                   
    pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return pi
print(calc(100))