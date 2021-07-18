
def prime(z):
    if z>1:
        for k in range(2, z):
            if z%k==0:
                return False
            break
        else:
            return True
    else:
        return False
def breaking(x):
    string1='NMolPKqjRIshTGufVEwdYCxbZA'
    string2='!@#$%^&*()_+-={}[]|\:;<>/~'
    string3=['87','83','79','73','71','67','61','59','57','53','51','47','43','41','37','31','29','23','19','17','13','11','07','05','03','02']
    if prime(x):
        return string2[x-1]
    elif x%2!=0 and x!=1:
        return string1[x-1]
    elif x%2==0:
        return string3[x-1]
    elif x==1:
        return '?'
def encryption(data):
    codex=[]
    encryp_data=''
    string_main1='abcdefghijklmnopqrstuvwxyz'
    string_main2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(data)):
        if data[i]!=" ":
            for j in range(26):
                if data[i]==string_main1[j]:
                    codex.append(str.upper(breaking(j+1)))
                elif data[i]==string_main2[j]:
                    codex.append(str.lower(breaking(j+1)))
        else:
            codex.append('#')
    for i in range(len(codex)):
        encryp_data=encryp_data+codex[i]
    print("technoreck's code for your data is:",encryp_data)

your_data=input("enter a sentence only of alphabets:")

encryption(your_data)
