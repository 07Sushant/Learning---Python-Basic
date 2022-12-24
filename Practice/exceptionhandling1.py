try:
    f = open("demo.py")
    try:
        f.write("Sushant")
    except:
        print("Error in file")
    
    finally:
        f.close()

except:
    print("Error in file")