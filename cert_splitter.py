#!/usr/bin/env python3

import os
import subprocess
import sys
#print(DDR_Encoded)

current_path = os.getcwd()
#print(current_path)

def cli_args():
    if len(sys.argv) != 2:
        print("Usage: python3 csplitter.py <cert.pfx>")
        sys.exit(1)  
    pfx_file = sys.argv[1]
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
    private_cmd = ["openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-nocerts", "-out", os.path.join(current_path, pfx_file + ".pri.pem"), "-nodes", "-legacy"]
    #print("Executing private command:", " ".join(private_cmd))
    subprocess.run(" ".join(private_cmd), shell=True)

    public_cmd = ["openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-clcerts", "-nokeys", "-out", os.path.join(current_path, pfx_file + ".pub.pem"), "-nodes", "-legacy"]
    #print("Executing public command:", " ".join(public_cmd))
    subprocess.run(" ".join(public_cmd), shell=True)
    
    cert_cmd = ["openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-nokeys", "-out", os.path.join(current_path, pfx_file + ".crt"), "-nodes", "-legacy"]
    subprocess.run(" ".join(cert_cmd), shell=True)


def without_pass(pfx_file):
    private_cmd = ["openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-nocerts", "-out", os.path.join(current_path, pfx_file + ".pri.pem"), "-nodes", "-legacy"]
    public_cmd = ["openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-clcerts", "-nokeys", "-out", os.path.join(current_path, pfx_file + ".pub.pem"), "-nodes", "-legacy"]
    cert_cmd = ["openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-nokeys", "-out", os.path.join(current_path, pfx_file + ".crt"), "-nodes", "-legacy"]
    #print("Executing private command without pass:", " ".join(private_cmd))
    #print("Executing public command without pass:", " ".join(public_cmd))
    subprocess.run(" ".join(private_cmd), shell=True)
    subprocess.run(" ".join(public_cmd), shell=True)
    subprocess.run(" ".join(cert_cmd), shell=True)

main()
