def read_log(filepath):
    with open(filepath,"r") as f:
        lines = f.readlines()
    return lines
        
def main():
    lines = read_log('build.log')
    d={"ERROR":0,"INFO":0,"WARNING":0}
    cnt=0
    for line in lines:
        line = line.strip()
        if "ERROR" in line:
            d["ERROR"]+=1
            print(line)
            cnt+=1
        elif "INFO" in line:
            d["INFO"]+=1
        elif "WARNING" in line:
            d["WARNING"]+=1
            
    print("Found",cnt, "errors.")
    for k, v in d.items():
        print(k,":",v)
main()