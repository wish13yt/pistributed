from math import factorial
from decimal import Decimal, getcontext
import time
import threading
import requests
import sys

print("Pistributed, an app to calculate Pi with distributed power.")
print("Do not run on systems owned by another entity, entities, person, or people, without explicit permission from them.")
print("""This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.""")
print("By continuing, you agree to these terms, disclaimers, and acknowledge that there is NO WARRANTY.")
input("I agree, and would like to continue. (to continue, press enter) ")
print("Thanks for confirming! I just need one more thing.")
print("Make sure you trust the server! I do not control any of them and am not responsible for anything on external websites and/or servers.")
server = input("What is the server URL that you'd like to connect to? (ex: https://example.com, http://localhost:5000) ")
print("Alright! Thanks. Let the calculating begin :D (to exit, run ctrl+c or close terminal)")
print("-------------------")
global pi_val
pi_val = None
try:
    def calc(n, prec):
        getcontext().prec = prec
        t = Decimal(0)
        pi = Decimal(0)
        deno = Decimal(0)
        for k in range(n):
            t = ((-1)**k) * (factorial(6*k)) * (13591409 + 545140134*k)
            deno = factorial(3*k) * (factorial(k)**3) * (640320**(3*k))
            pi += Decimal(t) / Decimal(deno)
        pi = pi * Decimal(12) / Decimal(640320**Decimal(1.5))
        pi = 1/pi
        return pi

    def upload():
        while True:
            if str(pi_val).startswith("3.14") == True:
                print(">> checking and uploading latest calculation")
                response = requests.get(server + "/api/getpi")
                print(response.text)
                replen = len(response.text)
                pilen = len(str(pi_val))
                if response.text == "No clients have connected yet. Become one of the first!":
                    print("server pi doesn't exist! uploading")
                    data = {'pi': str(pi_val)}
                    print(data)
                    response = requests.post(server + "/api/postpi", data=data)
                    print(response.text)
                else:
                    if replen > pilen:
                        print("server pi length is greater than local pi length! not uploading")
                    elif pilen > replen:
                        print("local pi length longer than server pi length! uploading")
                        data = {'pi': str(pi_val)}
                        response = requests.post(server + "/api/postpi", data=data)
                        print(response.text)
            else:
                print("pi_val not yet defined!")
            time.sleep(60)

    threading.Thread(target=upload, daemon=True).start()

    calculation = 1
    precision = 10

    while True:
        pi_val = calc(calculation, precision)
        print(pi_val)
        calculation += 1
        precision += 5
        time.sleep(5)
except:
    try:
        print("Saving your latest Pi to Pi.txt and exiting...")
        with open("pi.txt", "w") as f:
            f.write(str(pi_val))
        sys.exit()
    except:
        print("Unable to save to pi.txt. This could be because pi_val wasn't defined yet. Exiting..")
        sys.exit()