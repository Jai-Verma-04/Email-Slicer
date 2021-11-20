
def main():
    mail = input('Enter your email id: ')
    j=0
    once = 0
    for i in mail:
        j+=1
        if i.isspace():
            print("No spaces allowed in E-Mail")
            main()
        else:
            if i=='@':
                once+=1
                if once==1:
                    print('Username:', mail[:j-1])
                    print('Domain Name:', mail[j:])
                if once!=1:
                    print("Invalid Email")
              
            if '@' not in mail:
                print('Invalid Email')
                main()
main()
        
