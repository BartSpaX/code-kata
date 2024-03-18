def recite(start_verse, end_verse):
    days_and_presents = {
        0: ['first', 'a Partridge in a Pear Tree'],
        1: ['second', 'two Turtle Doves, and a Partridge in a Pear Tree'],
        2: ['third', 'three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        3: ['fourth', 'four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        4: ['fifth', 'five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        5: ['sixth', 'six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        6: ['seventh', 'seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        7: ['eighth', 'eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        8: ['ninth', 'nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        9: ['tenth', 'ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        10: ['eleventh', 'eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree'],
        11: ['twelfth', 'twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree']
    }
    verses = []
    for i in range(start_verse-1, end_verse):
        verses.append(f'On the {days_and_presents[i][0]} day of Christmas my true love gave to me: {days_and_presents[i][1]}.')
    return verses