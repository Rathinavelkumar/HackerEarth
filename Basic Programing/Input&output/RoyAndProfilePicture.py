length = int(input())
photos_count = int(input())

for each_photo in range(0, photos_count):
    width, height = map(int, input().split(" "))
    if width==length and height==length:
        print("ACCEPTED")
    elif width<length or height<length:
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")