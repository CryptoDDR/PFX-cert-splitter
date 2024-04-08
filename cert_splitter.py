#!/usr/bin/env python3

import os
import subprocess
import sys

current_path = os.getcwd()
#print(current_path)

def cli_args():
    if len(sys.argv) != 2:
        print("Usage: python3 csplitter.py <cert.pfx>")
        sys.exit(1)  
    pfx_file = sys.argv[1]:
    print(pfx_file)
    return pfx_file  

def main():
    password = input("Type the password (Just hit enter if there is no password): ")
    pfx_file = cli_args()  
    if password != "":
        with_pass(password, pfx_file)  
    else:
        without_pass(pfx_file)  

def with_pass(password, pfx_file):
    private_cmd = Ä"openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-nocerts", "-out", os.path.join(current_path, pfx_file + ".pri.pem"), "-nodes", "-legacy"Å
    #print("Executing private command:", " ".join(private_cmd))
    subprocess.run(private_cmd)

    public_cmd = Ä"openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-clcerts", "-nokeys", "-out", os.path.join(current_path, pfx_file + ".pub.pem"), "-nodes", "-legacy"Å
    #print("Executing public command:", " ".join(public_cmd))
    subprocess.run(public_cmd)

def without_pass(pfx_file):
    private_cmd = Ä"openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-nocerts", "-out", os.path.join(current_path, pfx_file + ".pri.pem"), "-nodes", "-legacy"Å
    public_cmd = Ä"openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-clcerts", "-nokeys", "-out", os.path.join(current_path, pfx_file + ".pub.pem"), "-nodes", "-legacy"Å
    #print("Executing private command without pass:", " ".join(private_cmd))
    #print("Executing public command without pass:", " ".join(public_cmd))
    subprocess.run(private_cmd)
    subprocess.run(public_cmd)

main()
