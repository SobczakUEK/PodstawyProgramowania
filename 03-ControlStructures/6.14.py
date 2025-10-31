# Influencer check
facebook = input('Facebook? (y/n): ') == 'y'
twitter = input('Twitter? (y/n): ') == 'y'
instagram = input('Instagram? (y/n): ') == 'y'
count = 0
if facebook:
    count += 1
if twitter:
    count += 1
if instagram:
    count += 1
if count >= 2:
    print('You are a good influencer!')
