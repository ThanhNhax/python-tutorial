print('Hello World!')
# Kiểu dữ liệu
name ='Nguyễn Thanh Nhã'
print(type(name))

age = 24
print(type(age))
point = 8.9
print(type(point))

option = [1,2,3,4,5]
print(type(option))

isTuple = ('nguyễn Thanh nhã', 24, True)
print(isTuple[2])

dictionary = {
    "name": "Nguyễn Thị Thủy Tiên",
    "name":'Nguyễn Thanh Nhã',
    "age": 23,
    'male': True,
}
dictionary.clear()
print (dictionary)

# kiểu dữ liệu của python:
# *   int: số nguyên
# *   float: số thực(số thập phân)
# *   string: chuỗi
# *   tuple: (kiểu dữ liệu) : giống như truyền tham số cho contructor trong class js
# *   dictionary: là kiểu object 


if (age<18):
    print('Chưa đủ tuổi!')
else:
    print('Đủ tuổi rồi nhé!')
    if(age<25):
        print('Còn trong tuổi phát triển tốt %d!'  %age)


#  kieu swtich-case thong qua kie du lieu dictionary

a= 'bon'
dic = {
    'hai':2,
    'mot':1,
    'ba':3
}

doc = dic.get(a,'khong co')

print(doc)

#  Hàm nhận dữ liệu từ người dùng 
print('Hello guy!')
new_age = input('How old are you? \n')
print('age:' + new_age)

# # mo file o che do ghi
# file  = open('readme.md','w')

# # ghi file
# file.write('Nguyen Thanh Nha - thanhnha.k13@gmail.com')


# # dong file
# file.close()
file = open('readme.md',"r")
# doc file
data = file.read()
file.close()
print(data)