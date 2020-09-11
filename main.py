# Author: Jasmine Sandhu jps6818@psu.edu

def getGradePoint(grade):
  if (grade == "A"):
    return 4.0 
  elif (grade == "A-"):
    return 3.67 
  elif (grade == "B+"):
    return 3.33
  elif (grade == "B"):
    return 3.0
  elif (grade == "B-"):
    return 2.67
  elif (grade == "C+"):
    return 2.33
  elif (grade == "C"):
    return 2.0
  elif (grade == "D"):
    return 1.0
  else:
    return 0.0

def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = float(input("Enter your course 1 credit: "))
  grade1 = getGradePoint(grade1)
  print(f"Grade point for course 1 is: {grade1}") 

  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = float(input("Enter your course 2 credit: "))
  grade2 = getGradePoint(grade2)
  print(f"Grade point for course 2 is: {grade2}")

  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = float(input("Enter your course 3 credit: "))
  grade3 = getGradePoint(grade3)
  print(f"Grade point for course 3 is: {grade3}")

  GPA = (grade1 * credit1 + grade2 * credit2 + grade3 * credit3) / (credit1 + credit2 + credit3) 
  print(f"Your GPA is: {GPA}") 

if __name__ == "__main__":
  run()   