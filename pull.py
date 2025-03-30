from github import Github
import time
from datetime import datetime, timezone
import os
from colorama import init, Fore, Style  # Import colorama for text formatting


# Initialize colorama
init(autoreset=True)

end_time = 1742795220.6248822
start_time = end_time - 86400

ACCESS_TOKEN = open("token.txt", "r").read()
g = Github(ACCESS_TOKEN)
print(g.get_user())

query = "flask language:python created:2025-04-01..2024-04-02"
result = g.search_repositories(query)
# print(result.totalCount)

for i in range(1):
    try:
        start_time_str = datetime.fromtimestamp(start_time, timezone.utc).strftime('%Y-%m-%d')    
        end_time_str = datetime.fromtimestamp(end_time, timezone.utc).strftime('%Y-%m-%d')
        query = f"language:python created:{start_time_str}..{end_time_str}"
        print(query)
        end_time -= 86400
        start_time -= 86400

        result = g.search_repositories(query)
        print(result.totalCount)

        for repo in result:
            print(f"{repo.clone_url}")
            print(dir(repo))

            print(repo.owner.login)

            os.system(f"git clone {repo.clone_url} repos/{repo.owner.login}/{repo.name}")
            print(Fore.CYAN + Style.BRIGHT + f"current start time is {start_time}")

    except Exception as e:
        print(str(e))
        print(Fore.RED + Style.BRIGHT + "Broke for some reason...")
        time.sleep(120)

print("Finished, your new end time should be:", start_time)
