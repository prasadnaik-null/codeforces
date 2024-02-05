import re
numbers=[input(),input()]
actual_answer=int(numbers[0])+int(numbers[1])
actual_answe_with_out_zero=int(re.sub(r'0','',str(actual_answer)))
numbers_with_out_zero=[re.sub(r'0','',numbers[0]),re.sub(r'0','',numbers[1])]
false_answer=int(numbers_with_out_zero[0])+int(numbers_with_out_zero[1])
if actual_answe_with_out_zero==false_answer:
    print("YES")
else:
    print("NO")