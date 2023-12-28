from datetime import datetime

def get_zodiac_info(birthdate_str):
    try:
        # Parse the input birthdate string into a datetime object
        birthdate = datetime.strptime(birthdate_str, "%m/%d/%Y")
        
        # Validate leap year
        if birthdate.month == 2 and birthdate.day == 29 and not (birthdate.year % 4 == 0 and (birthdate.year % 100 != 0 or birthdate.year % 400 == 0)):
            return "Invalid birthdate (not a leap year)."

        # Validate the date range
        min_date = datetime(1800, 1, 1)
        max_date = datetime(2100, 12, 31)
        if not (min_date <= birthdate <= max_date):
            return "Invalid birthdate (out of range)."

        # Determine the zodiac sign based on the birthdate
        if (3, 21) <= (birthdate.month, birthdate.day) <= (4, 19):
            return "Aries - You'll discover hidden talents and skills within yourself this month!" \
                   "\nLucky Numbers: 7, 12, 21\nLucky Color: Red\nPersonality Traits: Energetic, Courageous, Spontaneous" \
                   "\nFamous Aries: Lady Gaga, Leonardo da Vinci, Elton John"
        elif (4, 20) <= (birthdate.month, birthdate.day) <= (5, 20):
            return "Taurus - Unexpected financial gains are coming your way. Be prepared!" \
                   "\nLucky Numbers: 2, 6, 15\nLucky Color: Green\nPersonality Traits: Reliable, Patient, Practical" \
                   "\nFamous Taurus: Adele, William Shakespeare, Audrey Hepburn"
        elif (5, 21) <= (birthdate.month, birthdate.day) <= (6, 20):
            return "Gemini - A surprise adventure is on the horizon. Embrace the unexpected!" \
                   "\nLucky Numbers: 5, 11, 23\nLucky Color: Yellow\nPersonality Traits: Adaptable, Curious, Witty" \
                   "\nFamous Gemini: Angelina Jolie, Johnny Depp, Kanye West"
        elif (6, 21) <= (birthdate.month, birthdate.day) <= (7, 22):
            return "Cancer - Your positive energy will attract good fortune. Stay optimistic!" \
                   "\nLucky Numbers: 3, 9, 17\nLucky Color: Silver\nPersonality Traits: Nurturing, Intuitive, Protective" \
                   "\nFamous Cancer: Princess Diana, Tom Hanks, Elon Musk"
        elif (7, 23) <= (birthdate.month, birthdate.day) <= (8, 22):
            return "Leo - An old friend will reappear in your life, bringing joy and nostalgia!" \
                   "\nLucky Numbers: 1, 8, 22\nLucky Color: Gold\nPersonality Traits: Charismatic, Confident, Creative" \
                   "\nFamous Leo: Barack Obama, Jennifer Lopez, Mick Jagger"
        elif (8, 23) <= (birthdate.month, birthdate.day) <= (9, 22):
            return "Virgo - A long-standing goal will finally be achieved. Celebrate your success!" \
                   "\nLucky Numbers: 4, 10, 24\nLucky Color: Green\nPersonality Traits: Detail-Oriented, Practical, Analytical" \
                   "\nFamous Virgo: Beyoncé, Mother Teresa, Tim Burton"
        elif (9, 23) <= (birthdate.month, birthdate.day) <= (10, 22):
            return "Libra - A new love interest will enter your life. Keep an open heart!" \
                   "\nLucky Numbers: 6, 15, 21\nLucky Color: Blue\nPersonality Traits: Charming, Diplomatic, Social" \
                   "\nFamous Libra: Mahatma Gandhi, Kim Kardashian, Will Smith"
        elif (10, 23) <= (birthdate.month, birthdate.day) <= (11, 21):
            return "Scorpio - Your creativity will reach new heights. Express yourself boldly!" \
                   "\nLucky Numbers: 9, 18, 27\nLucky Color: Black\nPersonality Traits: Intense, Ambitious, Resourceful" \
                   "\nFamous Scorpio: Leonardo DiCaprio, Marie Curie, Bill Gates"
        elif (11, 22) <= (birthdate.month, birthdate.day) <= (12, 21):
            return "Sagittarius - Travel plans will unexpectedly fall into place. Pack your bags!" \
                   "\nLucky Numbers: 3, 12, 21\nLucky Color: Purple\nPersonality Traits: Optimistic, Adventurous, Independent" \
                   "\nFamous Sagittarius: Walt Disney, Taylor Swift, Brad Pitt"
        elif (12, 22) <= (birthdate.month, birthdate.day) or (1, 1) <= (birthdate.month, birthdate.day) <= (1, 19):
            return "Capricorn - Stay cautious while traveling. Avoid unnecessary risks." \
                   "\nLucky Numbers: 4, 8, 22\nLucky Color: Brown\nPersonality Traits: Disciplined, Ambitious, Practical" \
                   "\nFamous Capricorn: Michelle Obama, Elvis Presley, Steve Jobs"
        elif (1, 20) <= (birthdate.month, birthdate.day) <= (2, 18):
            return "Aquarius - Financial opportunities are coming your way. Be ready to seize them!" \
                   "\nLucky Numbers: 5, 15, 23\nLucky Color: Aqua\nPersonality Traits: Innovative, Humanitarian, Eccentric" \
                   "\nFamous Aquarius: Oprah Winfrey, Abraham Lincoln, Ellen DeGeneres"
        elif (2, 19) <= (birthdate.month, birthdate.day) <= (3, 20):
            return "Pisces - A serendipitous encounter will lead to new and meaningful connections." \
                   "\nLucky Numbers: 7, 12, 18\nLucky Color: Sea Green\nPersonality Traits: Compassionate, Imaginative, Intuitive" \
                   "\nFamous Pisces: Rihanna, Albert Einstein, Kurt Cobain"

        # Handle special cases or edge cases as needed

        # If the birthdate is in the future
        if birthdate > datetime.now():
            return "Birthdate is in the future."

        # For all other cases, return an error message
        return "Unable to determine zodiac sign."

    except ValueError:
        return "Invalid date format. Please use MM/DD/YYYY."

# Example usage:
birthdate_input = input("Enter your birthdate (MM/DD/YYYY): ")
zodiac_info = get_zodiac_info(birthdate_input)
print("Zodiac Info:", zodiac_info)
