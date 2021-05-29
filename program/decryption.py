def decryption(main_code):
    decryp_data=''
    string_main1='abcdefghijklmnopqrstuvwxyz'
    list1=[]
    list_num=['1','2','3','4','5','6','7','8']
    list_key=['?', '@', 'O', '73', 'P', '67', 'Q', '59', 'R', '53', 'S', '47', 'T', '41', 'U', '31', 'V', '23', 'W',
                '17', 'Y', '11', 'X', '05', 'Z', '02']

    for i in range(len(main_code)):
        if main_code[i] in list_num:
            for j in range(len(list_key)):
               if main_code[i:(i+2)]==list_key[j]:
                   list1.append(string_main1[j])
                   i=i+1
                   break

        elif main_code[i]=="#":
            list1.append(' ')

        elif main_code[i] not in list_num and main_code[i]!=" ":
            for k in range(len(list_key)):
                if main_code[i]==list_key[k]:
                    list1.append(string_main1[k])
                    break
    for r in range(len(list1)):
        decryp_data=decryp_data+list1[r]

    print('your original data for this code is:',decryp_data)

code=input("enter the code to get original data:")
decryption(code)
