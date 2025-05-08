import requests
import hashlib
import sys

def get_hashed(password):
    # Hash the password using SHA-1 (required by the API)
    hashed = hashlib.sha1(password.encode()).hexdigest().upper()
    head, tail = hashed[:5], hashed[5:]
    return head, tail

def get_pwned_count(head, tail):
    url = f'https://api.pwnedpasswords.com/range/{head}'
    res = requests.get(url)
    
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}, check the API and try again.")

    # Split response into lines and check for match
    lines = res.text.splitlines()
    for line in lines:
        line_tail, pwned_count = line.split(':')
        if line_tail == tail:  # Compare uppercase tail
            return int(pwned_count)
    return 0

def main(args):
    for password in args:
        head, tail = get_hashed(password)
        pwned_count = get_pwned_count(head, tail)
        if pwned_count == 0:
            print(f"'{password}' has never been pwned.")
        else:
            print(f"'{password}' has been pwned {pwned_count} times.")
    return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))