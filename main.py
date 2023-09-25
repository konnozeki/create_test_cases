
def sales(age, height):
    returning = "" #1
    if age > 100 or age < 6 or height > 200 or height < 80: #2
        returning = "Đầu vào không hợp lệ"  #3
    else:
        if 6 <= age <= 17: #4
            returning += "Giảm giá 60%. " #5
        elif 18 <= age <= 25: # 6
            returning += "Giảm giá 30%. " #7
        if 80 <= height <= 150: # 8
            returning += "Mua 1 tặng 1" #9
        else: #10
            if returning == "": #11
                returning = "Không được giảm giá" #12
            #else: (13)
    return returning #14

