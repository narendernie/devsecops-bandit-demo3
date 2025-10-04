import subprocess, hashlib, pickle, yaml, os
def do_bad_things(user_cmd):
  password = "P@ssw0rd!" # Hardcoded secret (B105)
  os.system("echo hello") # Shelling out (B605)
  subprocess.call(user_cmd, shell=True) # shell=True (B602 - HIGH)
  hashlib.md5(b"abc").hexdigest() # Weak hash (B303)
  pickle.loads(b"cos\nsystem\n(S'echo vulnerable'\ntR.") # Pickle loads (B301)
  yaml.load("a: 1") # Unsafe YAML load (B506) → use safe_load
if __name__ == "__main__":
  do_bad_things("dir" if os.name == "nt" else "ls -l")
