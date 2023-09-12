import random
import string

def generate_random_domain():
    domain_length = random.randint(5, 20)
    domain_name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(domain_length))
    tld = random.choice(["com", "org", "net", "io", "co", "app", "tech", "xyz", "info"])
    return f"{domain_name}.{tld}"

# the number of domain names to generate
num_domains = 700000

# Generate domain names and save them to a text file
with open(f"{num_domains}_domains.txt", "w") as file:
    for _ in range(num_domains):
        domain = generate_random_domain()
        file.write(domain + "\n")

print(f"{num_domains} domain names generated and saved to '{num_domains}_domains.txt'.")