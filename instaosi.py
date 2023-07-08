import instaloader, sys , os , time , subprocess
from colorama import Fore , Back , Style

#showcase ;)
os.system("clear")

time.sleep(3)
print(Fore.GREEN , "Please Wait...")
print("Bot Attempting Login")
print("")
print("")

# Open the file
with open('credentials.txt', 'r') as f:
  # Read the contents of the file
  contents = f.read()
# Split the contents into a list of lines
lines = contents.splitlines()
# Get the username and password from the first two lines
username = lines[0]
password = lines[1]

x = instaloader.Instaloader()

# Login Interface 
try:
	uname = username
	passwd = password

	x.login(uname,passwd)
	print("Login successful...")

except:
	print("Login failed!")
	sys.exit()


# Target Username

time.sleep(3)
os.system("clear")
time.sleep(2)
print("")
print(" ┏━━┓╋╋╋╋╋┏┓╋╋╋┏━━━┳━━━┳━━┓")
time.sleep(0.1)
print(" ┗┫┣┛╋╋╋╋┏┛┗┓╋╋┃┏━┓┃┏━┓┣┫┣┛")
time.sleep(0.1)
print(" ╋┃┃┏━┓┏━┻┓┏╋━━┫┃╋┃┃┗━━┓┃┃")
time.sleep(0.1)
print(" ╋┃┃┃┏┓┫━━┫┃┃┏┓┃┃╋┃┣━━┓┃┃┃")
time.sleep(0.1)
print(" ┏┫┣┫┃┃┣━━┃┗┫┏┓┃┗━┛┃┗━┛┣┫┣┓")
time.sleep(0.1)
print(" ┗━━┻┛┗┻━━┻━┻┛┗┻━━━┻━━━┻━━┛")
print("")
print("")
print("[~]  GɪᴛHᴜʙ : TɴYᴛCᴏᴅᴇʀ")
print("[~]  IɴsᴛᴀOsɪ A Pʏᴛʜᴏɴ Bᴀsᴇᴅ Osɪɴᴛ Tᴏᴏʟ")
print("")
time.sleep(3)

username = input("[≥]  Eɴᴛᴇʀ Tᴀʀɢᴇᴛ Usᴇʀɴᴀᴍᴇ :  ")
if username == "":
	print("Usᴇʀ Nᴏᴛ Fᴏᴜɴᴅ")
	sys.exit()


y = instaloader.Profile.from_username(x.context, username)

print("")
print("")
print("Exᴛʀᴀᴄᴛɪɴɢ Tʜᴇ Usᴇʀ Dᴇᴛᴀɪʟs...")
time.sleep(1)
print("")
print(Fore.LIGHTBLUE_EX , "[≥]  Username : ",y.username)
print("[≥]  ID : ",y.userid)
print("[≥]  Name : ",y.full_name)
print("[≥]  Verified : ",y.is_verified)
print("[≥]  Privacy : ",y.is_private)
print("[≥]  Business account : ",y.is_business_account)
print("[≥]  Business category name : ",y.business_category_name)
print("[≥]  Bio : ",y.biography)
print("[≥]  Followers : ",y.followers)
print("[≥]  Following : ",y.followees)
print("[≥]  Profile Pic Url : ",y.profile_pic_url)
print("[≥]  External Url : ",y.external_url)
print("[≥]  Media Account : \33[0m",y.mediacount)
print(Fore.LIGHTBLUE_EX , "[≥]  IGTV : ",y.igtvcount)
print("[≥]  Has a story to watch : ",y.has_viewable_story)
print("[≥]  Has Public Story : ",y.has_public_story)
print("[≥]  Has Highlight Reels : ",y.has_highlight_reels)
print("[≥]  Followed By User : ",y.followed_by_viewer)
print("[≥]  Follows Viewer : ",y.follows_viewer)
print("[≥]  Blocked By Viewer : ",y.blocked_by_viewer)
print("[≥]  Has Blocked Viewer : ",y.has_blocked_viewer)
print("[≥]  requested_by_viewer : ",y.requested_by_viewer)
print("[≥]  has_requested_viewer : ",y.has_requested_viewer)
print("")
print("")
print(Fore.YELLOW , "Tʜᴀɴᴋ Yᴏᴜ Fᴏʀ Usɪɴɢ !!!")
time.sleep(1)
print("")
print(Fore.RED , "Exɪᴛɪɴɢ...")
print("")
# Saving The Info Into The File
target = "Username : " , y.username
uid = "Id : " , y.userid
name = "Name : " , y.full_name
bio = "Bio : " , y.biography
followers = "Followers : " , y.followers
following = "Following : " , y.followees
profile_pic_url = "Profile_Pic_Url : " , y.profile_pic_url

foldername = y.username
os.system("mkdir {}".format(foldername))

lines = [str(target) , str(uid) , str(name) , str(bio) ,  str(followers) , str(following) , str(profile_pic_url)]

with open("userlogs.txt", 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# Subprocess Most Iritating =)

bfile = open("run.sh" , "w")
bfile.write("mv userlogs.txt " + str(foldername))
bfile.close()

# Runing That file

os.system("bash run.sh")

# Removing That File

os.remove("run.sh")

time.sleep(3)
