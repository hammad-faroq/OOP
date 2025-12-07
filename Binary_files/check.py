# for i in range(4):
#     print(i)
#     for j in range(4,i+1,-1):
#         print("yes")
import struct
print("________________________________summary sheet____________________________________")
user=int(input("Enter :"))
if user==1:
    b1=5
    k=0
    nm1=0
    h1=[]
        # with open(file="data.txt",mode="rb") as file:

    course1 = ""
    for i1 in range(b1):
        file1 = open("data.txt", "rb")
        file1.seek(k)
        c4 = file1.readline(92)
                    # print(c4)
        print("yes")
        fo1 = "79s i f f"
        e4 = struct.unpack(fo1, c4)
        f4 = e4[0].decode("utf-8").split(" ")
        roll = f4[0]
        for i in f4[1:]:
            if i == "":
                pass
            else:
                h1.append(i)
        try:
            course1 = h1[4] + " " + h1[5]
        except:
            course1 = h1[4]
        else:
            try:
                course1 = h1[4] + " " + h1[5] + " " + h1[6]
            except:
                course1 = h1[4] + " " + h1[5]
            else:
                pass
        file1.close()
        m1 = []
        with open(file="data.txt", mode="rb+") as file1:
            for k1 in range(4,i1+1,-1):
                c3 = file1.readline(92)
                        # print(c4)
                        # print(c3)
                nm1+=92
                fo1 = "79s i f f"
                e3 = struct.unpack(fo1, c3)
                f3 = e3[0].decode("utf-8").split(" ")
                roll = f3[0]
                for i in f3[1:]:
                    if i == "":
                        pass
                    else:
                        m1.append(i)
                na = f"{m1[0]}{m1[1]}"
                course = ""
                try:
                    course = m1[4] + " " + m1[5]
                except:
                    course = m1[4]
                else:
                    try:
                        course = m1[4] + " " + m1[5] + " " + m1[6]
                    except:
                        course = m1[4] + " " + m1[5]
                    else:
                        pass
                m1.clear()
                if course == course1:
                    marks = str(round(e3[2], 2))
                    semes = str(e3[1])
                    l = ""
                    l += f"Name: {na} Roll: {roll}\nSemester :{semes} Marks :{marks}"
                    print(f"{l}\nCourse :{course}")
                    print()
        print("___________________________________________________")