def prompt(sys_prompt, answers):
  ans = input("> EMODJI: " + sys_prompt + " (" + '/'.join(answers) + ")\n> You: ")

  while ans not in answers:
    print("> EMOODJI: Sorry, I don't understand.")
    ans = input("> EMODJI: " + sys_prompt + " (" + '/'.join(answers) + ")\n> You: ")
  return ans
'''
Prompts the user with questions and accepts user input
'''
def user_input():
  res = []
  is_laughing = ""
  is_sad = ""
  is_sure = ""
  is_happy = ""

  # Greeting
  print(
    "> EMOODJI: Hello! I am Emoodji!\n" 
    "> EMOODJI: I am a command line application that matches an emoji to how you're feeling."
  )

  q1 = "Is it okay if I ask you a few questions?"
  answers1 = ["Yes", "No"]
  start = prompt(q1, answers1)
  if start == "No":
    return "NONE"

  q2 = "Are you laughing?"
  answers2 = ["Yes", "No"]
  is_laughing = prompt(q2, answers2)

  q3 = "Are you feeling sad?"
  answers3 = ["Yes", "No"]
  is_sad = prompt(q3, answers3)

  if is_sad == "No":
    q4 = "Are you sure?"
    answers4 = ["Yes", "No"]
    is_sure = prompt(q4, answers4)

    if is_sure == "Yes":
      if is_laughing == "Yes":
        return "LAUGHING"
      else:
        return "NEUTRAL"
  if is_laughing == "Yes":
    return "CONFUSED"
  return "SAD"
  

def determine_emoji(emotion):
  res = "> EMOODJI: This is literally you: "
  if emotion == "LAUGHING":
    res += "\N{rolling on the floor laughing}"
  elif emotion == "SAD":
    res += "\N{pensive face}"
  elif emotion == "NEUTRAL":
    res += "\N{neutral face} (sorry, you're hard to read!)"
  elif emotion == "CONFUSED":
    res += "\N{smiling face with tear}"

  # grinning face
  return res

if __name__ == "__main__":
  print("> Starting Emoodji...")
  emotion = user_input()
  
  if emotion == "NONE":
    print("> EMOODJI: \N{expressionless face} Bye then.")
  else:
    print("> EMOODJI: I think I know how you feel...")
    print(determine_emoji(emotion))