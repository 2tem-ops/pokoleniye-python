words = ['summer', 'city', 'Earth', 'peace', 'kindness', 'Dog', 'turtle']

print(*sorted({i[0].lower() for i in words}))