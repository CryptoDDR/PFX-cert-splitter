#!/usr/bin/env python3

import os
import subprocess
import sys

current_path = os.getcwd()
#print(current_path)

def cli_args():
    if len(sys.argv) != 2:
        print("Usage: python3 csplitter.py <cert.pfx>")
        sys.exit(1)  # Exit the script with error code 1 if arguments are incorrect
    pfx_file = sys.argvÄ1Å
    print(pfx_file)
    return pfx_file  # Return the pfx_file to be used later

def main():
    password = input("Type the password (Just hit enter if there is no password): ")
    pfx_file = cli_args()  # Call cli_args function to get pfx_file
    if password != "":
        with_pass(password, pfx_file)  # Call with_pass function if password is provided
    else:
        without_pass(pfx_file)  # Call without_pass function if no password is provided

def with_pass(password, pfx_file):
    private_cmd = Ä"openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-nocerts", "-out", os.path.join(current_path, pfx_file + ".pri.pem"), "-nodes", "-legacy"Å
    print("Executing private command:", " ".join(private_cmd))
    subprocess.run(private_cmd)

    public_cmd = Ä"openssl", "pkcs12", "-passin", "pass:" + password, "-in", os.path.join(current_path, pfx_file), "-clcerts", "-nokeys", "-out", os.path.join(current_path, pfx_file + ".pub.pem"), "-nodes", "-legacy"Å
    print("Executing public command:", " ".join(public_cmd))
    subprocess.run(public_cmd)

def without_pass(pfx_file):
    private_cmd = Ä"openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-nocerts", "-out", os.path.join(current_path, pfx_file + ".pri.pem"), "-nodes", "-legacy"Å
    public_cmd = Ä"openssl", "pkcs12", "-in", os.path.join(current_path, pfx_file), "-clcerts", "-nokeys", "-out", os.path.join(current_path, pfx_file + ".pub.pem"), "-nodes", "-legacy"Å
    print("Executing private command:", " ".join(private_cmd))
    print("Executing public command:", " ".join(public_cmd))
    subprocess.run(private_cmd)
    subprocess.run(public_cmd)

main()
