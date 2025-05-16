#secret language
message = input("Enter the message: ")
print("The original message is:", message)
words = message.split(" ")

#encoding
nwords = []
for word in words:
  if len(word) >= 3:
     encoded_word = "abc" + word[1:] + word[0] + "xyz"
     nwords.append(encoded_word)
  else:
     nwords.append(word[::-1])
encoded_message = " ".join(nwords)
print("The encoded message is:", encoded_message)

#decoding
decoded_words = []
for word in nwords:
  if len(word) <= 2:
     decoded_words.append(word[::-1])
  else:
     decoded_word = word[3:-3]
     decoded_word = decoded_word[-1] + decoded_word[:-1]
     decoded_words.append(decoded_word)
decoded_message = " ".join(decoded_words)
print("The decoded message is:", decoded_message)