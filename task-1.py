def transformed_text(input_text):
    text=input_text
    
    # RULE 1: Replace the word "star" (exact case) with a star emoji "⭐".
    text = text.replace("star", "⭐")

    # RULE 2: Convert each digit character into its word form.
    digits = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", 
              "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
    result = ""
    for ch in text:
        if ch in digits:
            result = result + digits[ch]
        else:
            result = result + ch
    text=result

    #Rule 3: Add 📢 around fully capitalized words, to imply they're "SHOUTED"
    words = text.split()   
    result_words = []

    for w in words:
        if w.isupper() and len(w)>1:                                  # checking if the word is ALL CAPS
            result_words.append("📢" + w + "📢")
        else:
            result_words.append(w)

    text = " ".join(result_words)  

    return text   # final output

print(transformed_text("I just saw player 452 score 5 GOALS UNDER 5 MINS like a superstar!"))