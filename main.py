#github/hanzdev

from src import banner
import sys
import argparse, subprocess
import hashlib
from colorama import Fore

if __name__ == "__main__":

  parser = argparse.ArgumentParser()
  parser.add_argument('--type', help="set algorithm type", required=True, \
                                     choices=["md5", "sha1", "sha224", "sha256", "sha384", "sha512"])
  parser.add_argument('--text', help="input your text", dest='text', required=False)
  args = parser.parse_args()

  tt = str((args.text))

  def md5_en():
    ressha1 = hashlib.sha1(tt.encode())
    print(Fore.RED + f"({tt})" + Fore.GREEN + " MD5 output => ", end='')
    print(ressha1.hexdigest())
    print("")

  def sha1_en():
    ressha1 = hashlib.sha1(tt.encode())
    print(Fore.RED + f"({tt})" + Fore.GREEN + " SHA1 output => ", end='')
    print(ressha1.hexdigest())

  def sha224_en():
    ressha256 = hashlib.sha256(tt.encode())
    print(Fore.RED + f"({tt})" + Fore.GREEN + " SHA224 output => ", end='')
    print(ressha256.hexdigest())

  def sha256_en():
    ressha256 = hashlib.sha256(tt.encode())
    print(Fore.RED + f"({tt})" + Fore.GREEN + " SHA256 output => ", end='')
    print(ressha256.hexdigest())

  def sha384_en():
    ressha256 = hashlib.sha256(tt.encode())
    print(Fore.RED + f"({tt})" + Fore.GREEN + " SHA384 output => ", end='')
    print(ressha256.hexdigest())

  def sha512_en():
    ressha256 = hashlib.sha256(tt.encode())
    print(Fore.RED + f"({tt})" + Fore.GREEN + " SHA512 output => ", end='')
    print(ressha256.hexdigest())

  if args.type == "md5":
    md5_en()
  elif args.type == "sha1":
    sha1_en()
  elif args.type == "sha224":
    sha224_en()
  elif args.type == "sha256":
    sha256_en()
  elif args.type == "sha384":
    sha384_en()
  elif args.type == "sha512":
    sha512_en()
  else:
    print("Invalid value.")