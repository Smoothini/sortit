import shutil, datetime, yaml, os

root = "C:/users/home/downloads"
new_root = f"{root}/_sorted"
config_location = f"{root}/_sorted/moves.yaml"
log_location = f"{root}/_sorted/moves.log"


def logit(msg):
    timestamp = datetime.datetime.now()
    with open(log_location, 'a') as log:
        log.write(f"{timestamp}   {msg}\n")
        
def movit(item, destination):
    try:
        src = os.path.join(root, item)
        dest_dir = os.path.join(new_root, destination)
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, item)
        shutil.move(src, dest)
        #print(f"Moved '{src}' to '{dest}' successfully.")
        logit(f"Moved '{src}' to '{dest}' successfully.")
        return True
    except FileNotFoundError:
        print(f"{src} was not found.")
        logit(f"{src} was not found.")
    except PermissionError:
        print("Permission denied.")
        logit("Permission denied.")
    except UnicodeEncodeError:
        print("Filename issues")
        logit("Filename issue")
    except Exception as e:
        print("Another error occured: ", e)
        logit("Another error occured: ", e)

def findit(ext, config):
    for item in config['include'].keys():
        if ext.lower() in config['include'][item]:
            return item
    return None
    

def sortit():
    logit("Initializing sorting")
    count = 0

    try:
        config_file = open(config_location, 'r')
        config = yaml.safe_load(config_file)
    except Exception as e:
        print("Error occured loading the configuration: ", e)
        logit(f"Error occured loading the configuration: {e}")

    for item in os.listdir(root):
        itempath = os.path.join(root, item)

        if item not in config["exclude"]["files"]:
        
            if os.path.isfile(itempath):
                filename, extension = os.path.splitext(item)
                ext = extension[1:]
                
                destination = findit(ext, config)

                if destination:
                    if movit(item, destination):
                        count+=1
                else:
                    print("No config for extension ", ext)
                    logit(f"No config for extension {ext}")
        
        else:
            print("Excluded ", item)
            logit(f"Excluded {item}")
    if count:
        print(f"Successfully sorted {count} files")
        logit(f"Successfully sorted {count} files")
    else:
        print("Nothing to sort yay")
        logit("Nothing to sort yay")
    

sortit()
