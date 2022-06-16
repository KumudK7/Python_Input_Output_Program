
import argparse


if __name__ == '__main__':
    parser =argparse.ArgumentParser(description='Utility')
    parser.add_argument('-l',metavar='filename',help="Display no. of lines present in a file")
    parser.add_argument('-c',metavar='filename',help="Display no. of character present in a file")
    parser.add_argument('-w',metavar='filename',help="Display no. of words in a file")
    parser.add_argument('-n',metavar='filename',help="Display only numeric numbers in input file")
    parser.add_argument('-a',metavar='filename',help="Display only alphabets in input file")

    args = parser.parse_args()

    try:
        if args.l:
            with open(args.l, 'r') as fp:
                for count, line in enumerate(fp):
                    pass
            print('No. of lines present in a file: ', count + 1)
            
        elif args.c:
            with open(args.c, 'r') as fp:
                content = fp.read()
                count = 0
                for line in content:
                    if line.isalpha():
                        count += 1
                print('No. of characters present in file: ',count)

        elif args.n:
            with open(args.n, 'r') as fp:
                content = fp.read()
                nums=''
                for i in content:
                    if i.isnumeric():
                        nums+=i
                print('Only numeric numbers in file: ', nums)

        elif args.w:
            with open(args.w, 'r') as fp:
                content = fp.read()
                totalLines = content.split()
                number_of_words = len(totalLines)
                print('No. of words in a file: ', number_of_words)

        elif args.a:
            with open(args.a,'r') as fp:
                content = fp.read()
                val = ''
                for i in content:
                    if i.isalpha():
                        val+=i
                print('Only alphabets in input file: ',val)
    except (FileNotFoundError):
        print("File not found. Please provide valid filename")
    except:
        print("Something is wrong")



    


